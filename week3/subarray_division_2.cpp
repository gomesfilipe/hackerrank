#include <bits/stdc++.h>
using namespace std;

int arr[101];

int main() {
  int n, d, m, sum = 0, count = 0;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  cin >> d >> m;

  for (int i = 0; i < m; ++i) {
    sum += arr[i];
  }

  for (int i = 0; i < n - m + 1; ++i) {
    if (sum == d) count++;
    sum += arr[i + m] - arr[i];
  }

  cout << count << endl;
  return 0;
}
