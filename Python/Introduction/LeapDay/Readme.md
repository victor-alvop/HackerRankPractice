## Leap Year Determination

An extra day is added to the calendar almost every four years as February 29, and the day is called a **leap day**. It corrects the calendar for the fact that our planet takes approximately **365.25 days** to orbit the sun. A **leap year** contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

1. The year **can be evenly divided by 4**, is a leap year, **unless**:
2. The year **can be evenly divided by 100**, it is **NOT** a leap year, **unless**:
3. The year is also **evenly divisible by 400**. Then it **is** a leap year.

This means that in the Gregorian calendar:
- The years **2000** and **2400** are leap years.
- The years **1800**, **1900**, **2100**, **2200**, **2300** and **2500** are **NOT** leap years.  
[Source](https://en.wikipedia.org/wiki/Leap_year)

---

## Task

Given a year, determine whether it is a leap year.  
If it **is** a leap year, return the Boolean **`True`**.  
Otherwise, return **`False`**.

> Note: The code stub provided reads from STDIN and passes arguments to the `is_leap` function. You only need to complete the `is_leap` function.

---

## Input Format

Read `year`, the year to test.

---

## Constraints

- `1900 <= year <= 10^5`

---

## Output Format

The function must return a Boolean value: **`True`** if the year is a leap year, **`False`** otherwise.  
Output is handled by the provided code stub.

---

## Sample Input 0
