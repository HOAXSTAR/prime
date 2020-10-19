""" this is a problem to get the determinent of a 2x2 matrix
"""
import numpy as np


def det(a):
    return a[0,0]*a[1,1] - a[0,1]*a[1,0]
    
    
first = list(map(int,input().split()))
second = list(map(int,input().split()))
a = np.array([first,second])

print(det(a))
