#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n, x;
    scanf("%d", &n);
    
    priority_queue<int> pq;
    
    for (int i = 0; i < n; i++){
        scanf("%d", &x);
        if((x == 0 ) && pq.empty())
            printf("0\n");
        else if(x == 0){
            printf("%d\n", pq.top());
            pq.pop();
        }
        else
            pq.push(x);
    }

    return 0;
}
