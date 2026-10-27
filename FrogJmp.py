def solution(X, Y, D):
    #calculates the distance needed to travel
    distance = Y - X

    #calculates the jumps by dividing the distance by D and rounding to the nearest whole number because the frog only jumps a fixed distance
    jumps = distance // D

    #calculates the remainder of the distance divided by D, if its not 0, add an extra jump to jump the remainder of the distance 
    if distance % D != 0:
        jumps = jumps + 1

    return jumps
