#include <stdio.h>
#include <vector>
#include<algorithm>

using namespace std;
int main(void)
{
    long long K, N;
    scanf("%lld",&K);
    scanf("%lld", &N);
    vector<long long> cable(K);
    for(long long i=0; i<K; ++i)
    {
        scanf("%lld",&cable[i]);
    }

    long long result=1;
    long long start=1, end=*max_element(cable.begin(), cable.end());
    while(start<=end)
    {
        long long mid = (start+end)/2;
        long long cnt = 0;
        for(long long elem:cable)
        {
            cnt+=elem/mid;
        }
        if(cnt < N)
        {
            end = mid-1;
        }
        else
        {
            result = mid;
            start = mid+1;
        }
    }
    printf("%lld", result);
}