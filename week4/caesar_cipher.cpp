#include <bits/stdc++.h>
using namespace std;

char convertChar(char c, int k) {
  if (islower(c)) return (c + k - 'a') % 26 + 'a';
  if (isupper(c)) return (c + k - 'A') % 26 + 'A';
  return c;
}

void casearCipher(string& s, int k) {
  for (int i = 0; i < s.size(); ++i) {
    s[i] = convertChar(s[i], k);
  }
}

int main() {
  int n, k;
  string s;

  cin >> n;
  getline(cin, s);
  getline(cin, s);
  cin >> k;
  casearCipher(s, k);
  cout << s << endl;

  return 0;
}
