#include <bits/stdc++.h>

using namespace std;

int n, m;

vector<int> v[1005];
int ans[1005];
int arr[1005];//선행조건

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	queue<int> q;

	for (int i = 0; i < m; i++)
	{
		int a, b;

		cin >> a >> b;

		v[a].push_back(b);
		arr[b]++;
	}

	for (int i = 1; i <= n; i++)
	{
		ans[i] = 1;

		if (arr[i] == 0)
		{
			q.push(i);
		}
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
				ans[nxt] = ans[cur] + 1;
			}
		}
	}

	for (int i = 1; i <= n; i++)
	{
		cout << ans[i] << " ";
	}

	return 0;
}