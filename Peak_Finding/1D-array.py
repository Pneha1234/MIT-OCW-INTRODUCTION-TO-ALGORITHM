# question: to find the peak of one dimensional array
# statement: a peak is any element b such that b-1<= b >=b+1,
# edge_case definition: a peak is any element b such that b>=b-1 or b>=b+1
# suggested method:
#  if b[n/2]<b[n/2 -1] then only look at left half 1..n/2
#  elif b[n/2]< b[n/2+1] then only look at right half n/2 +1
# else n/2 is the peak
# time complexity 0(logn)

# solution

def find_a_peak(array):
    if len(array) == 0:
        return None

    if len(array) == 2:
        return array[1]

    half = len(array) // 2
    

    if array[half - 1] < array[half] and array[half] > array[half + 1]:
        return array[half]
    

    if array[half - 1] >= array[half]:
        peak = find_a_peak(array[0:half])
        if peak:
            return peak
            

    if half >= 1 and array[half + 1] >= array[half]:
        peak = find_a_peak(array[half:len(array)])
        if peak:
            return peak

def find_peak(array):
    return find_a_peak(array)


size = int(input('Enter size of array: '))
array = [int(input(F'Enter {i}th value: ')) for i in range(size)]
    
print("Index of a peak point is", find_peak(array))

