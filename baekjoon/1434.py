n, m = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

box = 0  # 지금 보고 있는 상자 번호

for book in books:
    while book > boxes[box]:  # 안 들어가면 다음 상자
        box += 1
    boxes[box] -= book  # 넣기 성공하면 공간 줄이기

print(sum(boxes))  # 남은 공간 다 더해서 출력