def solution(A):
    passing_cars = 0
    cars_going_east = 0
    for i in A:
        if i == 0:
            cars_going_east += 1
        else:
            passing_cars += cars_going_east
        if passing_cars > 1000000000:
            return -1
    return passing_cars
