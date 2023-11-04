#include<stdio.h>

using namespace std;
int main(void)
{
	long long T;
	scanf_s("%lld", &T);
	int dp[12];
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 11; ++i)
	{
		dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
	}
	while (T--)
	{
		int n;
		scanf_s("%d", &n);
		printf("%d\n", dp[n]);
	}
}