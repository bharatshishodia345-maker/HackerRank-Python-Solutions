# Breaking the Records

## Problem Statement

Maria plays basketball and records her score in every game. The first game's score becomes both her highest and lowest record.

For every following game:

- If the score is greater than her current highest score, the highest record is broken.
- If the score is lower than her current lowest score, the lowest record is broken.

The task is to determine how many times Maria breaks her highest and lowest records during the season.

---

## Requirements

- Read the scores of all games.
- Consider the first score as both the highest and lowest record.
- Traverse the remaining scores one by one.
- Count:
  - Number of times the highest record is broken.
  - Number of times the lowest record is broken.
- Return both counts.

---

## Approach

1. Initialize the first score as both the highest and lowest record.
2. Create two counters:
   - Highest Record Break Count
   - Lowest Record Break Count
3. Iterate through the remaining scores.
4. If a score is greater than the current highest record:
   - Update the highest record.
   - Increment the highest counter.
5. If a score is lower than the current lowest record:
   - Update the lowest record.
   - Increment the lowest counter.
6. Return both counters.

---

## Time Complexity

**O(n)**

The list of scores is traversed only once.

---

## Space Complexity

**O(1)**

Only a few extra variables are used regardless of input size.

---

## Example

Input

```
9
10 5 20 20 4 5 2 25 1
```

Output

```
2 4
```

---

## Language

- Python 3