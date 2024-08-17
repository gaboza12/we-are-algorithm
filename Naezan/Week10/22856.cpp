#include <bits/stdc++.h>

using namespace std;

int N;
int lastnode;
int ans = -1;

bool check[100'001];
vector<int> leftn;
vector<int> rightn;
vector<int> parent;

int getlast(int node)
{
	if (rightn[node] != -1)
	{
		return getlast(rightn[node]);
	}

	return node;
}

void search(int node)
{
	check[node] = true;
	++ans;

	if (leftn[node] != -1 && !check[leftn[node]])
	{
		search(leftn[node]);
	}
	else if (rightn[node] != -1 && !check[rightn[node]])
	{
		search(rightn[node]);
	}
	else if (node == lastnode)
	{
		cout << ans;
		return;
	}
	else if (parent[node] != -1)
	{
		search(parent[node]);
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;

	parent.resize(N + 1, -1);
	leftn.resize(N + 1, -1);
	rightn.resize(N + 1, -1);
	for (int i = 0;i < N;++i)
	{
		int n, a, b;
		cin >> n >> a >> b;

		leftn[n] = a;
		rightn[n] = b;

		if (a != -1)
			parent[a] = n;

		if (b != -1)
			parent[b] = n;
	}

	lastnode = getlast(1);
	search(1);

	return 0;
}

