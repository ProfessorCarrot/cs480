import random
from random import randint
import time

N = int(input('Enter a value for N: ')) #user input
X = int(input('Enter a value for X: ')) #user input
MAX_RANGE = 10000

#-----------------------------------------------------  
#Part A.2.a
i = 1
temp = 0
incList = []
for i in range(1,N+1):
   temp = N+(i*X)
   incList.append(temp)
   i += 1

#-----------------------------------------------------  
#Part A.2.b
j = 0
randomList = []
randInt = 0
for j in range(N):
   randInt = random.randrange(0, MAX_RANGE)
   randomList.append(randInt)
   j += 1

#-----------------------------------------------------
#This implementation of quicksort is from
#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

#-----------------------------------------------------
#This implementation of a randomized quicksort is from
#https://gist.github.com/hrsenvar/83b23f1d6bc7e545d3f45f07fce4a8d0
def quick_sort(A,low,high):
    if low<high :
        p=partition(A,low,high)
        quick_sort(A,low,p-1)
        quick_sort(A,p+1,high)
def partition(A,low,high):
    pivot_index=randint(low,high)
    pivot_value=A[pivot_index]
    A[low],A[pivot_index]=A[pivot_index],A[low]
    i=low
    for j in range(low,high+1):
        if A[j]<pivot_value :
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i],A[low]=A[low],A[i]
    return i

#-----------------------------------------------------   
usList = str(randomList) #unsorted list
inc = str(incList) #incremented list

quicksortedList = []
randomQuicksortedList = []
incQuicksortedList = []
incRandomQuicksortedList = []
#-----------------------------------------------------
#Quicksort
quicksortTimeStart = time.clock()
quickSort(randomList)
quicksortTimeEnd = time.clock()
quicksortedList.extend(randomList)

qsList = str(quicksortedList) #Quicksort
 
#Randomized Quicksort
randQuicksortTimeStart = time.clock()
quick_sort(randomList,0,len(randomList)-1)
randQuicksortTimeEnd = time.clock()
randomQuicksortedList.extend(randomList)

rqsList = str(randomQuicksortedList) #Randomized quicksort

#----------------------------------------------------- 
#Increasing order quicksort
incQuicksortTimeStart = time.clock()
quickSort(incList)
incQuicksortTimeEnd = time.clock()
incQuicksortedList.extend(incList)

incqsList = str(incQuicksortedList) #Increasing order quicksort

#Increasing Randomized Quicksort
incRandQuicksortTimeStart = time.clock()
quick_sort(incList,0,len(incList)-1)
incRandQuicksortTimeEnd = time.clock()
incRandomQuicksortedList.extend(incList)

incrqsList = str(incRandomQuicksortedList) #Increasing Randomized quicksort

#-----------------------------------------------------  
#Output
print('Quicksort time: ', quicksortTimeEnd - quicksortTimeStart)
print('Randomized quicksort time: ', randQuicksortTimeEnd - randQuicksortTimeStart)
print('Increasing Quicksort time: ', incQuicksortTimeEnd - incQuicksortTimeStart)
print('Increasing Randomized quicksort time: ', incRandQuicksortTimeEnd - incRandQuicksortTimeStart)

#-----------------------------------------------------  
#Opens and writes to the file, creates one if one does not exist
f = open('output.txt', 'w')

f.write('Unsorted: \n' + usList + '\n')
f.write('\nSorted with QuickSort: \n' + qsList + '\n')
f.write('\nSorted with Randomized QuickSort: \n' + rqsList + '\n')
f.write('\nIncreasing order(Part A.2.a): \n' + inc + '\n')
f.write('\nIncreasing order quicksort: \n' + incqsList + '\n')
f.write('\nIncreasing order random quicksort: \n' + incrqsList)
f.close()
  
input("\nPress Enter to continue.")
