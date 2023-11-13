#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main(void)
{
    long long N, M;
    scanf("%lld %lld", &N, &M);
    vector<long long> trees(N);
    while(N)
    {
        scanf("%lld", &trees[--N]);
    }

    long long start = 1, mid;
    long long end = *max_element(trees.begin(), trees.end());
    long long result = 0;
    while(start<=end)
    {
        mid = (start+end) / 2;
        long long count=0;
        for(long long wood : trees)
        {
            if(wood>mid)
            {
                count += wood-mid;
            }
            
        }
        if(count>=M)
        {
            result = max(result, mid);
            start = mid+1;
        }
        else
        {
            end = mid-1;
        }
    }
    printf("%lld", result);
}