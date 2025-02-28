## Task0

The dominant factor is reading both files into lists, which is O(N + M).
Accessing list elements is constant time O(1).
If N and M are large, the runtime depends mainly on file size.

## Task1
The dominant factor is reading both files into lists, which is O(N + M).
As we have to iterate over the elements to add them to the array we have here an O(n)
complexity. This could get optimized by using a set. With the set we ensure that an elements
cannot get added twice to the structure. By using a set, the time complexity is 0(1) as we dont
have to proof that the the number is not already in the array list. 

## Task2

Here we have a time complexity of O(N+M) so O(N) as we iterate through all elements once and 
safe the longest duration in seconds in a dict structure. 

## Task3

Of course we have again the time complexity of 0(N+M) for the files. Then we have again the situation
where iterate over the calls to extract the the calls we are looking for. Here we are again in the 
O(N) situation. Finally we need to apply a sorting to the extracted numbers. Here we have a complexity of
O(M log M) as we apply here a sort algorithm of the values found.

## Task4

O(N + M + K) (for storing texts, calls, and unique numbers)

