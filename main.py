def happy(num):
    check = []
    check.sort()
    list = [int(i) for i in str(num)]
    while num != 1:
        num = sum(num**2 for i in str(num))
        if num in check:
            print(f'{num} is not a happy number')
        check.append(num)
        check.sort()
    print(f'{num} is a happy number')

number = int(input('Enter number'))
happy(number)
