# Time Conversion

## Problem

Given a time in 12-hour AM/PM format, convert it into 24-hour military time.

## Example

Input:

```text
07:05:45PM

## Output:

19:05:45

Approach
Extract the first two characters as the hour.
Extract the last two characters to determine AM or PM.
For 12 AM, convert the hour to 00.
For PM values except 12 PM, add 12 to the hour.
Keep the minutes and seconds unchanged.
Format the hour using two digits.
Concepts Used
String slicing
int() conversion
Conditional statements
f-string formatting
12-hour to 24-hour time conversion
Time Complexity

O(1)

Space Complexity

O(1)