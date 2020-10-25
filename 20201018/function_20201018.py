# #함수
# #재사용
# def function_name(parameter): parameter 인수
    #code

# def my_print(argu):
#     print(argu)
#     print("program end")

# my_print("hello world")

# def plus(x,y):
#     print(x+y)

# def min(x,y):
#     print(x-y)

# def mux(x,y):
#     print(x*y)

# def div(x,y):
#     print(x,y)

# def cal(x,op,y):
#     result = 0
#     if op == '+':
#         result = x+y
#     elif op == '-': 
#         result = x - y   
#     elif op == '*':
#         result = x * y
#     elif op == '/':
#         result = x / y
#     else:
#         print("op입력을 다시 해주세요.")
#     return result

# print(cal(10,'+',20))
#행렬연산
def cal_matrix(x, op, y):
    result = [[0,0],[0,0]]

    if (type(x) != list) | (type(y) != list):
        print("x, y 에 2x2 행렬을 넣어 주세요")
        return result

    if op == '+':
        for i in range(2):
            for j in range(2):
                result[i][j] = x[i][j] + y[i][j]
                
    elif op == '-':
        for i in range(2):
            for j in range(2):
                result[i][j] = x[i][j] - y[i][j]
                
    elif op == '*':
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += x[i][k] * y[k][j]
        # result[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0]
        # result[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1]
        # result[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0]
        # result[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1]

        # result[i][j] = x[i][0] * y[0][j] + x[i][1] * y[1][j]
        # result[i][j] += x[i][k] * y[k][j]
                
    else:
        print("op 입력을 다시 해 주세요")

    return result

print(cal_matrix([[1,2],[3,4]],"*",[[5,6],[7,8]]))

#Default parameter
def pow(x=10):
    return x * x

#name parameter
print(pow(x=20))

#가변길이 파라미터
#파라미터가 여러개 입력 *

def myprint(*num):
    print(num)

myprint(11,12,13,14)

#키워드 파라미터 **
#dictionary 값을 파라미터로 받는다.

def print_id(**kw_param):
    print(kw_param)

print_id(id="12345") #dictionary key = value ->id = "12345"

# 지역 전역 변수 
#return (output)
def func_return(param1): #input
    param1 += 1
    return param1 # output

def func_return2(): #input
    num1, num2 = 10, 20
    return num1, num2 # output

return_value = func_return(10)
return_value1, return_value2 = func_return2()
return_value3 = func_return2()

print(return_value,return_value1,return_value2)
print(return_value3)
print(type(return_value3))