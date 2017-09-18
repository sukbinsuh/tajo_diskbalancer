#!/bin/python
import multiprocessing

import os
import logging
import multiprocessing

from multiprocessing import Process, Lock, Pool

cluster = []
local = []

def worker(num):
    """worker function"""
    #print 'Worker', num
    if num not in cluster:
        print num
    return

if __name__=='__main__':
    f1 = open("clusterblockinfo.txt")

    while True:
        line = f1.readline()
        if not line: break
        blocks = line.split()[1].split(":")[1].split("_")
        block = blocks[0] + "_" + blocks[1]
        #print block
        cluster.append(block)
    f1.close()

    print "--------------------------------------------------------"
    f2 = open("localhdfsinfo_data5.txt")

    while True:
        line = f2.readline()
        if not line: break
        block = line.split()[8]
        #print block
        local.append(block)
    f2.close()

    pool = Pool(processes=3)

    pool.map(worker, local)






