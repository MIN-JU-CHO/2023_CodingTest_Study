#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;
int main(void)
{
	int N;
	scanf_s("%d", &N);
	vector<long long>R(N), G(N), B(N);
	for (int i = 0; i < N; ++i)
	{
		scanf_s("%lld", &R[i]);
		scanf_s("%lld", &G[i]);
		scanf_s("%lld", &B[i]);
	}
	vector<vector<long long>> dp(N, vector<long long>(3));
	dp[0][0] = R[0];
	dp[0][1] = G[0];
	dp[0][2] = B[0];
	for (int i = 1; i < N; ++i)
	{
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R[i];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G[i];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B[i];
	}
	printf("%lld", min(dp[N - 1][0], min(dp[N - 1][1], dp[N - 1][2])));
}