## Task0

The dominant factor is reading both files into lists, which is O(N + M).
Accessing list elements is constant time O(1). If N and M are large, the runtime depends mainly on file size.
Taking into account the reading files and accessing the list the complexity is O(N)

## Task1
The dominant factor is reading both files into lists, which is O(N + M).
As we have to iterate over the elements to add them to the array we have here an O(N)
complexity. This could get optimized by using a set. With the set we ensure that an elements
cannot get added twice to the structure. By using a set, the time complexity is 0(1) as we dont
have to proof that the the number is not already in the array list. So the overall approximation here
is O(N)

## Task2

Here we have a time complexity of O(N+M) so O(N) as we iterate through all elements once and 
safe the longest duration in seconds in a dict structure. 

## Task3

Of course we have again the time complexity of 0(N+M) for the files. Then we have again the situation
where iterate over the calls to extract the the calls we are looking for. Here we are again in the 
O(N) situation. Finally we need to apply a sorting to the extracted numbers. Here we have a complexity of
O(NlogN) as we apply here a sort algorithm of the values found. In general the time complexity can get
approximated to O(NlogN).

## Task4

of course here again we have the complexity for the files O(n+m). The subsequent iterations follow into an O(n)
complexity. For the checking of the telemarketeers we are again in an 0(n) complexity. Sorting and printing then
leads to an O(n log n) time complexity. The final complexity approximation can then be identified as
o(n log n + m) 

