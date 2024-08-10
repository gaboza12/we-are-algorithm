#include <bits/stdc++.h>

using namespace std;

int n, c;
long long ans;

vector<pair<int, int>> x[100005];//[x](y,v)
vector<pair<int, int>> y[100005];//[y](x,v)

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> c;

	for (int i = 0; i < n; i++)
	{
		int a, b, c;
		
		cin >> a >> b >> c;

		x[a].push_back({ b, c });
		y[b].push_back({ a, c });
	}

	int cur_x = 100000;
	int cur_y = 0;

	long long num = 0;
	int cnt = 0;

	while (1)
	{
		if (cur_x < 0 || cur_y > 100000)
			break;

		if (cnt <= c)
		{
			for (int i = 0; i < y[cur_y].size(); i++)
			{
				if (y[cur_y][i].first <= cur_x)
				{
					cnt++;
					num += y[cur_y][i].second;
				}
			}
			cur_y++;
		}
		else
		{
			for (int i = 0; i < x[cur_x].size(); i++)
			{
				if (x[cur_x][i].first <= cur_y - 1)
				{
					cnt--;
					num -= x[cur_x][i].second;
				}
			}
			cur_x--;
		}

		if (cnt <= c)
			ans = max(ans, num);
	}

	cout << ans;

	return 0;
}