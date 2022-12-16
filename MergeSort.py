#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:31:53 2022

@author: arobalqurashi
"""

#the algo in pain english 
   # 1. Find the middle point to divide the array into two halves:  
     #        middle m = l+ (r-l)/2
    # 2. Call mergeSort for first half:   
      #       Call mergeSort(arr, l, m)
     #3. Call mergeSort for second half:
      #       Call mergeSort(arr, m+1, r)
     #4. Merge the two halves sorted in step 2 and 3:
      #       Call merge(arr, l, m, r)
      
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            

  
