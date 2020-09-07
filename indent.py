name = input('enter your name: ')
age = int(input('what is your age {}? '.format(name)))
print(age)

# if age >= 18:
#     print('شما میتوانید رانندگی کنید {}'.format(name))
#     print('البته قبلش باید گواهی نامه بگیرید')
# elif age == 100:
#     print('تو دیگه خیلی پیر شدی بهتره استراحت بکنی البته اگه هنوز زنده ای')
# else:
#     print('شما اجازه رانندگی ندارید')

if age < 18:
    print('شما اجازه رانندگی ندارید')
elif age == 100:
    print('تو دیگه خیلی پیر شدی بهتره استراحت بکنی البته اگه هنوز زنده ای')
else:
    print('شما میتوانید رانندگی کنید {}'.format(name))