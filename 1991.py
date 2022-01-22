import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
arr = dict()
answer = ['', '', '']
for _ in range(N):
    temp = sys.stdin.readline().split()
    arr[temp[0]] = [temp[1], temp[2]]

#왼쪽 오른쪽 자식, 형제 check
def preorder(char):
    if char != ".":
        answer[0] += char
        preorder(arr[char][0]) #왼쪽
        preorder(arr[char][1]) #오른쪽

def inorder(char):
    if char != ".":
        inorder(arr[char][0]) #왼쪽
        answer[1] += char
        inorder(arr[char][1]) #오른쪽

def postorder(char):
    if char != ".":
        postorder(arr[char][0])  # 왼쪽
        postorder(arr[char][1]) #오른쪽
        answer[2] += char

preorder('A')
inorder('A')
postorder('A')
for a in answer:
    print(a)
