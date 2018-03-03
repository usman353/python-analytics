import _thread
import time
import random


def runOften(threadname, sleeptime):
    while True:
        time.sleep(sleeptime)
        print('%s' % threadname)


def runlessOften(threadname, sleeptime):
    while True:
        time.sleep(sleeptime)
        print('%s' % threadname)


def runRandom(threadname, sleeptime):
    while True:
        time.sleep(sleeptime)
        print('%s' % threadname)
try:
    _thread.start_new_thread(runOften,('Often runs',2))
    _thread.start_new_thread(runlessOften,('less Often runs',2))
    _thread.start_new_thread(runRandom,('Often random runs',random.random()))
except Exception as e:
    print(e)
