#include<bits/stdc++.h>
using namespace std;

int parent[10005];
int cost[10005];

bool vis[10005];

int find(int x)
{
	if (parent[x] == x)
		return x;

	return parent[x] = find(parent[x]);
}

void Union(int a, int b)
{
	a = find(a);
	b = find(b);

	if (a == b)
		return;

	if (cost[a] >= cost[b])
		parent[a] = b;
	else
		parent[b] = a;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, M, k;

	cin >> N >> M >> k;

	for (int i = 1; i <= N; i++)
	{
		cin >> cost[i];
		parent[i] = i;
	}

	for (int i = 0; i < M; i++)
	{
		int v, w;
		cin >> v >> w;

		Union(v, w);
	}

	int cost_sum = 0;

	for (int i = 1; i <= N; i++)
	{
		int cur = find(i);

		if (!vis[cur])
		{
			cost_sum += cost[cur];
			vis[cur] = true;
		}
	}

	if (cost_sum > k)
		cout << "Oh no\n";
	else
		cout << cost_sum;

	return 0;
}