#include <bits/stdc++.h>

using namespace std;

int N, M, K, t;

//단순반복으로 불가능

//queue이용해서 중복인경우 1로해주는 방식 -> 9만회 언저리
//최종검사 최대 9만회

bool check1[301][301]; // 90kb
bool check2[301][301]; // 90kb

int ax[8] = { -1, -1, 1, 1, -2, -2, 2, 2 };
int ay[8] = { -2, 2, -2, 2, -1, 1, 1, -1 };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M >> K >> t;

	queue<pair<int, int>> q1;
	queue<pair<int, int>> q2;
	for (int i = 0; i < M; ++i)
	{
		int x, y;
		cin >> x >> y;
		q1.emplace(y, x);
	}

	for (int i = 0; i < t; ++i)
	{
		queue<pair<int, int>>& tq = i % 2 == 0 ? q1 : q2;
		queue<pair<int, int>>& ttq = i % 2 == 0 ? q2 : q1;
		bool(&tcheck)[301][301] = (i % 2 == 0) ? check2 : check1;
		while (!tq.empty())
		{
			pair<int, int> f = tq.front();
			tq.pop();
			
			for (int j = 0; j < 8; ++j)
			{
				int x = f.second + ax[j];
				int y = f.first + ay[j];

				if (x <= 0 || x > N || y <= 0 || y > N)
				{
					continue;
				}
				if (tcheck[y][x])
				{
					continue;
				}

				tcheck[y][x] = true;
				ttq.emplace(y, x);
			}
		}
	}

	bool(&anscheck)[301][301] = (t % 2 == 0) ? check1 : check2;
	string clean = "NO";
	for (int i = 0; i < K; ++i)
	{
		int x, y;
		cin >> x >> y;
		if (anscheck[y][x])
		{
			clean = "YES";
			break;
		}
	}

	cout << clean;

	return 0;
}