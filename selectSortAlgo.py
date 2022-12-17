# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:02:25 2022

@author: munirah
"""
# src : https://www.guru99.com/selection-sort-algorithm.html
def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList
 
