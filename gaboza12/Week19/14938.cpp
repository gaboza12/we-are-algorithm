#include <bits/stdc++.h>

using namespace std;

int n, m, r;

int item[105];
int dist[105][105];

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> r;

	for (int i = 1; i <= n; i++)
	{
		cin >> item[i];
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			if (i == j)
			{
				dist[i][j] = 0;
			}
			else
			{
				dist[i][j] = 1e9 + 10;
			}
		}
	}

	for (int i = 0; i < r; i++)
	{
		int a, b, l;

		cin >> a >> b >> l;
		dist[a][b] = min(dist[a][b], l);
		dist[b][a] = min(dist[b][a], l);
	}

	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}

	for (int i = 1; i <= n; i++)
	{
		int temp = item[i];

		for (int j = 1; j <= n; j++)
		{
			if (i == j)
				continue;

			if (dist[i][j] <= m)
			{
				temp += item[j];
			}
		}

		ans = max(ans, temp);
	}

	cout << ans;

	return 0;
}