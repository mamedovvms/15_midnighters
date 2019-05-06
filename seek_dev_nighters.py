from datetime import datetime
import pytz
import requests


URL = 'http://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    page = 1
    while True:
        params = {'page': page}
        response = requests.get(URL, params)
        page += 1
        if not response.ok:
            return False
        decoded_json = response.json()
        yield from decoded_json['records']


def get_local_date(timestamp, timezone):
    tz = pytz.timezone(timezone)
    local_date = datetime.fromtimestamp(timestamp, tz=tz)
    return local_date


def get_midnighters():
    midnighters = {}
    for record in load_attempts():
        timezone = record['timezone']
        timestamp = record['timestamp']
        username = record['username']
        local_date = get_local_date(timestamp, timezone)
        if local_date.hour <= 6:
            midnighters[username] = local_date.strftime('%H:%M:%S %Y.%m.%d')
    return midnighters


def print_midnighters(midnighters):
    if not len(midnighters):
        print('Нет ни одного полуночника')
        return

    for username, local_date in midnighters.items():
        print('Пользователь: {} отправил {}'.format(username, local_date))


def main():
    midnighters = get_midnighters()
    print_midnighters(midnighters)


if __name__ == '__main__':
    main()
