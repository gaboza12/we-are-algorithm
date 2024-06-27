#include <bits/stdc++.h>

using namespace std;

int N;

int parent[1'000'001];
int nodes[1'000'001];

int GetParent(int idx)
{
	if (parent[idx] == idx)
	{
		return idx;
	}

	return parent[idx] = GetParent(parent[idx]);
}

void SetParent(int v1, int v2)
{
	int lv1 = GetParent(v1);
	int lv2 = GetParent(v2);

	if (lv1 < lv2)
	{
		parent[lv2] = lv1;
		nodes[lv1] += nodes[lv2];
		nodes[lv2] = 0;
	}
	else if(lv1 > lv2)
	{
		parent[lv1] = lv2;
		nodes[lv2] += nodes[lv1];
		nodes[lv1] = 0;
	}
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	cin >> N;

	for (int i = 1; i <= 1'000'000; ++i)
	{
		parent[i] = i;
		nodes[i] = 1;
	}

	for (int i = 0; i < N; ++i)
	{
		char c;

		cin >> c;

		if (c == 'I')
		{
			int a, b;
			cin >> a >> b;

			//가장 작은 값을 부모로
			SetParent(a, b);
		}
		else if (c == 'Q')
		{
			int c;
			cin >> c;

			//출력
			cout << nodes[GetParent(c)] << '\n';
		}
	}

	return 0;
}