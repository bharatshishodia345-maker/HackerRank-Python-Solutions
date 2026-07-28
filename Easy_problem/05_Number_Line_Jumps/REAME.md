# Number Line Jumps – Kangaroo

## Problem

Two kangaroos start at different positions on a number line and jump forward at different speeds.

The task is to determine whether they can land on the **same position at the same time**.

Return:

* `YES` → if both kangaroos meet at the same position at the same time.
* `NO` → otherwise.

## Approach

For the kangaroos to meet:

* The first kangaroo must be behind the second kangaroo initially.
* The first kangaroo must have a greater jump speed.
* The difference in starting positions must be exactly divisible by the difference in jump speeds.

The solution checks these conditions using the modulo `%` operator.

## Example

```text
Input:
0 3 4 2

Output:
YES
```

Explanation:

```text
Kangaroo 1: 0 → 3 → 6 → 9 → 12
Kangaroo 2: 4 → 6 → 8 → 10 → 12
```

They meet at position `12`.

## Concepts Practiced

* Functions
* Conditional statements
* `if-else`
* Modulo `%` operator
* Mathematical logic
* HackerRank problem solving

## Complexity

* **Time Complexity:** O(1)
* **Space Complexity:** O(1)

## Platform

HackerRank – Algorithms

````


git status
git add Easy_problem/05_Number_Line_Jumps/
git commit -m "Add Number Line Jumps solution"
git push origin main
