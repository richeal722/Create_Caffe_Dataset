#!/usr/bin/env python


import os
import sys
import random


try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    test = int(sys.argv[3])
    allNum = end-start+1
except:
    print 'Please input picture range'
    print './createTest.py 1 1500 500'
    os._exit(0)

b_list = range(start,end)
blist_webId = random.sample(b_list, test)
blist_webId = sorted(blist_webId) 
allFile = []

testFile = open('ImageSets/Main/test.txt', 'w')
trainFile = open('ImageSets/Main/trainval.txt', 'w')

for i in range(allNum):
    allFile.append(i+1)

for test in blist_webId:
    allFile.remove(test)
    testFile.write(str(test) + '\n')
    
for train in allFile:
    trainFile.write(str(train) + '\n')
testFile.close()
trainFile.close()

#createTest.py
