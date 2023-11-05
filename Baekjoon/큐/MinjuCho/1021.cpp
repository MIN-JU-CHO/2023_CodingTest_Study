#include<iostream>
#include<deque>
#include<vector>
#include<algorithm>

using namespace std;
int main(void)
{
	int N, M;
	cin >> N >> M;
	deque<int> que(N);
	for (int i = 0; i < N; ++i)
	{
		que[i] = i + 1;
	}
	vector<int> idx(M);
	for (int i = 0; i < M; ++i)
	{
		cin >> idx[i];
	}
	int cnt = 0;
	for (int index : idx)
	{
		while (find(que.begin(), que.end(), index) != que.end())
		{
			if (que.front() == index)
			{
				que.pop_front();
				
				break;
			}
			else if (find(que.begin(), que.end(), index) - que.begin() <= (que.size() / 2))
			{
				que.push_back(que.front());
				que.pop_front();
				++cnt;
			}
			else
			{
				que.push_front(que.back());
				que.pop_back();
				++cnt;
			}
		}
	}
	cout << cnt;
}