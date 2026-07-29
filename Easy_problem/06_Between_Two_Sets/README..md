# Between Two Sets - HackerRank (Python)

## Problem Statement

There are two arrays of integers:

- Every element of the first array (`a`) must be a factor of the chosen integer.
- The chosen integer must be a factor of every element in the second array (`b`).

The task is to determine how many integers satisfy both conditions.

### Example

```python
a = [2, 4]
b = [16, 32, 96]
```

**Output**

```text
3
```

The valid integers are:

```text
4, 8, 16
```

---

## Approach

1. Find the starting point as the **maximum element** of array `a`.
2. Find the ending point as the **minimum element** of array `b`.
3. Check every number in this range.
4. For each number:
   - Verify it is divisible by every element in `a`.
   - Verify every element in `b` is divisible by it.
5. Count all valid numbers.

---

## Python Solution

```python
def getTotalX(a, b):
    start = max(a)
    end = min(b)

    count = 0

    for num in range(start, end + 1):

        valid = True

        # Check if all elements of 'a' are factors of num
        for value in a:
            if num % value != 0:
                valid = False
                break

        if not valid:
            continue

        # Check if num is a factor of all elements of 'b'
        for value in b:
            if value % num != 0:
                valid = False
                break

        if valid:
            count += 1

    return count
```

---

## Time Complexity

```text
O((min(b) - max(a)) × (len(a) + len(b)))
```

---

## Space Complexity

```text
O(1)
```

---

## Concepts Used

- Arrays
- Nested Loops
- Divisibility
- Brute Force
- Time Complexity Analysis

---

## Author

**Bharat Shishodia**

GitHub: *(Add your GitHub profile link here)*

LinkedIn: *(Add your LinkedIn profile link here)*