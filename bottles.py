#! /usr/env/ python3

for bottles in range(99, 0):

    if bottles == 1:
        print( "1  bottles of beer on the wall!")
        print("1 bottles of beer on the wall! 1 bottles of beer! You take one down and pass it around!")
    else: 
        print(bottles, " bottles of beer on the wall!")
        print(bottles, "bottles of beer!", bottles,"bottles of beer on the wall! You take one down, pass it around")
