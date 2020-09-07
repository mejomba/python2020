# file = open('file.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()

# with open('file.txt', 'r') as file:
#     for line in file:
#         print(line, end='')

# with open('file.txt', 'r') as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

# with open('file.txt', 'r') as file:
#     lines = file.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')

# with open('file.txt', 'r') as file:
#     lines = file.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')

with open('file.txt', 'r') as file:
    lines = file.read()
print(lines)
# for line in lines[::-1]:
#     print(line, end='')










