// 문제 풀이 링크: https://velog.io/@cuppizza/백준-12015-가장-긴-증가하는-부분-수열-2-C-파이썬
// 실행 시간: 232ms 메모리: 7384KB
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