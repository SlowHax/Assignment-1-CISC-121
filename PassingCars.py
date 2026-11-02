def solution(A):
    east_cars = 0  # stores the number of cars traveling east
    passing_cars = 0  # stores the total number of passing car pairs

    for car in A:
        if car == 0:  # car is traveling east
            east_cars += 1

        else:  # car == 1, so it is traveling west
            passing_cars += east_cars

        # return -1 if the number of passing cars is too large
        if passing_cars > 1000000000:
            return -1

    return passing_cars
