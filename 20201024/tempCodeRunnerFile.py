with open('C:/Users/82109/Desktop/Study/AI Basic Course/20201024/name.txt','r') as file_obj:
    lines = file_obj.readlines()
    print('type(lines) : {}'.format(type(lines)))
    for line in lines:
        print(line,end="")
    print("\n--- program read end ---")
