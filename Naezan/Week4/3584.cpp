#include <bits/stdc++.h>

using namespace std;

int T;
int parent[10'001];

int GetDepth(int node)
{
	int depth = 0;
	while (parent[node] != 0)
	{
		node = parent[node];
		++depth;
	}

	return depth;
}

int AdjustDepth(int node, int depthdiff)
{
	for (int i = 0; i < depthdiff; ++i)
	{
		node = parent[node];
	}

	return node;
}

int GetSameParent(int l, int r)
{
	int nl = l;
	int nr = r;

	int dl = GetDepth(nl);
	int dr = GetDepth(nr);

	//dr과 dl의 뎁스값 같도록 조정
	if (dl < dr)
	{
		nr = AdjustDepth(r, dr - dl);
	}
	else if (dl > dr)
	{
		nl = AdjustDepth(l, dl - dr);
	}

	//공통 부모 찾기
	while (nl != nr)
	{
		nl = parent[nl];
		nr = parent[nr];
	}

	return nl;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		for (int j = 0; j < N; ++j)
		{
			int a, b;
			cin >> a >> b;

			if (j == N - 1)
			{
				//공통 조상 구하기
				cout << GetSameParent(a, b) << '\n';
			}
			else
			{
				parent[b] = a;
			}
		}

		//parent 초기화
		memset(parent, 0, 10'001 * sizeof(int));
	}

	return 0;
}