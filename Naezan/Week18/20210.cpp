#include <bits/stdc++.h>

using namespace std;

int N;

vector<string> vec;

bool isalpha(const char c)
{
	return tolower(c) >= 'a' && tolower(c) <= 'z';
}

bool compalpha(const char l, const char r)
{
	char wl = tolower(l);
	char wr = tolower(r);
	if (wl == wr)
	{
		return l < r;
	}

	return wl < wr;
}

string getnum(const string& s, int idx, int& zeroc)
{
	string temps;

	bool bhaszero = true;
	while (idx < s.size())
	{
		if (isalpha(s[idx]))
		{
			return temps;
		}

		if (bhaszero)
		{
			if (s[idx] == '0')
			{
				++zeroc;
			}
			else
			{
				bhaszero = false;
			}
		}

		if (!bhaszero)
		{
			temps.push_back(s[idx]);
		}

		++idx;
	}

	//idx부터 s끝까지
	return temps;
}

bool comp(const string& ls, const string& rs)
{
	int lidx = 0;
	int ridx = 0;

	while (lidx < ls.size() && ridx < rs.size())
	{
		//알파벳은 그냥 하나씩대소비교(대소문자별로 다름)
		if (isalpha(ls[lidx]) && isalpha(rs[ridx]))
		{
			if (ls[lidx] != rs[ridx])
				return compalpha(ls[lidx], rs[ridx]);

			++lidx;
			++ridx;
			continue;
		}

		//둘 다 알파벳이 아니라 숫자인 경우
		if (!isalpha(ls[lidx]) && !isalpha(rs[ridx]))
		{
			int outzerol = 0;
			int outzeror = 0;
			string ln = getnum(ls, lidx, outzerol);
			string rn = getnum(rs, ridx, outzeror);

			//숫자길이가 같으면 그냥 일반비교
			if (ln.size() == rn.size())
			{
				//다만 앞에 0이 있는경우 갯수가 크면 뒤로감
				if (ln == rn)
				{
					if (outzerol != outzeror)
						return outzerol < outzeror;
				}
				else
				{
					return ln < rn;
				}
			}
			//숫자인경우 길이가 다르면 길이가 작은수가 먼저옴
			else
			{
				return ln.size() < rn.size();
			}

			lidx += ln.size() + outzerol;
			ridx += rn.size() + outzeror;
			continue;
		}

		//서로 알파벳이나 숫자라면 알파벳이 뒤로감
		if (isalpha(ls[lidx]))
		{
			return false;
		}

		if (isalpha(rs[ridx]))
		{
			return true;
		}
	}
	
	//둘 중 하나의 크기가 더 크다는 뜻이므로 큰값이 뒤로감
	return ls.size() < rs.size();
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	vec.resize(N);

	for (int i = 0; i < N; ++i)
	{
		cin >> vec[i];
	}

	sort(vec.begin(), vec.end(), comp);

	for (int i = 0; i < N; ++i)
	{
		cout << vec[i] << '\n';
	}

	return 0;
}