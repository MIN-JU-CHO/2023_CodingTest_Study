#include<iostream>

using namespace std;

int N, M;
int arr[9];
bool visited[10];

void subsequence(int pos)
{
	if (pos == M + 1)
	{
		for (int i = 1; i < M + 1; ++i)
		{
			cout << arr[i] << " ";
		}
		// endl : timeout
		cout << "\n";
		return;
	}
	for (int i = 1; i < N + 1; ++i)
	{
		if (visited[i] == false)
		{
			arr[pos] = i;
			visited[i] = true;
			subsequence(pos + 1);
			visited[i] = false;
		}
	}
}

int main(void)
{
	cin >> N;
	cin >> M;
	subsequence(1);
}