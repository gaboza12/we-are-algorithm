#include <bits/stdc++.h>

using namespace std;

int N, K;

int ans;

char rem[5] = { 'a', 'n','t','i','c' };
vector<string> words;

unordered_map<char, bool> learn;

void calc(std::unordered_map<char, bool>::iterator iter, int rc)
{
	if (rc == 0)
	{
		int learncount = 0;
		//words에 있는 값들과 check한 값을 비교해서 몇개까지 배웠는지 카운팅
		for (const string& s : words)
		{
			bool bhaslearn = true;
			for (const char c : s)
			{
				//해당 값을 배우지 않았다면
				if (!learn[c])
				{
					bhaslearn = false;
					break;
				}
			}

			//배운 단어라면 ans++해줌
			if (bhaslearn)
			{
				++learncount;
			}
		}

		ans = max(ans, learncount);
		return;
	}

	//단어를 배우는데 순서는 필요없음
	for (; iter != learn.end(); ++iter)
	{
		if (iter->second)
		{
			continue;
		}

		iter->second = true;
		calc(iter, rc - 1);
		iter->second = false;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> K;

	for (int i = 0; i < N; ++i)
	{
		string s;
		cin >> s;

		sort(s.begin(), s.end());

		//중복요소 잘라내기
		auto last = std::unique(s.begin(), s.end());
		s.erase(last, s.end());

		for (int j = 0; j < 5; ++j)
		{
			s.erase(std::remove(s.begin(), s.end(), rem[j]), s.end());
		}

		words.push_back(s);

		for (const char c : s)
		{
			learn.emplace(c, false);
		}
	}

	if (K < 5)
	{
		cout << 0 << '\n';
		return 0;
	}

	//모두 배울 수 있다면
	if (learn.size() <= K - 5)
	{
		cout << N << '\n';
		return 0;
	}

	calc(learn.begin(), K - 5);

	cout << ans << '\n';

	return 0;
}