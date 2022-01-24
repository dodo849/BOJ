#include <iostream>
//#include <cstring>
#include <vector>
//#include <cstdio>
//#include <algorithm>
//#include <queue>
#include <stdio.h>

using namespace std;

//최소힙에 원소를 추가
void push(vector<int> &v, int item, int idx){
    v[idx] = item;
    
    //부모의 값이 자식값보다 작아질 때까지 swap한다.
    int parentIdx = idx/2;
    
    while( (idx != parentIdx) && (v[parentIdx] > item) ){

        int temp = v[parentIdx];
        v[parentIdx] = item;
        v[idx] = temp;
        
        idx = parentIdx;
        parentIdx = idx/2;
    }
}

//최소힙에서 원소를 삭제
int pop(vector<int> &v, int idx){
    
    int min = v[1];
    
    //루트노드를 힙의 마지막 노드로 바꾼다.
    v[1] = v[idx];
    int curIdx = 1;
    
    
    //자식 중 작은 값의 인덱스를 고른다.
    int childIdx = v[curIdx*2] < v[curIdx*2+1] ? curIdx*2 : curIdx*2+1;
    
    //자식 노드값이 현재 노드보다 작을 때 까지 swap 해준다.
    while( (v[curIdx] > v[childIdx]) && (childIdx < idx) ){
        
        int temp = v[curIdx];
        v[curIdx] = v[childIdx];
        v[childIdx] = temp;
        
        curIdx = childIdx;
        childIdx = v[curIdx*2] < v[curIdx*2+1] ? curIdx*2 : curIdx*2+1;
    }
    
    return min;
}

int main(){

    //입력
    int N;
//    cin >> N;
    scanf("%d", &N);
    
    vector<int> v(N+1);
    
    //인덱스 계산을 위해, root 노드의 인덱스는 1
    int idx = 1;
    
    for(int i=0; i<N; i++){
        int temp;
        scanf("%d", &temp);
//        cin >> temp;
        
        if(temp == 0){      //입력이 0일 경우 힙에 pop 실행
            if(idx == 1)    //배열이 빈 경우엔 0 출력
                printf("0\n");
//                cout << 0 << endl;
            else{           //배열이 비어있지 않으면 pop 실행
                idx--;
                printf("%d\n", pop(/*배열*/ v, /*마지막 원소 인덱스*/ idx));
//                cout << pop(/*배열*/ v, /*마지막 원소 인덱스*/ idx) << endl;
            }
        }
        else{               //입력이 자연수일 경우 힙에 push 실행
            push(/*배열*/ v, /*추가할 값*/ temp, /*마지막 원소의 인덱스*/ idx);
            idx++;
        }
    }
    return 0;
}
