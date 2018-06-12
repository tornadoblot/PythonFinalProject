# 프로그래밍 입문 기말프로젝트 #1
from graphics import *
import sys


# 오류 발생 시 실행하는 함수
def isExcept():
    while True:
        n = input("""1: 파일명 재입력
2: 프로그램 종료
""")
        # 파일명을 재 입력하고 싶으면 재입력하고
        if n == '1':
            return True
        # 종료하고 싶으면 sys.exit()함수를 이용해 종료한다
        elif n == '2':
            sys.exit()
        # 1 또는 2 값이 아닐 경우 재 입력
        else:
            print("1 혹은 2 값을 입력해주세요")
            continue


# 그래프 창 그리기
def drawWin(wordCnt):
    # 기본 창 설정
    Width = 1000
    Height = 700
    win = GraphWin("CountWord", Width, Height)
    win.setBackground("lavenderblush")
    win.setCoords(-50, Height + 50, Width + 50, -50)

    # 중앙 설명 텍스트 설정
    mTxt = Text(Point(Width//2, -10), "그래프창 활성화 후 Enter키를 누르면 종료합니다")
    mTxt.setStyle("bold italic")
    mTxt.setSize(18)
    mTxt.setTextColor("mediumvioletred")
    mTxt.draw(win)

    # 정렬 기준 설명 텍스트 제작    

    # 왼쪽 라인 기본 설정
    Line(Point(0, Height - 30), Point(0, 20)).draw(win)
    Line(Point(0, Height - 30), Point(10, Height - 30)).draw(win)
    Text(Point(-10, Height - 30), "0").draw(win)
    Line(Point(0, 20), Point(10, 20)).draw(win)

    # 그래프 그리기
    for i in range(8):
        # x, y값 초기화
        x = 50 + 130 * i
        y = Height -30 - 20 * wordCnt[i][1]
        # 많이 등장한 단어를 텍스트로 출력
        Text(Point(x, Height - 10), wordCnt[i][0]).draw(win)

        # y값이 특정 높이를 넘어섰을 때 일괄적으로 높이 설정
        if y <= 20:
            # 그래프 바 설정
            bar = Rectangle(Point(x - 20, Height - 30), Point(x + 20, 20))
            bar.setWidth(0)
            bar.setFill("hotpink")
            bar.draw(win)

            # 바 중간에 들어가는 텍스트 설정
            txt = Text(Point(x, 225), str(wordCnt[i][1]))
            txt.setTextColor("white")
            txt.draw(win)

            # 각 바에 따른 왼쪽 기준 라인 설정
            Line(Point(0, 20), Point(10, 20)).draw(win)
            Text(Point(-10, 20), str(wordCnt[i][1])).draw(win)

        else:
            # 빈도수에 따른 그래프 바 설정
            bar = Rectangle(Point(x - 20, Height - 30), Point(x + 20, y))
            bar.setWidth(0)
            bar.setFill("hotpink")
            bar.draw(win)

            # 바 중간에 들어가는 텍스트 설정
            txt = Text(Point(x, y + 10 * wordCnt[i][1]), str(wordCnt[i][1]))
            txt.setTextColor("white")
            txt.draw(win)
            
            # 각 바에 따른 왼쪽 기준 라인 설정
            Line(Point(0, y), Point(10, y)).draw(win)
            Text(Point(-10, y), str(wordCnt[i][1])).draw(win)

    # 윈도우창에 입력이 들어왔으면 종료
    while True:
        if win.checkKey() == "Return":
            break

    win.close()
        




def main():
    # 파일 불러오기
    while True:
        try:
            fName = input("파일명을 입력해주세요 < .txt 제외 >")
            file = open(fName+'.txt', 'r')
            # spilit으로 단어 나누기
            text = file.read().lower().split()

        # 파일이 존재하지 않는 오류가 발생하면
        except FileNotFoundError:
            print("파일이 존재하지 않습니다")
            if isExcept(): continue

        # 예상치 못한 오류가 발생하면
        except Exception as e:
            print("다음과 같은 오류가 발생했습니다", e)
            if isExcept(): continue

        # 어떠한 오류도 발생하지 않았을 경우 무한루프 종료
        else: break
        
    wList = {}
    
    # 딕셔너리 형태로 문자 등장횟수 정리
    for i in text:
        wList[i] = text.count(i)

    # 딕셔너리를 이름순으로 정렬 후 등장빈도 순으로 정렬
    wList = sorted(wList.items(), key = lambda x: x[0])
    wList = sorted(wList, key = lambda x: x[1], reverse = True)

    # 그래프창 그리기
    drawWin(sorted(wList[:8], key = lambda x: x[0]))
    file.close()

main()
