# 프로그래밍 입문 기말프로젝트 #2

f = open("name.txt", 'r')

line = f.read().splitlines()
cnt = 0

#if line[0][9] == '1':
#    print('*')

for i in range(len(line)):
    for j in range(len(line[i])):
        if line[i][j] == '1':
            print("*", end='')
        else:
            print(" ", end='')

    #cnt += 1
    #print(line[i][j])
    print()
    
            
f.close()