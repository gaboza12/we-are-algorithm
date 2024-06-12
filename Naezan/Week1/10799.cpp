#include <iostream>

using namespace std;

int stickl;
int ans;

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	char c;
	char prevstick = '(';
	while ((c = cin.get()) != '\n')
	{
		if (c == '(')
		{
			++stickl;
		}
		else if (c == ')')
		{
			if (prevstick == '(')
			{
				ans += (--stickl);
			}
			else
			{
				++ans;
				--stickl;
			}
		}

		prevstick = c;
	}

	cout << ans;

	return 0;
}