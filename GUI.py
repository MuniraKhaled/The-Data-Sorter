#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:28:02 2022

@author: arobalqurashi
"""

import time
import QuickSortAlgo
import MergeSort
import Randomized
import selectSortAlgo
import mdian_of_medians

from tkinter import *
import tkinter as tk

window  = tk.Tk()
window.title('Sorting Algorithms')
window.geometry('600x400')


lbl= tk.Label(text='WELCOME TO OUR SORTING ALGORITHMS PROJECT', font=('Arial Bold',15))
lbl.pack()

lbl1= tk.Label(text='Please choose from our menu:')
lbl1.pack()


''''''
def readlist():
    #opening the file in read mode
    myFile = open("reading_file.txt","r")
    numbers = []
    for number in myFile: 
        numbers.append(int(number))
     
    myFile.close()
    return numbers

numbers = readlist()
size = len(numbers)  
''''''


''''''
def write():
    writeCodeIn = open("writing_file.txt","w")

    for i in range(size):
        writeCodeIn.write(str(numbers[i])+"\n")
        
    writeCodeIn.close() 
''''''


''''''
def Quick_Sort():
    start = time.process_time()
    QuickSortAlgo.quickSort(numbers, 0, size-1)
    print(time.process_time()-start)
    write()
    print("<<< Quick Sort >>> is done and the result is installed in writing_file.txt")
''''''

 
''''''
def Merge_Sort():
    start = time.process_time()
    MergeSort.mergeSort(numbers)
    print(time.process_time()-start)
    write()
    print(" <<< Merge Sort >>> is done and the result is installed in writing_file.txt")
''''''

    
''''''
def Randomized_Sort():
    start = time.process_time()
    Randomized.randomizeQS(numbers, 0, size-1)
    print(time.process_time()-start)
    write()
    print(" <<< Randomized Sort >>> is done and the result is installed in writing_file.txt")
''''''


''''''
def Select_Sort():
    start = time.process_time()
    selectSortAlgo.selectionSort(numbers)
    print(time.process_time()-start)
    write()
    print(" <<< Select Sort >>> is done and the result is installed in writing_file.txt")
''''''


''''''
def mdian_finding():
    hey = mdian_of_medians;
    start = time.process_time()
    hey.findMedian(numbers,size)
    print(time.process_time()-start)
    print(" <<< Median finding >>> is done and the medin is : "+ str(hey.ans))
''''''

#button
b1=tk.Button(text = '1.Quick Sort Algorithm', command = Quick_Sort)
b1.pack()

b2=tk.Button(text = '2.Merge Sort Algorithm', command = Merge_Sort )
b2.pack()

b3=tk.Button(text = '3.Randomized Quick Sort Algorithm', command = Randomized_Sort)
b3.pack()

b4=tk.Button(text = '4.Select Sort Algorithm' , command = Select_Sort)
b4.pack()

b5=tk.Button(text = '5.Median Finding', command = mdian_finding)
b5.pack()

b6=tk.Button(text = '6.EXIT',command=window.destroy)
b6.pack()

window.mainloop()