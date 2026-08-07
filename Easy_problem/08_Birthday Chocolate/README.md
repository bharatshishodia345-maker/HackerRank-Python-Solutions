# Birthday Chocolate (Subarray Division)

## Problem Statement

Lily wants to share a chocolate bar with Ron.

Each chocolate square contains an integer.

Find the number of contiguous segments such that:

- The length of the segment is equal to Ron's birth month (m).
- The sum of the integers in that segment is equal to Ron's birth day (d).

Return the total number of valid segments.

---

## Requirements

- Input an array representing the chocolate bar.
- Consider only contiguous segments.
- Each segment must have exactly **m** elements.
- The sum of the segment must be equal to **d**.
- Return the total number of valid segments.

---

## Approach

1. Traverse every possible starting index.
2. Extract a contiguous segment of length **m**.
3. Calculate the sum of that segment.
4. If the sum equals **d**, increment the counter.
5. Return the final count.

---

## Algorithm

1. Initialize `count = 0`.
2. Loop from index `0` to `len(s) - m`.
3. Calculate the sum of `m` consecutive elements.
4. If the sum equals `d`, increase the count.
5. Return the count.

---

## Time Complexity

**O((n - m + 1) × m)**

Each window of size **m** is summed independently.

---

## Space Complexity

**O(1)**

Only a few extra variables are used.

---

## Example

### Input

```
5
1 2 1 3 2
3 2
```

### Output

```
2
```

---

## Language

- Python 3