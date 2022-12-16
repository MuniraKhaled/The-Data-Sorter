#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 04:17:35 2022

@author: areejalmisfer 
"""

from random import randint

def randomizeQS(numbers,start,end):
    if start<end:
        pivot=randint(start,end)
        numbers[end],numbers[pivot]=numbers[pivot],numbers[end]

        p=Partitioning(numbers,start,end)
        randomizeQS(numbers,start,p-1)
        randomizeQS(numbers,p+1,end) 
 
   # find partition 
def Partitioning(numbers, p, q): 
    i = p - 1
    pivot = numbers[q]
 
    for j in range(p, q):
        if numbers[j] <= pivot:
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1], numbers[q] = numbers[q], numbers[i + 1]

    return i+1