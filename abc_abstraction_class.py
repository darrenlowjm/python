import pytest

def do_something(num):    
    return num 
   
@pytest.mark.ignore   
def test_something_1():
    assert do_something(10) == 9
    
def test_something_2():
    print("test 2")

import time 

import random

name_original = 'christopher'
name =  list(name_original)
for num in range(100000):
    #time.sleep(0.01)
    random.shuffle(name)
    
    
    print(f'{num+1}. Hi there I am {"".join(name)}')
    if name == list(name_original):
        print('Hit!')
        break
  