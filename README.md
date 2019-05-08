# Night Owls Detector

The program takes data to the address of the form 
https://devman.org/api/challenges/solution_attempts/?page=2.
In the data obtained selects records in which the time in the range 
from 00 hours to 6 am. The result is a list of login and time.

# Examples

```bash
$ python bars.py seek_dev_nighters.py# possibly requires call of python3 executive instead of just python\
User: id57193343
User: vmamedov1984
User: ZaurAgamov
...
```
Running on Windows is similar.

If no matching entries were found, a corresponding message will be displayed.
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
