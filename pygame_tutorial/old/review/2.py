def fizz_buzz(num):
    for number in range(1, num + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz", end=" ")
        elif number % 3 == 0:
            print("fizz", end=" ")
        elif number % 5 == 0:
            print("buzz", end=" ")
        else:
            print(number, end=" ")
        
fizz_buzz(15)
# fizz_buzz(3)
# fizz_buzz(5)
# fizz_buzz(6)
# fizz_buzz(11)