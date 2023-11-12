#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;
int main(void)
{
	int N, M;
	scanf_s("%d", &N);
	vector<int> arr(N);
	for (int i = 0; i < N; ++i)
	{
		scanf_s("%d", &arr[i]);
	}
	sort(arr.begin(), arr.end());
	scanf_s("%d", &M);
	vector<int> output(M);
	for (int i = 0; i < M; ++i)
	{
		int input;
		scanf_s("%d", &input);
		auto iter = lower_bound(arr.begin(), arr.end(), input);
		if ( iter!= arr.end() && *iter == input )
		{
			output[i] = 1;
		}
		else
		{
			output[i] = 0;
		}
	}
	for (int i = 0; i < M; ++i)
	{
		printf("%d\n", output[i]);
	}
}