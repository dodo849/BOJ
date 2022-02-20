#include <iostream>
//#include <cstring>
#include <vector>
//#include <cstdio>
//#include <algorithm>
//#include <queue>

using namespace std;

int cnt = 0;

typedef struct _Node{
    int value;
    _Node* left;
    _Node* right;
    _Node* parent;
} Node;

Node* createNode(){
    Node* n = (Node*)malloc(sizeof(Node));
    n->value = -1;
    n->left = NULL;
    n->right = NULL;
    n->parent = NULL;

    return n;
}

Node* findNode(Node* n, int target){
    
    if(n->value == target)
        return n;

    Node* nextLeftNode = NULL;
    Node* nextRightNode = NULL;
    
    if(n->left != NULL){
        nextLeftNode = findNode(n->left, target);
        if (nextLeftNode != NULL){
            if(nextLeftNode->value == target)
                return nextLeftNode;
                
            }
    }

    if(n->right != NULL){
        nextRightNode = findNode(n->right, target);
        if (nextRightNode != NULL){
            if(nextRightNode->value == target)
                return nextRightNode;
        }
    }
    
    return NULL;
}

void countLeaf(Node* n){
    if(n->left==NULL && n->right==NULL)
        cnt++;
    if(n->left != NULL)
        countLeaf(n->left);
    if(n->right != NULL)
        countLeaf(n->right);
    return;
}

int main() {ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);

    /*-----입력-트리구성-----*/
    int N;
    scanf("%d", &N);
    
    if(N == 0){
        cout << 0;
        return 0;
    }

    Node* root = createNode();

    for(int i=0; i<N; i++){
        int temp;
        scanf("%d", &temp);
        
        if(temp == -1){
            root->value = i;
        }
        else{
            Node* parent = findNode(root, temp);
            Node* n = createNode();
            n->value = i;

            if(parent != NULL){
                if(!parent->left)
                    parent->left = n;
                else if(!parent->right)
                    parent->right = n;
                else{
                    // none
                }
                n->parent = parent;
            }
            }
    }

    int M;
    scanf("%d", &M);

    /*-----풀이-노드 삭제-----*/
    // 삭제할 노드의 부모를 찾는다
    if(M == 0){ //만약 삭제노드가 root이면 0을 출력
        cout << 0;
    }
    else{
        // 부모를 찾아 해당 노드의 연결을 지운다.
        Node* removeNode = findNode(root, M);
        Node* parentOfRemove = removeNode->parent;
        if(parentOfRemove->left->value == M)
            parentOfRemove->left = NULL;
        else
            parentOfRemove->right = NULL;
        

        //리프노드의 개수를 세는 함수
        countLeaf(root);
        cout << cnt;
    }

    return 0;
}
