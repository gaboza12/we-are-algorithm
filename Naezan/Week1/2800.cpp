#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <string>

using namespace std;

string str;
stack<int> s1;
vector<pair<int, int>> s2;
priority_queue<string, vector<string>, greater<string>> ans;

void calc(string s, int idx)
{
	if (idx > s2.size() - 1)
	{
		//��������
		s.erase(remove_if(s.begin(), s.end(), [](char c) {
			return isspace(c);
			}), s.end());

		//������ ��
		if (s != str)
		{
			ans.push(s);
		}
		return;
	}

	string ds = s;
	for (int i = 0; i < str.size(); ++i)
	{
		if (i == s2[idx].first || i == s2[idx].second)
		{
			ds[i] = ' ';
		}
	}

	calc(ds, idx + 1);
	calc(s, idx + 1);
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	cin >> str;

	//�� ��ȣ�� ���ϱ�
	for (int i = 0; i < str.size(); ++i)
	{
		if (str[i] == '(')
		{
			s1.push(i);
		}
		else if (str[i] == ')')
		{
			s2.emplace_back(s1.top(), i);
			s1.pop();
		}
	}

	//��������� ��ȣ�� �߰� �ݺ� 2^n���� ���⵵
	calc(str, 0);

	string prev;
	while (!ans.empty())
	{
		if(prev != ans.top())
			cout << ans.top() << '\n';

		prev = ans.top();
		ans.pop();
	}

	return 0;
}