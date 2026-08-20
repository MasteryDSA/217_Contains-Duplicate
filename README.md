# LeetCode: 217. Contains Duplicate
### Problem Description
Given an integer array nums return true if any value appears at least twice in the array, and return false if every element is distinct.


#### Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.


#### Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.


#### Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


## Algorithm Explanation

My solution checks for duplicates by comparing the length of the original list with the length of a set made from that list.

1. Get the length of the original list using `len(nums)`.
2. Convert the list into a set using `set(nums)`. A set only keeps unique elements.
3. Get the length of the set.
4. Compare the two lengths:

   * If they are the same, there are no duplicates.
   * If the set is shorter, there is a duplicate.
5. Return `True` if a duplicate exists and `False` if there are no duplicates.

### Example

```python
nums = [1, 2, 3, 1]

len(nums)       # 4
len(set(nums))  # 3
```

Since the lengths are different, the list contains a duplicate.

### Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

### Why I Chose This Approach

I chose the length-check approach because it is **simple and easy to understand**. I only need to convert the list into a set and compare the two lengths to know if duplicates exist.

There is also another approach using a `seen` set:

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)

return False
```

I would also recommend the `seen` approach because it checks the numbers one by one and can **return immediately when it finds a duplicate**.

However, I still chose the length-check approach for this solution because I wanted to practice and demonstrate the basic idea of using a **set to remove duplicates and comparing lengths**. Both approaches have O(n) average time complexity and O(n) space complexity.
