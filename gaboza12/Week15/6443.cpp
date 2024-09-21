#include <bits/stdc++.h>

using namespace std;

int n;

vector<set<string>> vs;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		string temp;

		cin >> temp;

		sort(temp.begin(), temp.end());

		set<string> s;

		do
		{
			s.insert(temp);
		} while (next_permutation(temp.begin(), temp.end()));

		vs.push_back(s);
	}

	for (int i = 0; i < vs.size(); i++)
	{
		for (auto nxt : vs[i])
		{
			cout << nxt << "\n";
		}
	}

	return 0;
}