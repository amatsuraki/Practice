# -*- coding: utf-8 -*-

#num = 1
#fin_num = 51

num = input("Enter start number: ")
num_fin = input("Enter finish number: ")

num = int(num)
num_fin = int(num_fin)

while num < (num_fin + 1):
    
    if num%15 == 0:
        print("FizzBuzz")
     
    elif num%5 == 0:
        print("Buzz")
       
    elif num%3 == 0:
        print("Fizz")

    else:
        print(str(num))

    num += 1
       
