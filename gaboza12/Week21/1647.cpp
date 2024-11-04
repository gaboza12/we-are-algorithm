#include <bits/stdc++.h>

using namespace std;

int n, m;
int parent[100005];
int ans = 0;
int mx = 0;

vector<pair<int, pair<int, int>>> v;

int find(int x)
{
	if (parent[x] == x)
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
		parent[i] = i;

	for (int i = 0; i < m; i++)
	{
		int a, b, c;

		cin >> a >> b >> c;

		v.push_back({ c, {a, b} });
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
			ans += cost;
			mx = max(mx, cost);
		}
	}

	cout << ans - mx;

	return 0;
}