#include <bits/stdc++.h>

using namespace std;

int N, ans;
int coin[10'001];
int parent[10'001];
vector<vector<int>> childs;

void calc(int idx)
{
	//자식노드 순회
	for (int child : childs[idx])
	{
		calc(child);
	}

	//부모로 코인 전달
	if (coin[idx] > 1)
	{
		coin[parent[idx]] += (coin[idx] - 1);
		ans += (coin[idx] - 1);
	}
	//코인이 부족하면 부모 코인 회수
	else if (coin[idx] <= 0)
	{
		coin[parent[idx]] += (coin[idx] - 1);
		ans -= (coin[idx] - 1);
	}

	coin[idx] = 1;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	while (true)
	{
		cin >> N;

		if (N == 0)
		{
			break;
		}

		memset(coin, 0, sizeof(coin));
		memset(parent, 0, sizeof(parent));
		childs.clear();
		childs.resize(N + 1);

		for (int i = 0; i < N; ++i)
		{
			//정점, 구슬개수, 자식 수
			int v, c, d;
			cin >> v >> c >> d;
			coin[v] = c;

			//자식 셋팅
			for (int j = 0; j < d; ++j)
			{
				int ch;
				cin >> ch;
				childs[v].push_back(ch);
				parent[ch] = v;
			}
		}

		//최소횟수 구하기
		for (int i = 1; i <= N; ++i)
		{
			calc(i);
		}

		cout << ans << '\n';
		ans = 0;
	}

	return 0;
}