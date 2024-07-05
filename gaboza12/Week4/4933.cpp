#include<bits/stdc++.h>
using namespace std;

vector<int> treeA_parent, treeB_parent;
int childCount[26];

vector<string> v;

void Init()
{
	treeA_parent.clear();
	treeB_parent.clear();

	fill(childCount, childCount + 26, 0);
	for (int i = 0; i < 26; i++)
	{
		treeA_parent.push_back(-1);
		treeB_parent.push_back(-1);
	}
}

void MakeTree(vector<int>& tree)
{
	stack<char> s;
	s.push(v[0][0]);
	tree[s.top() - 'A'] = (s.top() - 'A' + 1);

	for (int i = 1; i < v.size(); i++)
	{
		while (childCount[s.top() - 'A'] == 2)
		{
			s.pop();
		}

		childCount[s.top() - 'A']++;

		if (v[i] != "nil")
		{
			tree[v[i][0] - 'A'] = (s.top() - 'A' + 1);
			s.push(v[i][0]);
		}
	}

	fill(childCount, childCount + 26, 0);
}

void Input_String()
{
	v.clear();

	string input;

	while (1)
	{
		cin >> input;
		if (input == "end")
		{
			break;
		}
		else
		{
			v.push_back(input);
		}
	}

	reverse(v.begin(), v.end());
}

void Check_Print()
{
	bool check = true;
	for (int i = 0; i < 26; i++)
	{
		if (treeA_parent[i] != treeB_parent[i])
		{
			check = false;
			break;
		}
	}

	check ? cout << "true\n" : cout << "false\n";
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int T;

	cin >> T;

	while (T--)
	{
		Init();

		Input_String();
		MakeTree(treeA_parent);

		Input_String();
		MakeTree(treeB_parent);

		Check_Print();
	}

	return 0;
}