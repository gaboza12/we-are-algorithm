#include <bits/stdc++.h>

using namespace std;

int t;

int func(int left, int right, string str, bool flag)
{
	while (left < right)
	{
		if (str[left] != str[right])
		{
			if (!flag)
			{
				//유사 회문
				if (func(left + 1, right, str, true) == 0 || func(left, right - 1, str, true) == 0)
					return 1;
			}
			//회문, 유사회문 아님
			return 2;
		}

		left++;
		right--;
	}
	//while문 통과하면 회문
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		string s;

		cin >> s;

		cout << func(0, s.size() - 1, s, false) << "\n";
	}

	return 0;
}