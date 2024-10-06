#include <bits/stdc++.h>
using namespace std;

bool validTriangle(unsigned int a, unsigned int b, unsigned int c) {
  return a < b + c && b < a + c && c < a + b;
}

unsigned int perimeter(unsigned int a, unsigned int b, unsigned int c) {
  return a + b + c;
}

unsigned int maxx3(unsigned int a, unsigned int b, unsigned int c) {
  return max(max(a, b), c);
}

unsigned int minn3(unsigned int a, unsigned int b, unsigned int c) {
  return min(min(a, b), c);
}

void sort3(unsigned int* a, unsigned int* b, unsigned int* c) {
  vector<unsigned int> v;
  v.push_back(*a);
  v.push_back(*b);
  v.push_back(*c);

  sort(v.begin(), v.end());

  *a = v[0];
  *b = v[1];
  *c = v[2];
}

void updateMaxTriangle(unsigned int* max1, unsigned int* max2, unsigned int* max3, unsigned int b1, unsigned int b2, unsigned int b3) {
  if (! validTriangle(b1, b2, b3)) return;

  unsigned int p1 = perimeter(b1, b2, b3);
  unsigned int p2 = perimeter(*max1, *max2, *max3);

  if (p1 < p2) {
    return;
  }

  else if (p1 > p2) {
    *max1 = b1;
    *max2 = b2;
    *max3 = b3;
  }

  else if (maxx3(b1, b2, b3) > maxx3(*max1, *max2, *max3)) {
    *max1 = b1;
    *max2 = b2;
    *max3 = b3;
  }

  else if (minn3(b1, b2, b3) > minn3(*max1, *max2, *max3)) {
    *max1 = b1;
    *max2 = b2;
    *max3 = b3;
  }
}

unsigned int arr[50];

int main() {
  unsigned int n, max1 = 0, max2 = 0, max3 = 0;
  cin >> n;

  for (unsigned int i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  for (unsigned int i = 0; i < n; ++i) {
    for (unsigned int j = i + 1; j < n; ++j) {
      for (unsigned int k = j + 1; k < n; ++k) {
        updateMaxTriangle(&max1, &max2, &max3, arr[i], arr[j], arr[k]);
      }
    }
  }

  if (max1 == 0) {
    cout << -1 << endl;
  } else {
    sort3(&max1, &max2, &max3);
    cout << max1 << " " << max2 << " " << max3 << endl;
  }

  return 0;
}
