# import pdb

# def multiplication (a, b):
#     answer = a * b
#     return answer
# pdb.set_trace()
# x = input("Enter first number: ")
# y = input("Enter second number: ")
# result = multiplication(x, y)
# print(result)




def multiplication (a, b):
    answer = a * b
    return answer
breakpoint() # same as pdb.set_trace() # we can use this in Python 3.7 and above # don't need to import pdb
x = input("Enter first number: ")
y = input("Enter second number: ")
result = multiplication(x, y)
print(result)