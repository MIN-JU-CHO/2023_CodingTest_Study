#include<stdio.h>
#include<set>
#include<map>
#include<vector>

using namespace std;

int main(void)
{
    int N;
    scanf("%d", &N);
    vector<int>arr(N);
    set<int> dic;
    map<int, int> order;
    for(int i=0; i<N; ++i)
    {
        scanf("%d",&arr[i]);
        dic.insert(arr[i]);
    }
    int i=0;
    for(int temp:dic)
    {
        order[temp] = i++;
    }
    for(int elem:arr)
    {
        printf("%d ", order[elem]);
    }
}