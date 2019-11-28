def FizzBuzz2(b, e):
    for i in range(b, e+1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

if __name__ == "__main__":
    print('Hello World!')
