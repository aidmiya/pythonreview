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
    print('FizzBuzz を行います．')
    print('FizzBuzz1 関数の場合')
    FizzBuzz1()
    print('FizzBuzz2 関数の場合')
    FizzBuzz2(1, 30)
    print('終わります．')
