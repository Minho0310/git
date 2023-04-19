credit_sum=0
creditxscoresum=0
while True:
    credit = int(input('학점을 입력해주세요(입력을 종료하고싶다면 0을 입력해주세요):'))
    if credit == 0:
        break
    score = float(input('평점을 입력해주세요:'))
    creditxscoresum += credit*score
    credit_sum += credit
    print(f"학점은{credit}입니다")
    print(f"평점은{score}입니다")
gpa=creditxscoresum / credit_sum
print(f"gpa는{gpa}입니다")



