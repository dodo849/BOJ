#2020010849 이도연
i = 0
sum = 0
print("홀수:", end=" ")
while(i < 21):
    if(i % 2 != 0):
        print(i, end=" ")
        sum = sum + i
    i = i + 1
print()
print("홀수의 합:", sum)