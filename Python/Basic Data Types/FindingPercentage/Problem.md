### Problem Statement

The provided code stub will read in a dictionary containing key/value pairs of `name:[marks]` for a list of students.  
Print the average of the marks array for the student name provided, **showing 2 places after the decimal**.

---

#### Example

Input:
3
alpha 20 30 40
beta 50 50 50
gamma 70 80 90
beta

Output:

The `query_name` is `'beta'`. Beta's average score is `50.00`.

---

### Input Format

- The first line contains the integer `n`, the number of students' records.  
- The next `n` lines contain the names and marks obtained by a student, each value separated by a space.  
- The final line contains `query_name`, the name of a student to query.

---

### Constraints

- `2 <= n <= 10`  
- `0 <= marks[i] <= 100`  
- Length of marks array is `3`

---

### Output Format

Print one line: The average of the marks obtained by the particular student **correct to 2 decimal places**.
