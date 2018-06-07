# 프로그래밍 입문 기말프로젝트 #1
from graphics import *
import sys


# 오류 발생 시 실행하는 함수
def isExcept():
    while True:
        n = int(input("""1: 파일명 재입력
2: 프로그램 종료
"""))
        # 파일명을 재 입력하고 싶으면 재입력하고
        if n == 1:
            return True
        # 종료하고 싶으면 sys.exit()함수를 이용해 종료한다
        elif n == 2:
            sys.exit()
        else:
            print("1 혹은 2 값을 입력해주세요")


# 그래프 창 그리기
def drawWin(wordCnt):
    win = GraphWin("CountWord", 1000, 500)
    win.setBackground("white")
    win.setCoords(-50, 550, 1050, -50)

    for i in range(8):
        x = 50 + 120 * i
        Text(Point(x, 450), wordCnt[i][0]).draw(win)

        bar = Rectangle(Point(x - 20, 430), Point(x + 20, 430 - 20 * wordCnt[i][1]))
        bar.draw(win)
        


    if win.getKey():
        win.close()



def main():
    # 파일 로딩
    while True:
        try:
            fName = input("파일명을 입력해주세요 < .txt 제외 >")

            file = open(fName+'.txt', 'r')
            # spilit으로 단어 나누기
            text = file.read().split()

        # 파일이 존재하지 않는 오류가 발생하면
        except FileNotFoundError:
            print("파일이 존재하지 않습니다")
            if isExcept(): continue

        # 예상치 못한 오류가 발생하면
        except Exception as e:
            print("다음과 같은 오류가 발생했습니다", e)
            if isExcept(): continue

        else: break
        
    wList = {}
    
    # 딕셔너리 형태로 문자 등장횟수 정리
    for i in text:
        wList[i] = text.count(i)

    # 딕셔너리를 이름순으로 정렬 후 등장빈도 순으로 정렬
    wList = sorted(wList.items(), key = lambda x: x[0])
    wList = sorted(wList, key = lambda x: x[1], reverse = True)

    print(wList)

    drawWin(wList)
    file.close()

main()