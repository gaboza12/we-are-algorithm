#include <bits/stdc++.h>

using namespace std;

int R, C;

//좌표 + 플레이어 현재 진행도
struct Info
{
	int x, y, c;
};

queue<pair<int, int>> fq;
queue<Info> aq;

int ax[4] = { 0, 0, 1, -1 };
int ay[4] = { -1, 1, 0, 0 };

char board[1001][1001];
bool check[1001][1001];

int fire[1001][1001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> R >> C;

	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			char c;
			cin >> c;

			board[i][j] = c;

			if (c == 'F')
			{
				fq.push({ j, i }); // x, y
				fire[i][j] = 0;
			}
			else if (c == 'J')
			{
				aq.push({ j,i,0 });
				check[i][j] = true;
				fire[i][j] = 5000;
			}
			else
			{
				fire[i][j] = 5000;
			}
		}
	}

	//불보드 만들기
	while (!fq.empty())
	{
		pair<int, int> cor = fq.front();
		fq.pop();

		for (int i = 0; i < 4; ++i)
		{
			int dx = ax[i] + cor.first;
			int dy = ay[i] + cor.second;

			if (dx < 0 || dy < 0 || dx >= C || dy >= R)
			{
				continue;
			}

			if (board[dy][dx] == '#')
			{
				continue;
			}

			//작은값 부여
			if (fire[cor.second][cor.first] + 1 < fire[dy][dx])
			{
				fire[dy][dx] = fire[cor.second][cor.first] + 1;
				fq.push({ dx, dy });
			}
		}
	}

	int ans = -1;
	//불보드의 값보다 큰 값으로 이동(그냥 전체 이동하면서 출구까지 연결되면 ok)
	while (!aq.empty())
	{
		Info cor = aq.front();
		aq.pop();
		int x = cor.x;
		int y = cor.y;

		//출구 도착
		if (x <= 0 || y <= 0 || x >= C - 1 || y >= R - 1)
		{
			ans = cor.c + 1;
			break;
		}

		for (int i = 0; i < 4; ++i)
		{
			int dx = ax[i] + x;
			int dy = ay[i] + y;

			if (dx < 0 || dy < 0 || dx >= C || dy >= R)
			{
				continue;
			}

			if (board[dy][dx] == '#' || check[dy][dx])
			{
				continue;
			}

			//볼보드 값보다 현재 플레이어의 진행값이 작아야만함
			if (cor.c + 1 < fire[dy][dx])
			{
				check[dy][dx] = true;
				aq.push({ dx, dy, cor.c + 1 });
			}
		}
	}

	if (ans == -1)
	{
		cout << "IMPOSSIBLE";
	}
	else
	{
		cout << ans;
	}

	return 0;
}