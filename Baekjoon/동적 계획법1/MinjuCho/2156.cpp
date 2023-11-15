#include<stdio.h>
#include<vector>
#include<algorithm>
#include<numeric>

using namespace std;
int main(void)
{
	int n;
	scanf_s("%d", &n);
	vector<long long> glass(n);
	for (int i = 0; i < n; ++i)
	{
		scanf_s("%lld", &glass[i]);
	}
	if (n <= 2)
	{
		printf("%d", accumulate(glass.begin(), glass.end(), 0));
		return 0;
	}
	vector<long long> dp(n, 0);
	dp[0] = glass[0];
	dp[1] = glass[0] + glass[1];
	dp[2] = max({ glass[0] + glass[2], glass[1] + glass[2], dp[1] });
	for (int i = 3; i < n; ++i)
	{
		dp[i] = max({ dp[i - 3] + glass[i - 1] + glass[i], dp[i - 2] + glass[i], dp[i - 1]});
	}
	printf("%lld", *max_element(dp.begin(), dp.end()));
}