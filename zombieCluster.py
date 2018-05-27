#!/bin/python3

import sys
import os


# Complete the function below.

def zombieCluster(zombies):
	N = len(zombies)
    	cluster = range(N)
    	for i in range(N):
        	for j in range(i + 1, N):
            		if zombies[i][j] == '1':
                		cluster[j] = min(cluster[i], cluster[j])
                		cluster[i] = cluster[j]
	print cluster
	return len(set(cluster))
input = ['100001',
                '010001',
                '001001',
                '000101',
                '000011',
'111111']

print zombieCluster(input)
