#include <iostream>
#include <map>

using namespace std;

int N;
int score[21][21];
int result = 99999999;
bool team[21];

void makeTeam(int depth, int idx)
{
	if (depth == N / 2 + 1)
	{
		for (int i=1; i<=N; ++i)
		{
			cout << i << " : " << team[i] << '\t';
		}
		cout << endl;
		int link = 0, start = 0;
		for (int i=1; i<=N; ++i)
		{
			for (int j=1; j<=N; ++j)
			{
				if (i == j)
				{
					continue;
				}
				if (team[i] == 0 && team[j] == 0)
				{
					link += score[i][j];
				}
				else if (team[i] == 1 && team[j] == 1)
				{
					start += score[i][j];
				}
			}
		}
		result = min(result, abs(link - start));
		return;
	}
	for (int i = idx; i <= N; ++i)
	{
		team[i] = true;
		makeTeam(depth + 1, i + 1);
		team[i] = false;
	}
}

int main(void)
{
	cin >> N;
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			cin >> score[i][j];
		}
	}
	makeTeam(1, 1);
	cout << result;
}