#include<iostream>

using namespace std;

int N;
int result = 0;
int queen[15];
bool visited[15];

// [1 ~ pos - 1] check up/down/diagonal
bool check(int pos)
{
	for (int i = 1; i < pos; ++i)
	{
		if (queen[pos] == queen[i]
			|| abs(pos - i) == abs(queen[pos] - queen[i]))
		{
			return false;
		}
	}
	return true;
}

void nqueen(int depth)
{
	// satisfied case
	if (depth == N + 1)
	{
		++result;
		return;
	}
	// locate queen pos
	for (int i = 1; i < N + 1; ++i)
	{
		// skip visited
		if (visited[i])
		{
			continue;
		}
		// back-tracking
		queen[depth] = i;
		visited[i] = true;
		if (check(depth))
		{
			nqueen(depth + 1);
		}
		visited[i] = false;
	}
}

int main(void)
{
	cin >> N;
	nqueen(1);
	cout << result;
}