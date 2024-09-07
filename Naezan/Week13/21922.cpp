#include <bits/stdc++.h>

using namespace std;

int N, M;

enum Dir
{
	L, R, U, D
};

int ax[4] = { -1, 1, 0, 0 };//left, right, up, down
int ay[4] = { 0, 0, -1, 1 };

std::vector<std::vector<int>> vec;
std::vector<std::vector<bool>> check;
queue<pair<int, int>> q;

void calc(int x, int y, Dir dir)
{
	if (x < 0 || y < 0 || x >= M || y >= N)
	{
		return;
	}

	check[y][x] = true;
	int val = vec[y][x];

	if (val == 9)
	{
		return;
	}

	if (val == 1)
	{
		if (dir == L || dir == R)
		{
			return;
		}
	}
	else if (val == 2)
	{
		if (dir == U || dir == D)
		{
			return;
		}
	}
	//3이나 4를 만나면 방향 변경
	else if (val == 3)
	{
		switch (dir)
		{
		case L:
			dir = D;
			break;
		case R:
			dir = U;
			break;
		case U:
			dir = R;
			break;
		case D:
			dir = L;
			break;
		}
	}
	else if (val == 4)
	{
		switch (dir)
		{
		case L:
			dir = U;
			break;
		case R:
			dir = D;
			break;
		case U:
			dir = L;
			break;
		case D:
			dir = R;
			break;
		}
	}

	int dx = x + ax[dir];
	int dy = y + ay[dir];

	calc(dx, dy, dir);
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	vec.resize(N);
	for (auto& v : vec)
	{
		v.resize(M);
	}

	//체크값 초기화
	check.resize(N);
	for (auto& v : check)
	{
		v.resize(M);
	}

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			cin >> vec[i][j];
			if (vec[i][j] == 9)
			{
				q.emplace(j, i);//x y
			}
		}
	}

	while (!q.empty())
	{
		pair<int, int> xy = q.front();
		q.pop();

		int sx = xy.first;
		int sy = xy.second;
		check[sy][sx] = true;

		//4방향으로 방향값을 가진상태로 전진(하나씩 진행)
		for (int i = 0; i < 4; ++i)
		{
			int dx = sx + ax[i];
			int dy = sy + ay[i];

			//재귀
			calc(dx, dy, (Dir)i);
		}
	}

	int ans = 0;
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			if (check[i][j])
			{
				++ans;
			}
		}
	}

	cout << ans;

	return 0;
}