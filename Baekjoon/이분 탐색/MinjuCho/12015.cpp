#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;
int main(void)
{
    int N;
    scanf("%d", &N);
    vector<int> A;
    for(int i=0; i<N; ++i)
    {
        int temp;
        scanf("%d", &temp);
        if(A.empty() || A.back()<temp)
        {
            A.push_back(temp);
        }
        else
        {
            *lower_bound(A.begin(), A.end(), temp) = temp;
        }
    }

    printf("%ld", A.size());
}