#include <iostream>
#include <stack>

using namespace std;

int ans;
stack<char> s;
// 계산된 숫자들
stack<int> calceds;

void calc(int scale)
{
	int nidx = 0;
	int p = calceds.top();
	while (p != 0)
	{
		p = calceds.top();
		nidx += p;
		calceds.pop();
	}

	if (nidx == 0)
	{
		nidx = scale;
		calceds.pop();
	}
	else
	{
		nidx = nidx * scale;
	}
	calceds.push(nidx);
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	char c;
	while ((c = cin.get()) != '\n')
	{
		if (c == ')')
		{
			if (!s.empty())
			{
				if (s.top() == '(')
				{
					s.pop();

					calc(2);
				}
			}
			else
			{
				s.push(c);
			}
		}
		else if (c == ']')
		{
			if (!s.empty())
			{
				if (s.top() == '[')
				{
					s.pop();

					calc(3);
				}
			}
			else
			{
				s.push(c);
			}
		}
		else
		{
			calceds.push(0);
			s.push(c);
		}
	}

	if (s.size() != 0)
	{
		ans = 0;
	}
	else
	{
		while (!calceds.empty())
		{
			ans += calceds.top();
			calceds.pop();
		}

		cout << ans;
	}

	return 0;
}