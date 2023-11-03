#include<iostream>

using namespace std;
int main(void)
{
	int N, result = 0;
	cin >> N;
	while (N >= 0)
	{
		if (N % 5 == 0)
		{
			result += N / 5;
			break;
		}
		N -= 3;
		++result;
	}
	if (N < 0)
	{
		result = -1;
	}
	cout << result;
}