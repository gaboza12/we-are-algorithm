#include <bits/stdc++.h>

using namespace std;

vector<int> computer[10005];

bool vis[10005];

int n, m;

int num = 0;

vector<int> ans;

void vis_initial()
{
	for (int i = 0; i < 10005; i++)
	{
		vis[i] = false;
	}
}

void func(int idx)
{
	int temp = 1;

	vis[idx] = true;

	queue<int> q;
	q.push(idx);

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();

		for (int nxt : computer[cur])
		{
			if (!vis[nxt])
			{
				vis[nxt] = true;
				q.push(nxt);
				temp++;
			}
		}
	}
	
	if (num < temp)
	{
		num = temp;

		ans.clear();

		vector<int>().swap(ans);

		ans.push_back(idx);
	}
	else if (num == temp)
	{
		ans.push_back(idx);
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < m; i++)
	{
		int a, b;

		cin >> a >> b;

		computer[b].push_back(a);
	}

	for (int i = 1; i <= n; i++)
	{
		vis_initial();
		func(i);
	}

	sort(ans.begin(), ans.end());

	for (int i = 0; i < ans.size(); i++)
	{
		cout << ans[i] << " ";
	}
	
	return 0;
}
