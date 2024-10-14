#include <bits/stdc++.h>

using namespace std;

int n;

vector<string> v;

bool cmp(string s1, string s2)
{
	int sz = max(s1.size(), s2.size());

	for (int i = 0; i < sz; i++)
	{
		if (i >= s1.size() || i >= s2.size())
			break;

		//isalpha : A-Z = 1 / a-z = 2 / 알파벳 아니면 0
		if (s1[i] != s2[i] && (isalpha(s1[i]) || isalpha(s2[i])))
		{
			//둘중에 하나가 숫자면
			if (isdigit(s1[i]) || isdigit(s2[i]))
			{
				return isdigit(s1[i]);
			}

			char temp1 = isupper(s1[i]) ? s1[i] - 'A' : s1[i] - 'a';
			char temp2 = isupper(s2[i]) ? s2[i] - 'A' : s2[i] - 'a';

			//같은 알파벳이면 대문자먼저
			if (temp1 == temp2)
			{
				return isupper(s1[i]);
			}
			//다른 알파벳이면 알파벳순
			else
			{
				return temp1 < temp2;
			}
		}
		//둘다 숫자면
		else if (isdigit(s1[i]) && isdigit(s2[i]))
		{
			int zeroCnt1 = 0, zeroCnt2 = 0;
			int state = 0;

			while (s1[i] == '0')
			{
				s1.erase(s1.begin() + i);
				zeroCnt1++;
			}

			while (s2[i] == '0')
			{
				s2.erase(s2.begin() + i);
				zeroCnt2++;
			}

			while (isdigit(s1[i]) || isdigit(s2[i]))
			{
				if (s1.size() != s2.size() && (i >= s1.size() || i >= s2.size()))
				{
					return s1.size() < s2.size();
				}

				if (isalpha(s1[i]) || isalpha(s2[i]))
				{
					return isalpha(s1[i]);
				}

				if (state == 0 && s1[i] != s2[i])
				{
					state = 1 + (s1[i] < s2[i]);
				}

				i++;
			}

			if (state)
			{
				return state - 1;
			}

			if (zeroCnt1 != zeroCnt2)
			{
				return zeroCnt1 < zeroCnt2;
			}

			i--;
		}
	}

	return s1.size() < s2.size();
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		string temp;
		cin >> temp;
		v.push_back(temp);
	}

	sort(v.begin(), v.end(), cmp);

	for (int i = 0; i < v.size(); i++)
	{
		cout << v[i] << "\n";
	}

	return 0;
}