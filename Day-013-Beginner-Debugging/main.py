def odd_or_even(number):
    if number % 2 == 0:      #Instead of == equality operator, assignment operator was used
        return "This is an even number."
    else:
        return "This is an odd number."
    

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:     #Instead of 400, it was mistakenly written 4000
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:  #Instead of and, or was used in the condition
            print("FizzBuzz")
        elif number % 3 == 0:       #Instead of elif, only if was written which may print all conditions if all are true
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)   #Instead of printing the number it enclosed variable in [] brackets
