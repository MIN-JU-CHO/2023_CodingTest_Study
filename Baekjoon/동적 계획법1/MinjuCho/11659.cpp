#include<stdio.h>
#include<vector>

using namespace std;
int main(void)
{
	int N, M, i, j;
	scanf_s("%d %d", &N, &M);

	vector<int> arr(N + 1);
	vector<int> dp(N + 1, 0);
	for (int k = 1; k < N + 1; ++k)
	{
		scanf_s("%d", &arr[k]);
		dp[k] = dp[k - 1] + arr[k];
	}

	while (M--)
	{
		scanf_s("%d %d", &i, &j);
		printf("%d\n", dp[j] - dp[i - 1]);
	}
}