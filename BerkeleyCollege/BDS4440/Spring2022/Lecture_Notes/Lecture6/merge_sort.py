"""Run the merge sort algorithm and (optionally) print the steps"""
#example1 python merge_sort.py -l [35,73,90,65,23,86,43,81,34,58] #run with printing steps
#example2 python merge_sort.py -l [35,73,90,65,23,86,43,81,34,58] -p False #run with printing steps
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-l","--list_data", default=None, help="data must be in list or array format")
ap.add_argument("-p","--print_steps", default="True", type=str, help="print the steps of the merge")
args = vars(ap.parse_args())

def subarray_string(data,low,high):
    temp = '  '*low
    temp += ' '.join(str(item) for item in data[low:high+1])
    return temp

def sort_array(data,low,high,print_steps):
    """Split data, sort subarrays and merge them into a sorted array."""
    #test base case size of array equals 1
    if (high-low)>=1: #if not base case
        middle1 = (low+high)//2 #calculate the middle of array
        middle2 = middle1 + 1
        
        #output split step
        if print_steps:
            print(f'split: {subarray_string(data,low,high)}')
            print(f'       {subarray_string(data,low,middle1)}')
            print(f'       {subarray_string(data,middle2,high)}\n')
        
        #split array in half then sort each half (recursive calls)
        sort_array(data,low,middle1,print_steps)
        sort_array(data,middle2,high,print_steps)
        return merge(data,low,middle1,middle2,high,print_steps)
        
def merge(data,left,middle1,middle2,right,print_steps):
    left_index = left #index into left subarray
    right_index = middle2 #index into right subarray
    combined_index = left #index into temporary working array
    merged = [0]*len(data) #working array
    
    #output two subarrays before merging
    if print_steps:
        print(f'merge: {subarray_string(data,left,middle1)}')
        print(f'       {subarray_string(data,middle2,right)}')
    
    #merge arrays until reaching end of either
    while left_index <= middle1 and right_index <= right:#place smaller of two current elements into result and move to next space in arrays
        if data[left_index]<=data[right_index]:
            merged[combined_index] = data[left_index]
            combined_index+=1
            left_index+=1
        else:
            merged[combined_index]=data[right_index]
            combined_index+=1
            right_index+=1
            
    #if left array is empty
    if left_index == middle2: #if true, copy in rest of right array
        merged[combined_index:right+1] = data[right_index:right+1]
    else: #right array is empty, copy in rest of left array
        merged[combined_index:right+1] = data[left_index:middle1+1]
        
    data[left:right+1] = merged[left:right+1]
    if print_steps:
        print(f'         {subarray_string(data,left,right)}\n')
    return data
    
def merge_sort(data,print_steps):
    array = sort_array(data,0,len(data)-1,print_steps)
    if not print_steps:
        print(array)
    return array


data = eval(args["list_data"]) #convert string into list
data = [float(j) for j in data] #convert to list of floats
print_steps = args["print_steps"]
if print_steps in [0,'0','False','false',False]:
    print_steps=False
else:
    print_steps=True

merge_sort(data,print_steps)