fb = [input() for _ in range(3)]

def isFB(s):
    if s == "Fizz" or s == "Buzz" or s == "FizzBuzz":
        return True
    return False

def getFB(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

if not isFB(fb[0]):
    getFB(int(fb[0]) + 3)
elif not isFB(fb[1]):
    getFB(int(fb[1]) + 2)
else:
    getFB(int(fb[2]) + 1)