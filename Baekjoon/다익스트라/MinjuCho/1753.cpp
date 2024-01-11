#include <vector>
#include <queue>
#include <iostream>

#define weight first
#define vertex second
using namespace std;

int V, E, st;
const int INF = 0x3f3f3f3f;
vector<pair<int, int>> adj[200001];
int d[200001];

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> V >> E >> st;
	while (E--)
	{
		int u, v, w;
		cin >> u >> v >> w;
		adj[u].push_back({ w, v });
	}

	// 첫 노드 0, 나머지 INF
	fill(d, d + V + 1, INF);
	d[st] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, st });
	while (!pq.empty())
	{
		pair<int, int> cur = pq.top();
		pq.pop();
		// 이미 최단거리 존재 시 skip
		if (cur.weight != d[cur.vertex])
		{
			continue;
		}
		for (pair<int, int> next : adj[cur.vertex])
		{
			// 이미 최단거리 일 때
			if (d[next.vertex] <= d[cur.vertex] + next.weight)
			{
				continue;
			}
			d[next.vertex] = d[cur.vertex] + next.weight;
			pq.push({ d[next.vertex], next.vertex });
		}
	}

	for (int i = 1; i <= V; ++i)
	{
		if (d[i] == INF)
		{
			cout << "INF" << endl;
			continue;
		}
		cout << d[i] << endl;
	}
}