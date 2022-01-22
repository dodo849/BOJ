import random

print("학번 이름 : 2020010849 이도연")

s = 0
n = 7 #반복 횟수

print("난수 : " , end = "")
for i in range(n):
    r = random.randint(10, 70)
    print(r, end=" ")
    s = s + r
print()
print("합: %d 평균: %.2f"%(s, s/n))