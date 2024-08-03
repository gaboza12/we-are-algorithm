#include <bits/stdc++.h>

using namespace std;

int M, N;

// 초기식
// arr[i][j]는 i, j에서 끝까지 도달할 수 있는 경로의 수
// 점화식을 찾을 수 없었음 -> 기존의 dp랑 약간 다른 스타일의 형식
// 점화식이 아닌 피보나치 스타일로 구현했어야 했던 문제

int arr[501][501];
int dp[501][501];
bool check[501][501];
int x[4] = { 0, 0, 1, -1 };
int y[4] = { 1, -1, 0, 0 };

int calc(int _x, int _y)
{
	if (_x == N - 1 && _y == M - 1)
	{
		return 1;
	}

	if (check[_y][_x])
	{
		return dp[_y][_x];
	}

	check[_y][_x] = true;
	for (int i = 0; i < 4; ++i)
	{
		int dx = _x + x[i];
		int dy = _y + y[i];

		if (dx < 0 || dy < 0 || dx >= N || dy >= M)
		{
			continue;
		}

		//더 작은 값인 경우
		if (arr[_y][_x] > arr[dy][dx])
		{
			dp[_y][_x] += calc(dx, dy);
		}
	}

	return dp[_y][_x];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> M >> N;

	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			cin >> arr[i][j];
		}
	}
	
	cout << calc(0, 0) << "\n";

	return 0;
}