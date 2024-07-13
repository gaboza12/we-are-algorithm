#include <bits/stdc++.h>

using namespace std;

int K, M, ans;

int maxnum;

vector<bool> check;
bool checksame[10] = { false, };

vector<int> primes;
vector<bool> sumprimes;
vector<bool> mulprimes;

void InitPrime()
{
	maxnum = pow(10, K);
	check.resize(maxnum, true);
	primes.reserve(maxnum);

	check[0] = false;
	check[1] = false;

	for (int i = 2; i * i < maxnum; ++i)
	{
		if (check[i])
		{
			for (int j = i * i; j < maxnum; j += i)
			{
				check[j] = false;
			}
		}
	}

	for (int i = 2; i < maxnum; ++i)
	{
		if (check[i])
		{
			primes.emplace_back(i);
		}
	}
}

void SumOfPrime()
{
	sumprimes.resize(maxnum, false);
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
	mulprimes.resize(maxnum, false);
	for (const auto& prime1 : primes)
	{
		if (prime1 >= maxnum)
		{
			break;
		}

		for (const auto& prime2 : primes)
		{
			long long primemul = (long long)prime1 * (long long)prime2;

			if (primemul < maxnum)
			{
				mulprimes[(int)primemul] = true;
			}
		}
	}
}

bool CheckDivision(int n)
{
	if (!sumprimes[n])
	{
		return false;
	}

	while (n % M == 0)
	{
		n /= M;
	}

	return mulprimes[n];
}

void ValidDigit(int k, int n)
{
	if (k == 0)
	{
		if (CheckDivision(n))
		{
			++ans;
		}
		return;
	}

	for (int i = 0; i <= 9; ++i)
	{
		// 맨 앞자리 0이 들어오는 거 방지
		if ((i == 0 && k == K) || checksame[i])
		{
			continue;
		}

		checksame[i] = true;
		ValidDigit(k - 1, n * 10 + i);
		checksame[i] = false;
	}
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

	//제일 높은자리부터 수를 생성하면서 최대 10^5만큼 반복
	//k는 자리 높이, n은 확인할 값
	ValidDigit(K, 0);

	cout << ans;

	return 0;
}