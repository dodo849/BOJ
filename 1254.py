import sys

#-----함수-----#
def Palindrome(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

#-----입력-----#
s = sys.stdin.readline().strip()

flag = False

#-----풀이-----#
for i in range(len(s)):
    #문자열을 끊어서 검사
    flag = Palindrome(s[i:])

    #처음 True인 경우가 최대 펠린드롬 길이
    if flag == True:
        print(len(s) + i)
        break