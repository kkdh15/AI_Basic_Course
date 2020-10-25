# a / b => 'b!=0'
# a = 10
# b = 0

# if (b!=0):
#     print(a / b)

# # Exception class
# try:
#     #print(10 / 0)
#     str = 'abcdef'
#     print(str[9])
# except ZeroDivisionError:
#     print('ZeroDivisionError 발생')
# except IndexError:
#     print("IndexError 발생")
# else: #Error 발생하지 않으면 동작
#     print("Error 발생하지 않으면 동작")
# finally:
#     print("무조건 동작")

def get_pizza_name():
    print('banolrim pizza')
    raise NotImplementedError

get_pizza_name()