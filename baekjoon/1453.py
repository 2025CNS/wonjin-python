n = int(input())
seat = list(map(int, input().split()))
seating_num = set(seat)

print(len(seat) - len(seating_num))