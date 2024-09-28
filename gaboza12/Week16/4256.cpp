#include <bits/stdc++.h>

using namespace std;

int t, n;

vector<int> v_pre, v_in;

void post_order(int start, int end, int pos)
{
	for (int i = start; i < end; i++)
	{
		if (v_in[i] != v_pre[pos])
			continue;

		post_order(start, i, pos + 1);
		post_order(i + 1, end, pos + 1 + i - start);
		cout << v_pre[pos] << " ";
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> t;

	while (t--)
	{
		while (!v_pre.empty())
			v_pre.pop_back();

		while (!v_in.empty())
			v_in.pop_back();

		cin >> n;

		for (int i = 0; i < n; i++)
		{
			int temp;
			cin >> temp;
			v_pre.push_back(temp);
		}

		for (int i = 0; i < n; i++)
		{
			int temp;
			cin >> temp;
			v_in.push_back(temp);
		}

		post_order(0, n, 0);
		cout << "\n";
	}

	return 0;
}