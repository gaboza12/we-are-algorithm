#include <bits/stdc++.h>

using namespace std;

int T;
int parent1[30];
int parent2[30];

void ProcessTree(int* parent)
{
	stack<int> stree;
	string s("none");

	while (s != "end")
	{
		cin >> s;

		if (s == "end")
		{
			//루트가 다를 수도 있으니 체크
			if (!stree.empty())
			{
				int root = stree.top();
				parent[root] = root;
				stree.pop();
			}
			
			break;
		}

		// 0번째는 nil로 사용
		if (s == "nil")
		{
			stree.push(0);
		}
		else
		{
			//스택이 2개이상 채우면 후위 순회하며 부모 셋팅
			if (stree.size() >= 2)
			{
				//왼쪽 -> 오른쪽
				int left = stree.top();
				stree.pop();
				int right = stree.top();
				stree.pop();

				parent[left] = s[0] - 'A' + 1;
				parent[right] = s[0] - 'A' + 1;
			}

			//부모
			stree.push(s[0] - 'A' + 1);
		}
	}

	parent[0] = 0;
}

bool IsSameTree()
{
	for (int i = 0; i < 30; ++i)
	{
		if (parent1[i] != parent2[i])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		memset(parent1, 0, 30 * sizeof(int));
		memset(parent2, 0, 30 * sizeof(int));

		ProcessTree(parent1);
		ProcessTree(parent2);

		//트리 비교 -> 부모가 같은지 비교
		if (IsSameTree())
		{
			cout << "true\n";
		}
		else
		{
			cout << "false\n";
		}
	}

	return 0;
}