//
// Created by Henry Heng on 16/04/2026.
//

#ifndef CPP_MERGE_SORTED_ARRAY_H
#define CPP_MERGE_SORTED_ARRAY_H

#include <cassert>
#include <vector>
using namespace std;

class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    for (; j >= 0; k -= 1) {
      if (i >= 0 && nums1[i] >= nums2[j]) {
        nums1[k] = nums1[i--];
      } else {
        nums1[k] = nums2[j--];
      }
    }
  }
};

struct Tester {
  static void test1() {
    vector nums1 = {1, 2, 3, 0, 0, 0};
    vector nums2 = {2, 5, 6};
    constexpr int m = 3;
    constexpr int n = 3;

    auto* sol = new Solution();
    sol->merge(nums1, m, nums2, n);

    const vector ans = {1, 2, 2, 3, 5, 6};
    assert(nums1 == ans);

    cout << "test1() passed\n";
  }

  static void test2() {
    vector nums1 = {1};
    vector<int> nums2 = {};
    constexpr int m = 1;
    constexpr int n = 0;

    auto* sol = new Solution();
    sol->merge(nums1, m, nums2, n);

    const vector ans = {1};
    assert(nums1 == ans);

    cout << "test2() passed\n";
  }
};

#endif //CPP_MERGE_SORTED_ARRAY_H
