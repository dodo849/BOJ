#include <iostream>
//#include <cstring>
//#include <vector>
//#include <cstdio>
//#include <algorithm>
#include <queue>
//#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

using namespace std;

int main(){ ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
    
    int N;
    cin >> N;
    
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            int temp;
            cin >> temp;
            pq.push(temp);
            if(pq.size() > N)
                pq.pop();
            }
        }

    cout << pq.top();

    return 0;
}
