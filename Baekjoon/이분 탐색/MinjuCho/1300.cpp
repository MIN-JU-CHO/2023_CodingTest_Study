#include <iostream>
#include <algorithm>

using namespace std;
int main(void)
{
	long long N, k;
	cin >> N >> k;
	long long start = 1, end = k, finding = end;
	while (start <= end)
	{
		long long mid = (start + end) / 2;
		long long cnt = 0;
		for (long long i = 1; i <= N; ++i)
		{
			cnt += min(mid / i, N);
		}
		if (cnt < k)
		{
			start = mid + 1;
		}
		else
		{
			finding = mid;
			end = mid - 1;
		}
	}
	cout << finding;
}