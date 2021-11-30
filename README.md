## lagou

### 数据结构与算法面试宝典

#### 栈

## LeetCode

### 0016

#### 题目

数组中选出三个数, 他们的和最接近指定值.

#### 解题思路

### 0021

#### 题目

两个有序链表合并.

#### 解题思路

归并排序的思想. 注意哨兵以及循环判定条件:

- `while node.next`
- `while node`


### 0415

#### 题目

数字的字符串相加

#### 解题思路

模拟计算的过程.
- 注意循环条件
- 注意算上进位
- 在其他语言中, 字符转化为数字如'1'的值为49, 因此最好的做法是`int(c - '0')`
- Go中转化10进制的数字为字符的方法为`strconv.Itoa(result%10)`
- python的append的效率比insert高
