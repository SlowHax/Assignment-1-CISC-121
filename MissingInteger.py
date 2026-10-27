def solution(A):

    #check to see the array has numbers in it
    if len(A) == 0:
        return A
    
    #create a dictionary to store the positive numbers in A
    numbers = {}

    #for loop to find all of the positive integers in A and add them to the dictionary
    for number in A:
        if number > 0:
            numbers[number] = True
    
    #create a variable "missing" because the rules say to find all numbers 0<
    missing = 1

    #while loop to find the smallest positive number in the array. Adds +1 to missing if it is found in the array since the number is found
    while missing in numbers:
        missing = missing + 1

    return missing
