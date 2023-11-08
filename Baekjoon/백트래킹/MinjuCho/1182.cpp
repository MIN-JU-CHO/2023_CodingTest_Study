#include<iostream>

using namespace std;
int arr[21];
int N, S;
int result = 0;

void makesub(int depth, int total)
{
	if (depth == N + 1)
	{
		if (total == S)
		{
			++result;
		}
		return;
	}
	makesub(depth + 1, total);
	makesub(depth + 1, total + arr[depth]);
}

int main(void)
{
	cin >> N >> S;
	for (int i = 1; i <= N; ++i)
	{
		cin >> arr[i];
	}
	makesub(1, 0);
	// except empty set
	if (S == 0)
	{
		--result;
	}
	cout << result;
}