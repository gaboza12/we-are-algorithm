#include<bits/stdc++.h>
using namespace std;

int K, M;
bool numbers[100001];
bool usedNum[10];
bool primeNum[100001];

void getPrime() 
{
	memset(primeNum, true, sizeof(primeNum));
	primeNum[0] = false;
	primeNum[1] = false;
	for (int i = 2; i * i <= 100000; i++) 
	{
		if (primeNum[i]) 
		{
			for (int k = i * i; k <= 100000; k += i) 
			{
				primeNum[k] = false;
			}
		}
	}
}

void input() 
{
	cin >> K >> M;
}

void rule1() 
{
	for (int i = 0; i < 100001; i++) 
	{
		if (!numbers[i]) 
			continue;
		numbers[i] = false;
		for (int j = 2; j < i / 2 + 1; j++) 
		{
			if (primeNum[j]) 
			{
				if (primeNum[i - j] && j != (i - j)) 
				{
					numbers[i] = true;
					break;
				}
			}
		}
	}
}
int getdividenum(int num, int M) {
	if (num < M) return num;
	while (true) {
		if (num%M != 0) return num;
		num = num / M;
	}
	return num;
}

void rule2() {
	for (int i = 0; i < 100001; i++) 
	{
		if (!numbers[i]) 
			continue;
		numbers[i] = false;
		int tmp = getdividenum(i, M);
		for (int j = 0; j*j < i + 1; j++) 
		{
			if (primeNum[j]) 
			{
				if (tmp%j == 0 && primeNum[tmp / j]) 
				{
					numbers[i] = true;
					break;
				}
			}
		}
	}
}

void getNumbers(int count, string num) 
{
	if (count == K) 
	{
		numbers[stoi(num)] = true;
		return;
	}
	for (int i = 0; i <= 9; i++) 
	{
		if (count == 0 && i == 0) continue;
		if (usedNum[i]) continue;
		usedNum[i] = true;
		getNumbers(count + 1, num + to_string(i));
		usedNum[i] = false;
	}
}

int sol() 
{
	int result = 0;
	getPrime();
	getNumbers(0, "");
	rule1();
	rule2();
	for (int i = 0; i < 100001; i++) 
	{
		if (numbers[i]) 
		{
			result++;
		}
	}

	return result;
}

int main() 
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	input();

	cout << sol();
	return 0;
}