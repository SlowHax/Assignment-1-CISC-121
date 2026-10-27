def solution(A, K):
#if the length of the array A is zero then nothing happens
    if len(A) == 0:
        return A
#stores the last integer of the array in a variable called "last"
    for i in range(K):
        last = A[-1]

#This is a for loop that takes the accurate range of A using the length of A - 1, and moves every item in the array one spot to the right  
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j - 1] #puts the value from the position just to the left of the current position

        A[0] = last #puts the old last number at the beginning

    return A
