import numpy as np
import datetime
import math

from numpy import random

MIN_MAGIC_NUMBER = 1
MAX_MAGIC_NUMBER = 100

def binarySearch(array, x, lowIndex:int, highIndex:int):
    # stores number of attempts
    attempt = 0
    
    # input array must be sorted
    array.sort()
    
    # Repeat until the pointers lowIndex and highIndex meet each other
    while lowIndex <= highIndex:
        
        # calculate number of attempts
        attempt = attempt + 1
        
        # get the midIndexdle point of input array
        midIndex = lowIndex + (highIndex - lowIndex)//2

        if array[midIndex] == x:
            return (midIndex, attempt)
                
        elif array[midIndex] < x:
            lowIndex = midIndex + 1

        else:
            highIndex = midIndex - 1
 
    return (None, attempt)

def benchmark(array, repetitions):
    step = repetitions
    attemps = []
    
    # generate array of random magic numbers
    magic_array = random.randint(MIN_MAGIC_NUMBER, MAX_MAGIC_NUMBER + 1, size=(repetitions))
    
    # measure time spent for calculations
    dtStart = datetime.datetime.now()
    
    while step >= 0:
        position, attempt = binarySearch(array, magic_array[step - 1], 0, len(array)-1)
        if position == None:
            raise Exception(f'Something goes terrible wrong. The magic number {magic_array[step - 1]} was not found in the array set')
        
        # save attempt result
        attemps.append(attempt)
        
        # move to the next step
        step = step - 1
    
    # stop time measurement
    dtStop = datetime.datetime.now()    
    
    # spent time
    spent_time = dtStop - dtStart
    spent_time_ms = int(spent_time.total_seconds() * 1000)
    
    # calculate statistics
    avg_attempt = round(sum(attemps) / len(attemps), 4)
    max_attempt = max(attemps)
    min_attempts = min(attemps)
    
    print('==================================')
    print('====== Benchmark results =========')
    print('==================================')
    print(f'== Total attempts: {repetitions} in {spent_time_ms} milliseconds')
    print(f'== Average attempts count per try: {avg_attempt}')
    print(f'== Max attempts count per try: {max_attempt}')
    print(f'== Min attempts count per try: {min_attempts}')
    
    

# generate magic number
magic_number = np.random.randint(MIN_MAGIC_NUMBER, MAX_MAGIC_NUMBER + 1)

print(f'Компьютер загадал число \'{magic_number}\'')

# generate array of number variants
array = list(range(MIN_MAGIC_NUMBER, MAX_MAGIC_NUMBER + 1))

position, attempt = binarySearch(array, magic_number, 0, len(array)-1)

if position != None:
    found_x = array[position]
    print(f'Загаданное число \'{found_x}\' было угадано с {attempt} попытки\n')
else:
    print(f'К сожалению загаданное по условию число \'{magic_number}\' не удалось обнаружить в массиве вариантов\n')

# do the benchmark
try:
    benchmark(array, 1000000)
except Exception as ex:
    print(ex)
