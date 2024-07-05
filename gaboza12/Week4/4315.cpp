#include<bits/stdc++.h>
using namespace std;

int parent[10005];
int bead[10005];
vector<vector<int>> children;

int move_cnt = 0;

void dfs(int node)
{
	for (int i = 0; i < children[node].size(); i++)
	{
		dfs(children[node][i]);
	}

	bead[parent[node]] += (bead[node] - 1);
	move_cnt += abs(bead[node] - 1);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, v, bead_cnt, d;

	while (cin >> n, n)
	{
		fill(parent, parent + 10005, 0);
		fill(bead, bead + 10005, 0);

		children.clear();
		children.resize(n + 5);

		move_cnt = 0;
		
		int root = 0;

		for (int i = 0; i < n; i++)
		{
			cin >> v >> bead_cnt >> d;

			bead[v] = bead_cnt;
			
			for (int j = 0; j < d; j++)
			{
				int child;
				cin >> child;

				parent[child] = v;
				children[v].push_back(child);
			}
		}

		for (int i = 1; i <= n; i++)
		{
			if (parent[i] == 0)
			{
				root = i;
				break;
			}
		}

		dfs(root);

		cout << move_cnt << "\n";
	}

	return 0;
}