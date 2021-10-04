#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 10
day = 8

def test_code():
    assert main.hasL("cat") == False, 'hasL("cat") == False failed'
    assert main.hasL("qwertyuiop") == False, 'hasL("qwertyuiop") == False failed'
    assert main.hasL("aergjnsdgljpyj") == True, 'hasL("aergjnsdgljpyj") == True failed'
    assert main.hasL("pool") == True, 'hasL("pool") == True failed'


def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
