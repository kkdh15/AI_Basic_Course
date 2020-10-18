#Key = Value
#dict = {key:value, key2:value2}

#생성
member = {"yeo":"12345","stu_num":"20201018","stu_name":"kimdohyun"} #json
temp_dict = {}
print(type(member))
print(member)

#검색
print(member['stu_num'])

#변경
member['stu_num'] = '20202020'
print(member['stu_num'])

#삭제
del member['yeo']
print(member)

#추가
member['phone_number'] = '01012345678'
print(member)

#내부 함수 확인
print(dir(member))
print()

print(member.items())
print(member.values())
values_list = list(member.values())

print(member.keys())
keys_list = list(member.keys())

print(values_list)
print(keys_list)

#Key : stu_num 존재여부
print("stu_num" in member)

#list = [1,2,3] , list2 = [seoul,inchon,busan]
#1:seoul, 2:inchon, 3:busan
list = [1,2,3]
list2 = ["seoul", "inchon", "busan"]
dic_place = dict(zip(list,list2))
print(dic_place)