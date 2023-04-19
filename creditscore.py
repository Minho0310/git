credit_sum=0
creditxscoresum=0

while True:
    credit = int(input('학점을 입력해주세요(입력을 종료하고싶다면 0을 입력해주세요):'))
    if credit == 0:
        break
    score_e = input('평점을 입력해주세요:')
    match score_e:
        case 'A+':
            score=4.5
        case 'A':
            score=4.0
        case 'B+':
            score=3.5
        case 'B':
            score=3.0
        case 'C+':
            score=2.5
        case 'C':
            score=2.0
        case 'D+':
            score=1.5
        case 'D':
            score=1.0
        case 'F':
            score=0.0

    creditxscoresum += credit*score
    credit_sum += credit
    print(f"학점은{credit}입니다")
    print(f"평점은{score_e}입니다")
gpa=creditxscoresum / credit_sum
print(f"열람용:{credit_sum}학점,GPA:{gpa}")
print("!!!")



