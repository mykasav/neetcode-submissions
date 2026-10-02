# NeetCode Solutions

My Python solutions to [NeetCode](https://neetcode.io) data structures and algorithms problems, synced automatically on each submission. When a problem has several submissions, the later ones are usually a more efficient rewrite.

## Solved problems

### Arrays & Hashing

| Problem | Approach | Time | Solution |
|---|---|---|---|
| [Contains Duplicate](https://neetcode.io/problems/duplicate-integer) | Hash set of seen values | O(n) | [Python](Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-0.py) |
| [Valid Anagram](https://neetcode.io/problems/is-anagram) | Character frequency maps (earlier: sorting) | O(n) | [Python](Data%20Structures%20%26%20Algorithms/is-anagram/submission-3.py) |
| [Two Sum](https://neetcode.io/problems/two-integer-sum) | Hash map of value → index | O(n) | [Python](Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-0.py) |
| [Top K Frequent Elements](https://neetcode.io/problems/top-k-elements-in-list) | `Counter` + heap | O(n log k) | [Python](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/submission-0.py) |

### Two Pointers

| Problem | Approach | Time | Solution |
|---|---|---|---|
| [Valid Palindrome](https://neetcode.io/problems/is-palindrome) | Two pointers skipping non-alphanumerics, O(1) space (earlier: filtered string reversal) | O(n) | [Python](Data%20Structures%20%26%20Algorithms/is-palindrome/submission-1.py) |
| [Two Sum II](https://neetcode.io/problems/two-integer-sum-ii) | Two pointers on the sorted array | O(n) | [Python](Data%20Structures%20%26%20Algorithms/two-integer-sum-ii/submission-4.py) |

### Linked List

| Problem | Approach | Time | Solution |
|---|---|---|---|
| [Reverse Linked List](https://neetcode.io/problems/reverse-a-linked-list) | Iterative pointer reversal | O(n) | [Python](Data%20Structures%20%26%20Algorithms/reverse-a-linked-list/submission-0.py) |
| [Merge Two Sorted Lists](https://neetcode.io/problems/merge-two-sorted-linked-lists) | Dummy head + tail pointer | O(n + m) | [Python](Data%20Structures%20%26%20Algorithms/merge-two-sorted-linked-lists/submission-0.py) |
| [Linked List Cycle](https://neetcode.io/problems/linked-list-cycle-detection) | Floyd's slow/fast pointers | O(n) | [Python](Data%20Structures%20%26%20Algorithms/linked-list-cycle-detection/submission-1.py) |
| [Remove Nth Node From End](https://neetcode.io/problems/remove-node-from-end-of-linked-list) | Dummy node + fast pointer with an n-step lead | O(n) | [Python](Data%20Structures%20%26%20Algorithms/remove-node-from-end-of-linked-list/submission-0.py) |
