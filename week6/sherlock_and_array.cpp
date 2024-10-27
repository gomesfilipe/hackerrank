#include <iostream>
#include <vector>
using namespace std;

int arr[100000];

int main () {
  int t, n, sum, leftSum, rightSum;
  bool yes;
  cin >> t;

  while (t--) {
    cin >> n;
    sum = 0;
    yes = false;

    for (int i = 0; i < n; ++i) {
      cin >> arr[i];
      sum += arr[i];
    }

    leftSum = 0;
    rightSum = sum;

    for (int i = 0; i < n; ++i) {
      rightSum -= arr[i];

      if (leftSum == rightSum) {
        yes = true;
        break;
      }

      leftSum += arr[i];
    }

    if (yes) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }

  return 0;
}