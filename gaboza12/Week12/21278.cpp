#include <bits/stdc++.h>

using namespace std;

int n, m;

vector<int> v[105];

int arr[105];

int ans1, ans2;
int sum = 1e9 + 10;

void arr_initial()
{
	for (int i = 0; i < 105; i++)
	{
		arr[i] = 10000;
	}
}

void func(int a, int b)
{
	arr_initial();

	queue<int> q;
	q.push(a);
	arr[a] = 0;

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();

		for (int nxt : v[cur])
		{
			if (arr[nxt] > arr[cur] + 2)//왕복이라 + 2
			{
				arr[nxt] = arr[cur] + 2;
				q.push(nxt);
			}
		}
	}

	q.push(b);
	arr[b] = 0;

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();

		for (int nxt : v[cur])
		{
			if (arr[nxt] > arr[cur] + 2)
			{
				arr[nxt] = arr[cur] + 2;
				q.push(nxt);
			}
		}
	}

	int res = 0;

	for (int i = 1; i <= n; i++)
	{
		res += arr[i];
	}

	if (sum > res)
	{
		sum = res;
		ans1 = a;
		ans2 = b;
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

		v[a].push_back(b);
		v[b].push_back(a);
	}

	for (int i = 1; i <= n; i++)
	{
		sort(v[i].begin(), v[i].end());
	}

	for (int i = 1; i < n; i++)
	{
		for (int j = i + 1; j <= n; j++)
		{
			func(i, j);
		}
	}

	cout << ans1 << " " << ans2 << " " << sum;

	return 0;
}