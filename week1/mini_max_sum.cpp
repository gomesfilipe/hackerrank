#include <bits/stdc++.h>
using namespace std;

int main() {
  unsigned long long sum = 0, aux, minn = 1000000000, maxx = 1;

  for (int i = 0; i < 5; ++i) {
    cin >> aux;
    sum += aux;

    minn = min(minn, aux);
    maxx = max(maxx, aux);
  }

  cout << sum - maxx << " " << sum - minn << endl;
  return 0;
}
