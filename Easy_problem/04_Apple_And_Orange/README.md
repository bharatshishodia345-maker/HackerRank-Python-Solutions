# Apple and Orange

## 📌 Problem

Given a house represented by the range `[s, t]`, an apple tree is located at position `a` and an orange tree is located at position `b`.

We need to calculate:

- How many apples fall on the house.
- How many oranges fall on the house.

The final position of each fruit is calculated using:

`fruit_position = tree_position + fruit_distance`

## 🧠 Approach

1. Start the apple count from `0`.
2. For every apple, calculate its landing position.
3. Check whether the position lies between `s` and `t`.
4. If yes, increase the apple count.
5. Repeat the same process for oranges.
6. Print both counts.

## 💻 Concepts Used

- Functions
- Lists
- `for` loops
- Conditional statements
- Range checking
- Counting

## ⏱️ Complexity

Time Complexity: `O(m + n)`

Space Complexity: `O(1)` excluding the input arrays.

## 🛠️ Language

Python 3

## 🎯 Learning Outcome

Learned how to iterate through arrays, calculate positions, check whether values fall within a given range, and count matching elements.