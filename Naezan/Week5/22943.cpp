#include <bits/stdc++.h>

using namespace std;

int K, M, ans;

int maxnum;

// false인 경우 소수임
vector<bool> check;
vector<int> samecheck;

vector<int> primes;
unordered_map<int, bool> sumprimes;
unordered_map<int, bool> mulprimes;

void InitPrime()
{
	maxnum = pow(10, K);
	check.resize(maxnum + 1, true);

	check[0] = false;
	check[1] = false;

	for (int i = 2; i <= (int)sqrt(maxnum); ++i)
	{
		if (check[i])
		{
			for (int j = i * i; j < maxnum; j += i)
			{
				check[j] = false;
			}
		}
	}

	for (int i = 2; i <= maxnum; ++i)
	{
		if (check[i])
		{
			primes.emplace_back(i);
		}
	}
}

void SumOfPrime()
{
	for (const auto& prime1 : primes)
	{
		// 최댓값보다 큰값이면 더이상 조사할 필요도 없음
		if (prime1 >= maxnum)
		{
			break;
		}

		for (const auto& prime2 : primes)
		{
			//같은 값끼리는 더하는 조건X
			if (prime1 == prime2)
			{
				continue;
			}

			int primesum = prime1 + prime2;

			if (primesum < maxnum)
			{
				sumprimes[primesum] = true;
			}
		}
	}
}

void MulOfPrime()
{
	for (const auto& prime1 : primes)
	{
		if (prime1 >= maxnum)
		{
			break;
		}

		for (const auto& prime2 : primes)
		{
			long long primemul = (long long)prime1 * (long long)prime2;

			if (sumprimes.count((int)primemul) > 0)
			{
				if (sumprimes[(int)primemul] && primemul < maxnum)
				{
					mulprimes[(int)primemul] = true;
				}
			}
		}
	}
}

bool ValidDigit(const string& s)
{
	samecheck.resize(10, 0);
	//각 자릿수를 순회하며 중복갯수 확인
	for (int i = 0; i < s.size(); ++i)
	{
		int n = s[i] - '0';
		++samecheck[n];
	}

	int count = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		int n = s[i] - '0';
		if (samecheck[n] > 0)
		{
			++count;
		}

		//중복갯수가 1이 넘어가면 유효하지 않음
		if (samecheck[n] > 1)
		{
			return false;
		}
	}

	//K갯수만큼 없으면 유효하지 않음
	return count == K;
}

bool CheckDivision(int n)
{
	while (n % M == 0)
	{
		n /= M;
	}

	return mulprimes.count(n) > 0;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> K >> M;

	InitPrime();

	SumOfPrime();

	MulOfPrime();

	for (const auto& prime : mulprimes)
	{
		if (prime.second)
		{
			if (CheckDivision(prime.first))
			{
				string s = to_string(prime.first);
				if (ValidDigit(s))
				{
					++ans;
				}
			}
		}
	}

	cout << ans;

	return 0;
}