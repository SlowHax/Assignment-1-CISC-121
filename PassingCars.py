def solution(A):
    east_cars = 0 #a variable that stores the amount of cars passing east
    passing_cars = 0#do the same for the cars passing west, since they always pass the cars going east, we call it "passing_cars"

    for car in A:
        if car == 0: #if car is going east
            east_cars += 1
        
        if car == 0: #if car is going west and passes.
            passing_cars += east_cars

        else: #if the car is not going east or west
          print("This car is not going east or west!)
    
    if passing_cars > 1000000000:
        return -1
    
    return passing_cars
