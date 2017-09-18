#!/bin/python

import os
import logging
import multiprocessing

from multiprocessing import Process, Lock, Pool

def doubler(number):
    result = number * 2
    proc = os.getpid()
    #lock.acquire()
    #try:
    print('{0} doubled to {1} by process id: {2}'.format(number, result, proc))
    #finally:
        #lock.release()

if __name__=='__main__':
    lock = Lock()
    numbers = [5,10,15,20,25]
    pool = Pool(processes=3)

    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    pool.map(doubler, numbers)

    #for index, number in enumerate(numbers):
    #    proc = Process(target=doubler, args=(number,lock,))
    #    proc.start()
