# #Stack / append() pop() LIFO(Last In First Out)
# stack = []
# stack.append("A")
# stack.append("B")
# stack.append("C")
# print(stack)
# print(stack.pop())
# print(stack)

# #Queue / append() pop() FIFO(First In First Out)
# queue = []
# queue.append("A")
# queue.append("B")
# queue.append("C")
# print(queue)
# print(queue.pop(0))
# print(queue)

# print(type(stack))
# print(type(queue))

# #list comprehension : 코드를 짧게 쓰자
# list = []
# for i in range(6):
#     if (i%2==1):
#         list.append(i)
# print(list)

# list2 = [i for i in range(6) if i%2==1]
# print(list2)

# list3 = [x*y for x in range(1,6,1) for y in range(1,6,1)]
# print(list3)

# #list list 1D -> 2D
# list2D = [[1,2,3],[4,5,6],[7,8,9]]
# print(list2D)

# for i in range(3):
#     for j in range(3):
#         print(list2D[i][j], end=" ")
#     print()

#1
matrix=[]
for i in range(5):
    row = []
    for j in range(5):
        row.append(0) # 0 0 0 0 0
    matrix.append(row)
print(matrix)

#2
matrix = [[0 for i in range(5)] for j in range(5)] 
print(matrix)

# # #3 얇은 복사 발생 문제
# # matrix=[[0]*5]*5
# # print(matrix)

num=1
for i in range(5):
    if i%2==0:
        for j in range(5):
            matrix[i][j] = num
            num += 1
    else:
        for j in range(4,-1,-1):
            matrix[i][j] = num
            num += 1

#출력부
for i in range(5):
    for j in range(5):
        print("{0:2}".format(matrix[i][j]),end=" ")
    print()
print()

for arr in matrix:
    for num in arr:
        print("{0:2}".format(num),end=" ")
    print()