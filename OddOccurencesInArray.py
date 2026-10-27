def solution(A):
    if len(A) == 0:
        return A #technically not needed because says array is always non empty but added just in case
    
    #create a dictionary to store numbers
    counts = {}

    #for loop to find the numbers in the array and add it to the dictionary
    for number in A:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1
    #checks if the remainder of the count of the number is not zero, or in other words has no pairs.
    for number in counts:
        if counts[number] % 2 != 0:
            return number
