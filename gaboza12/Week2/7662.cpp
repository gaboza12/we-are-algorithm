#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int T, k;

	cin >> T;

	while (T--)
	{
		cin >> k;

		priority_queue<int> mx;
		priority_queue<int, vector<int>, greater<int>> mn;

		map<int, int> cnt_check;

		for (int i = 0; i < k; i++)
		{
			char input_char;
			int input_digit;
			cin >> input_char >> input_digit;

			if (input_char == 'I')
			{
				mx.push(input_digit);
				mn.push(input_digit);

				cnt_check[input_digit]++;
			}
			else
			{
				if (input_digit == 1)
				{
					if (!mx.empty())
					{
						cnt_check[mx.top()]--;
						mx.pop();
					}
				}
				else
				{
					if (!mn.empty())
					{
						cnt_check[mn.top()]--;
						mn.pop();
					}
				}

				while (!mx.empty() && cnt_check[mx.top()] == 0)
				{
					mx.pop();
				}

				while (!mn.empty() && cnt_check[mn.top()] == 0)
				{
					mn.pop();
				}
			}
		}

		if (mx.empty() || mn.empty())
		{
			cout << "EMPTY\n";
		}
		else
		{
			cout << mx.top() << " " << mn.top() << "\n";
		}

	}

	return 0;
}