#include <bits/stdc++.h>

using namespace std;

int n, m;
int cnt = 0;

vector<pair<int, pair<int,int>>> v; //{cost, {from, to}}
int parent[100005];

long long sum1 = 0;
long long sum2 = 0;

int find(int x)
{
	if (x == parent[x])
		return x;

	return parent[x] = find(parent[x]);
}

void uni(int x, int y)
{
	x = find(x);
	y = find(y);

	if (x == y)
		return;

	if (parent[x] < parent[y])
		swap(x, y);

	parent[y] = x;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
	{
		parent[i] = i;
	}

	for (int i = 0; i < m; i++)
	{
		int a, b, c;

		cin >> a >> b >> c;

		sum1 += c;

		v.push_back({ c, { a, b }});
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++)
	{
		int from = v[i].second.first;
		int to = v[i].second.second;
		int cost = v[i].first;

		int a = find(from);
		int b = find(to);

		if (a != b)
		{
			uni(a, b);
			sum2 += cost;

			cnt++;
		}
	}

	if (cnt != n - 1)
		cout << -1;
	else
		cout << sum1 - sum2;

	return 0;
}