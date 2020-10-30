# def function(param):
#     print(param)

# function("***** hello world *****")

# print(divmod(10,3)) # (3,1) (x//y,x%y)

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))

# a=10
# b=20
# print(id(a),id(b))
# a=b
# print(id(a),id(b))

# file_object = open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/test.txt','w')
# file_object.write('hello kimdohyun')
# file_object.close()

# file_object = open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/test.txt','r')
# line = file_object.readline()
# print(line)
# file_object.close()

# with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/test.txt','r') as file_object:
#     line = file_object.readline()
#     print(line)

#list -> file
# names = ['kimdohyun','mike','david']

# with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/name.txt','w') as file_obj:
#     for name in names:
#         file_obj.write(name + '\n')
#     file_obj.writelines(names)
#     print('--- program write end ---')

# with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/name.txt','r') as file_obj:
#     lines = file_obj.readlines()
#     print('type(lines) : {}'.format(type(lines)))
#     for line in lines:
#         print(line,end="")
#     print("\n--- program read end ---")

#문제 name.txt -- 복사 --> name_copy.txt

# names = []
# with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/name.txt','r',encoding='utf-8') as file_obj:
#     names = file_obj.readlines()

# with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/name_copy.txt','w',encoding='utf-8') as file_obj_copy:
#     for index, name in enumerate(names):
#         file_obj_copy.write(str(index+1) +'\t'+ name)

# #파일 encoding utf-8

# ##파일 암호화 
# print(ord("여"))
# print(chr(50668))

# num = int(ord("여"))+10 # 암호화 알고리즘
# print(num)
# print(chr(50678))

# ##파일 복호화 -10
# print(chr(50678-10))

#예제 암호화와 복호화
inFp, outFp = None, None #파일 obj
inStr, outStr = '',''

secu_num = 0 #암호화 알고리즘 핵심

select = int(input("1: 암호화, 2: 복호화 //번호를 선택해주세요."))
in_file_name = input("입력 파일명 저장: ")
out_file_name = input("저장 파일명 저장: ")

if select == 1:
    secu_num = 100 #암호화
elif select == 2:
    secu_num = -100 #복호화

inFp = open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/'+in_file_name,'r',encoding='utf-8')
outFp = open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/'+out_file_name,'w',encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ''
    for i in range(len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu_num
        ch2 = chr(chNum)
        outStr = outStr + ch2 #문자열 만들기

    outFp.write(outStr)
        
outFp.close()
inFp.close()

print(f"{in_file_name} ---> {out_file_name} : 암호화 변환완료")
print("--- program end ---")