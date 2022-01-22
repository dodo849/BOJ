def add1(x, y):
    sum = x+y
    return sum

def add2(idx1, idx2):
    arr.append(arr[idx1] + arr[idx2])

x = int(input("정수를 입력하세요: "))
y = int(input("정수를 하나더 입력하세요: "))

result = add1(x, y)
print("add1의 결과는 %d입니다." % result)

arr= []
arr.extend([x, y])
add2(0, 1)
print("add2의 결과는 %d입니다." % (arr[2]))