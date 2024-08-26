#include <bits/stdc++.h>

using namespace std;

int board[50][5];

int r1, c1, r2, c2;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };

void make_board()
{
	int num = 1, offset = 0, cnt = 0;
	int x = 0, y = 0;

	while (1)
	{
		if (-offset <= x && x <= offset && -offset <= y && y <= offset)
		{
			if (r1 <= x && x <= r2 && c1 <= y && y <= c2)
			{
				board[x - r1][y - c1] = num;
				cnt++;

				if (cnt == (r2 - r1 + 1) * (c2 - c1 + 1))
					return;
			}
			
			num++;
		}

		for (int i = 0; i < 4;)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (-offset <= nx && nx <= offset && -offset <= ny && ny <= offset)
			{
				if (r1 <= nx && nx <= r2 && c1 <= ny && ny <= c2)
				{
					board[nx - r1][ny - c1] = num;
					cnt++;

					if (cnt == (r2 - r1 + 1) * (c2 - c1 + 1))
						return;
				}

				x = nx;
				y = ny;
				num++;
			}
			else
				i++;
		}

		offset++;
		y++;
	}
}

int findNum()
{
	int mx = -1;

	for (int i = 0; i <= r2 - r1; i++)
	{
		for (int j = 0; j <= c2 - c1; j++)
		{
			mx = max(mx, board[i][j]);
		}
	}

	return to_string(mx).size();
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> r1 >> c1 >> r2 >> c2;

	make_board();

	int num = findNum();

	for (int i = 0; i <= r2 - r1; i++)
	{
		for (int j = 0; j <= c2 - c1; j++)
		{
			int sz = to_string(board[i][j]).size();

			for (int k = 0; k < num - sz; k++)
			{
				cout << " ";
			}
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}