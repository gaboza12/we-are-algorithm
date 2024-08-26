#include<bits/stdc++.h>
using namespace std;

int parent[200005];
int sizes[200005];

int find(int x)
{
	if (parent[x] == x)
		return parent[x];

	return parent[x] = find(parent[x]);
}

void Union(int a, int b)
{
	a = find(a);
	b = find(b);

	if (a == b)
		return;

	if (sizes[a] < sizes[b])
		swap(a, b);

	parent[b] = a;
	sizes[a] += sizes[b];
	sizes[b] = 0;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int testCase, F;

	cin >> testCase;

	while (testCase--)
	{
		for (int i = 0; i < 200005; i++)
		{
			parent[i] = i;
			sizes[i] = 1;
		}

		cin >> F;

		map<string, int> human;
		int num = 1;

		for (int i = 0; i < F; i++)
		{
			string name1, name2;

			cin >> name1 >> name2;

			if (human.count(name1) == 0)
				human[name1] = num++;

			if (human.count(name2) == 0)
				human[name2] = num++;

			Union(human[name1], human[name2]);

			int temp1, temp2;

			temp1 = find(human[name1]);
			temp2 = find(human[name2]);

			cout << max(sizes[temp1], sizes[temp2]) << "\n";
		}
	}

	return 0;
}