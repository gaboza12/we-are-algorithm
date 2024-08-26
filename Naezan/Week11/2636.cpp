#include <bits/stdc++.h>

using namespace std;

int N, M;

int board[101][101];
bool check[101][101];

int ax[4] = { 0, 0, -1, 1 };
int ay[4] = { 1, -1, 0, 0 };

int daytime = 0;
int last[101];

bool bComplete = false;

void calc(int x, int y)
{
	queue<pair<int, int>> ansq;

	queue<pair<int, int>> q;
	q.push({ x, y });
	check[y][x] = true;

	while (!q.empty())
	{
		pair<int, int> c = q.front();
		q.pop();

		for (int i = 0; i < 4; ++i)
		{
			int dx = ax[i] + c.first;
			int dy = ay[i] + c.second;

			if (dx < 0 || dy < 0 || dx >= N || dy >= M)
			{
				continue;
			}

			if (check[dy][dx])
			{
				continue;
			}

			//치즈가 있다면 치즈 정보 등록
			if (board[dy][dx])
			{
				ansq.push({ dx, dy });
			}
			else
			{
				q.push({dx, dy});
			}

			check[dy][dx] = true;
		}
	}

	//삭제될 치즈갯수
	int deleted = ansq.size();

	while (!ansq.empty())
	{
		pair<int, int> c = ansq.front();
		ansq.pop();

		board[c.second][c.first] = false;
	}

	memset(check, false, sizeof(check));

	++daytime;
	last[daytime] = last[daytime - 1] - deleted;

	if (last[daytime] == 0)
	{
		bComplete = true;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> M >> N;

	int initialc = 0;
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			cin >> board[i][j];
			if (board[i][j] == true)
			{
				++initialc;
			}
		}
	}

	last[daytime] = initialc;

	while (!bComplete)
	{
		calc(0, 0);
	}

	cout << daytime << '\n';
	cout << last[daytime - 1] << '\n';

	return 0;
}