#include <iostream>
//#include <cstring>
//#include <vector>
//#include <cstdio>
//#include <algorithm>
#include <queue>
#include <stdio.h>
#include <cstdlib>

using namespace std;

#define MAX 50
int N, M, result=MAX;
int arr[MAX][MAX];
queue< pair<int,int> > q;
int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int bfs(int x, int y){
    
    int visited[MAX][MAX];

    q.push(make_pair(x, y));
    
    while (!q.empty()){
        
        int cx=q.front().first, cy=q.front().second;
        q.pop();
        visited[cx][cy] = 1;
        
        //안전거리 구하는 로직이 완전 틀림
        if(arr[cx][cy] == 1){
            int min;
            if(abs(cx-x) > abs(cy-y))
                min = abs(cy-y);
            else
                min = abs(cx-x);
            return min;
        }
           
        for(int i=0; i<8; i++){
            int nx=cx+dx[i], ny=cy+dy[i];
            if(nx>=0 && nx<N && ny>=0 && ny<M)
                if(visited[nx][ny]==0)
                    q.push(make_pair(nx, ny));
        }
    }
    return MAX;
}

int main(){ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
    
    //--- 입력 ---//
    cin >> N >> M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            int temp;
            cin >> temp;
            arr[i][j] = temp;
        }
    }
    
    //--- 풀이 ---//
    for(int i=0; i<N; i++){
        for(int j=0; i<M; j++){
            int temp = bfs(i, j);
            if (result < temp)
                result = temp;
        }
    }
    
    cout << result;

    return 0;
}


