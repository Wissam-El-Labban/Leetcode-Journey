This is a pattern that is used to query the SUM of elements in a sub-array.

While you can search for the sum of two elements of an array using a single query that would require your program to search in linear time, using multiple queries would require an O(n*m) time complexity where m is the number of queries, and n is the length of the array.

The main idea behind the prefix sum array is that you will make an array that is derived from the original array and then have each element as a sum of all elements that came before it in addition to the original value of the element itself. 

Array = [1, 2, 3, 4, 5, 6, 7]
Prefix-sum = [1, 3, 6, 10, 15, 21, 28]

P[i] = A[0] + A[1] + ... A[i]

With this technique we can answer the sum of two indexes using a simple expression below without having to do any searches.

SUM[i, j] = P[j] - P[i-1]

There are times when a new array may not be needed and you can use an input array to avoid using extra space.

We need to exclude the sum of the elements before the left index hence why we subtract it by 1 or initialize it to 0 if it is the first most index.



