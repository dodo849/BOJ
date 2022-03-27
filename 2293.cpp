//
//  main.cpp
//  BOJ
//
//  Created by DOYEONLEE2 on 2022/03/27.
//

// 📄 솔루션 O

#include <iostream>
#include <algorithm>

using namespace std;

int dp[10000+1] = {0};
int value[100+1] = {0};
int n, k;

int main(int argc, const char * argv[]) {
    
    // ✅ 입력
    cin >> n >> k;
    
    for(int i = 1; i < n+1; i++){
        int temp;
        cin >> temp;
        value[i] = temp;
    }
    
    // ✅ 풀이
    dp[0] = 1;
    for(int i = 1; i < n+1; i++){
        int coin = value[i];
        for(int j = coin; j < k+1; j++){
            dp[j] = dp[j] + dp[j - coin];
        }
        
    }
    
    // ✅ 결과출력
        cout << dp[k];
    
    
    return 0;
}


