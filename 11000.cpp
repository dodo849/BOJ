#include <iostream>
//#include <cstring>
#include <vector>
//#include <cstdio>
//#include <algorithm>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

#define MAX 200000

struct compare{
    bool operator()(pair<int, int>a, pair<int, int>b){
        return a.first>b.first;
    }
};

int main(){ ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
    int N;
    cin >> N;
    
    // 강의시간 저장 & 오름차순 정렬
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> time;
    //끝나는 시간도 오름차순 정렬
    priority_queue<int, vector<int>, greater<int>> room;

    for(int i=0; i<N; i++){
        int start, end;
        cin >> start >> end;
        time.push(make_pair(start, end));
    }
    
    int curStart = time.top().first;
    int curEnd = time.top().second;
    time.pop();
    room.push(curEnd);
    for(int i=0; i<N-1; i++){
        curStart = time.top().first;
        curEnd = time.top().second;
        time.pop();
        room.push(curEnd);
        //만약 이어서 수업이 가능하다면 대체
        if(curStart >= room.top())
            room.pop();
    }
    
    cout << room.size() << endl;
    
    return 0;
}
