age = int(input('what is your age: '))


if age in range(18, 60):
    print('شما میتوانید کار کنید')
else:
    print('شما نمیتوانید کار کنید')

if age < 18 or age > 60:
    print('شما نمیتوانید کار کنید')
else:
    print('شما میتوانید کار کنید')