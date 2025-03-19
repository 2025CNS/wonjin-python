s = input()  # YYMMDD 형식으로 입력받기
yy = s[:2]   # 연도 (앞 두 자리)
mm = s[2:4]  # 월 (중간 두 자리)
dd = s[4:6]  # 일 (마지막 두 자리)

print(yy, mm, dd)  # 공백으로 구분하여 출력