## Merging Intervals

### Background
At Berkeley Lights we have OptoSelect chips, which can have a varying number of pens. We identify pens using a simple index (pen 1, pen 2, etc). Sometimes, for example when exporting cells from a chip, the user would like to specify a set of pens to use. For convenience, we allow the user to specify pens using a special “syntax” (using commas and dashes) that allows a mix of individual pens and intervals: 
```
1,2-5,6,10-12,11-15
1-99,101,5000-5001
```
A user may not always define intervals in the most optimal way, so we need a way to take an arbitrary user input and generate a list of non- overlapping intervals. For example:
```
1-5, 2-10 1-10
```

### How to Run
Edit the input passed in the main method and run. The final list of non-overlapping intervals should be printed as output
Example
```angular2html
Input: 1-5, 2-10
Output: 1-10
```

### Test
Run the tests in **test_interval** file which cover various scenarios and verifies them against expected outputs


### Time Complexity
Assuming n as the total intervals in input list, the parse input step takes **O(n)** time, merge input step involves sorting in **O(nlog(n))** time and then a linear scan and merge in **O(n)**. Hence the overall time complexity is
```angular2html
O(nlog(n))
```

### Space Complexity
Space is consumed in the parse_input step where a list is created to contain items. The merge_intervals step will also take **O(n)** space. Hence the overall space complexity is:
```angular2html
O(n)
```