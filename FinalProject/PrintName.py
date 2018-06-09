# 프로그래밍 입문 기말프로젝트 #2

# 화면 비울시에 필요한 os 모듈 임포트
import os

# 안내 사항 및 문자 입력, 화면 클리어 처리
print("name.txt를 수정해 출력되는 문자의 형태를 변경할 수 있습니다.")
str_ipt = input("문자를 입력해주세요")
os.system('cls')

# 파일 열기
f = open("name.txt", 'r')

# 기타 변수 초기화
text = f.read().splitlines()
line =[[], [], []]
cnt = 0

# line 리스트에 파일의 내용을 2차원 리스트로 정리
for i in range(3):
    while True:
        line[i].append(text[cnt])
        cnt += 1
        if cnt >= len(text) or text[cnt] == '' : 
            break          
    cnt += 1

# 3중 포문으로 입력받은 문자로 이름 출력
for i in range((cnt-3)//3):
    for j in range(len(line)):
        for k in range(len(line[j][i])):
            if line[j][i][k] == '1':
                print(str_ipt, end='')
            else:
                print(" ", end='')
        print("", end='\t')
    print("")


## 이 친구가 돌아가는 이유는?
#for i in range(len(line[i])):
#    print(i)
#    cnt += 1

f.close()