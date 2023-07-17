import math

tolerance = 0.000001

def newton(n):
    estimate = 1.0
  
    while True:
        estimate = (estimate + n / estimate) / 2
        dierence = abs(n - estimate ** 2)
        if dierence <= tolerance:
            break
      
    return estimate


def main():
    while True:
        number = input("Enter a positive number or press Enter to exit: ")
        if number == "":  
            break
        number = float(number)
        estimate = newton(number)
        
        print("The program's estimate is ", estimate)
        print("Python's estimate is ", math.sqrt(number))


if __name__ == "__main__":
  main()
