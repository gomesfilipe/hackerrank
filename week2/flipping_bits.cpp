#include <bits/stdc++.h>
using namespace std;

unsigned int pot2[32] = {
  1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
  2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
  524288, 1048576, 2097152, 4194304, 8388608, 16777216,
  33554432, 67108864, 134217728, 268435456, 536870912,
  1073741824, 2147483648
};

int main() {
  int q;
  unsigned int n, aux, result;
  cin >> q;

  for (int i = 0; i < q; ++i) {
    cin >> n;
    result = 0;

    for (int j = 0; j < 32; ++j) {
      aux = (n >> j) & 1;

      if (aux == 0) {
        result += pot2[j];
      }
    }

    cout << result << endl;
  }

  return 0;
}
