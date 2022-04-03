"""Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number 
and for multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz' """

# using modulo is the key to solving this problem.

def fizzbuzz():
    for i in range(0,101):
        if i % 3==0 and i % 5==0:
            print("FizzBuzz")
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)
fizzbuzz()