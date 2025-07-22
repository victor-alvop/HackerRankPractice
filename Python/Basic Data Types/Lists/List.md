## 🧪 HackerRank - List Operations

### 💬 Description

You are given a list: `my_list = []`.  
You will receive **N** commands to manipulate this list. The available commands are:

- `insert i e`: Insert integer `e` at position `i`.
- `print`: Print the list.
- `remove e`: Delete the first occurrence of integer `e`.
- `append e`: Append integer `e` at the end of the list.
- `sort`: Sort the list in ascending order.
- `pop`: Remove the last element from the list.
- `reverse`: Reverse the list.

### 🧾 Input Format

- The first line contains an integer **N**, the number of commands.
- The next **N** lines contain one of the above commands.

### ✅ Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 10
append 9
append 1
sort
print
pop
reverse
print


### 🖨️ Sample Output

[6, 5, 10]
[1, 5, 6, 9]
[9, 6, 5, 1]