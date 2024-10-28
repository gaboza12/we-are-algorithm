#include <bits/stdc++.h>

using namespace std;

int n, t, m;

vector<int> v[10005];
int arr[10005];
int _time[10005];
int res[10005];

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	queue<int> q;

	for (int i = 1; i <= n; i++)
	{
		cin >> _time[i] >> m;

		res[i] = _time[i];

		for (int j = 0; j < m; j++)
		{
			int num;
			cin >> num;

			v[num].push_back(i);
			arr[i]++;
		}

		if (m == 0)
			q.push(i);
	}

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();

		for (int nxt : v[cur])
		{
			if (--arr[nxt] == 0)
			{
				q.push(nxt);
			}

			res[nxt] = max(res[nxt], res[cur] + _time[nxt]);
		}
	}

	for (int i = 1; i <= n; i++)
	{
		ans = max(ans, res[i]);
	}

	cout << ans;

	return 0;
}