#include<bits/stdc++.h>
using namespace std;

int parent[10005];
bool vis[10005];

int T, N;


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> T;

	while (T--)
	{
		cin >> N;

		for (int i = 0; i < 10005; i++)
		{
			parent[i] = 0;
			vis[i] = false;
		}

		for (int i = 0; i < N - 1; i++)
		{
			int a, b;
			
			cin >> a >> b;
			parent[b] = a;
		}

		int node1, node2;

		cin >> node1 >> node2;

		vis[node1] = true;

		while (node1)
		{
			node1 = parent[node1];
			vis[node1] = true;
		}

		while (1)
		{
			if (vis[node2])
			{
				cout << node2 << "\n";
				break;
			}
			node2 = parent[node2];
		}
	}

	return 0;
}