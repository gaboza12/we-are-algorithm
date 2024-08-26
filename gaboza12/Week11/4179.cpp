#include <bits/stdc++.h>

using namespace std;

char board[1005][1005];
int r, c;

int dist1[1005][1005];
int dist2[1005][1005];

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> r >> c;

	queue<pair<int, int>> q1, q2;

	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			dist1[i][j] = -1;
			dist2[i][j] = -1;
		}
	}

	for (int i = 0; i < r; i++)
	{
		string s;
		cin >> s;

		for (int j = 0; j < s.size(); j++)
		{
			board[i][j] = s[j];
			if (s[j] == 'J')
			{
				q1.push({ i, j });
				dist1[i][j] = 0;
			}
			else if (s[j] == 'F')
			{
				q2.push({ i, j });
				dist2[i][j] = 0;
			}
		}
	}

	//불
	while (!q2.empty())
	{
		pair<int, int> cur = q2.front();
		q2.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (nx < 0 || nx >= r || ny < 0 || ny >= c)
				continue;

			if (dist2[nx][ny] >= 0 || board[nx][ny] == '#')
				continue;

			dist2[nx][ny] = dist2[cur.first][cur.second] + 1;
			q2.push({ nx, ny });
		}
	}

	//지훈
	while (!q1.empty())
	{
		pair<int, int> cur = q1.front();
		q1.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];
	
			//탈출
			if (nx < 0 || nx >= r || ny < 0 || ny >= c)
			{
				cout << dist1[cur.first][cur.second] + 1;
				return 0;
			}

			if (dist1[nx][ny] >= 0 || board[nx][ny] == '#')
				continue;

			if (dist2[nx][ny] <= dist1[cur.first][cur.second] + 1 && dist2[nx][ny] != -1)
				continue;

			dist1[nx][ny] = dist1[cur.first][cur.second] + 1;
			q1.push({ nx, ny });
		}
	}

	cout << "IMPOSSIBLE";

	return 0;
}