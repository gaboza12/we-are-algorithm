#include <bits/stdc++.h>

using namespace std;

int n, m;

vector<int> v[1005];
int arr[1005];
queue<int> q;
vector<int> ans;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < m; i++)
	{
		int num;
		cin >> num;

		int cur;
		int prev;

		for (int j = 0; j < num; j++)
		{
			cin >> cur;

			if (j == 0)
			{
				prev = cur;
				continue;
			}
			else
			{
				v[prev].push_back(cur);
				arr[cur]++;
			}

			prev = cur;
		}
	}

	for (int i = 1; i <= n; i++)
	{
		if (arr[i] == 0)
			q.push(i);
	}

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		ans.push_back(cur);

		for (int nxt : v[cur])
		{
			arr[nxt]--;

			if (arr[nxt] == 0)
				q.push(nxt);
		}
	}

	if (ans.size() == n)
	{
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i] << "\n";
	}
	else
		cout << "0\n";
	
	return 0;
}