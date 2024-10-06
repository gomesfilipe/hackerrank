#include <bits/stdc++.h>
using namespace std;

void readArray(vector<int>& v, int n) {
  int aux;
  for (int i = 0; i < n; ++i) {
    cin >> aux;
    v.push_back(aux);
  }
}

vector<int> a;
vector<int> b;

int main() {
  int q, n, k;
  bool result;
  cin >> q;

  while (q--) {
    cin >> n >> k;

    readArray(a, n);
    readArray(b, n);

    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), greater<>());

    result = true;
    int i = 0, j = 0;

    while (i < n && j < n) {
      if (a[i] + b[j] < k) {
        result = false;
        break;
      }

      i++;
      j++;
    }

    if (result) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }

    a.clear();
    b.clear();
  }

  return 0;
}
