import traceback
def add(a, b):
    return a / b


a = 1
b = 0
try:
    print(add(a, b))
except ZeroDivisionError as e:
    # print(e)
    # traceback.print_exc()
    pass
# except, err:
# #     print(err)
