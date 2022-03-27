//
//  main.cpp
//  BOJ
//
//  Created by DOYEONLEE2 on 2022/03/27.
//

#include <iostream>
#include <algorithm>

using namespace std;

int stairs[300+1] = {0};
int dp[300+1] = {0};

int main(int argc, const char * argv[]) {
    
    // ✅ 입력
    int N;
    cin >> N;
    
    for(int i = 1; i < N+1; i++){
        int temp;
        cin >> temp;
        stairs[i] = temp;
    }
    
    // ✅ 풀이
    dp[1] = stairs[1];
    dp[2] = stairs[1] + stairs[2];
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]);
    //i를 선택할지 말지
    for(int i = 4; i < N; i++){
        dp[i] = stairs[i] + max(dp[i-2], stairs[i-1] + dp[i-3]);
    }
    
    //마지막 계단은 반드시 밟아야 한다.
    if(dp[N-2] > stairs[N-1] + dp[N-3]){
        cout << stairs[N] + dp[N-2];
    }
    else{
        cout << stairs[N] + stairs[N-1] + dp[N-3];
    }
    
    
    return 0;
}
