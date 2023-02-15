This program finds an arithmetic expression by a bottom up approach that query over the positive integers
with addition, multiplication, subtraction, and integer division.
This supports input-output pairs such as 4 maps to 8, and synthesize the function 4 + 4 = 8 (as one example).

For each input, this would generate new functions by appending one operation to the input,
use conditional inference to eliminate functional equivalent functions (expression that results to the same value),
pick better functions among equivalence, and repeat this up to MAX_FUNCTION_DEPTH to give a good function.
Priority given to shorter expressions.

This will first print all valid functions this program found (for demonstration purpose)
then print one function it picked through the equivalence comparison.


An example output:

Please enter two numbers separated by a space, in the format of 'input output'
1000 20
Printing possible expressions
(((1000*0)+4)*5)　=　20
(((1000*0)+5)*4)　=　20
(((1000/2)/5)/5)　=　20.0
(((1000/5)/5)/2)　=　20.0
(((1000/5)/8)-5)　=　20.0
(((1000/8)-5)/6)　=　20.0
(((1000*0)+4)*5)　=　20
(((1000*0)+4)*5)　=　20
(((1000*0)+5)*4)　=　20
(((1000/2)/5)/5)　=　20.0
(((1000/5)/5)/2)　=　20.0
(((1000/5)/8)-5)　=　20.0
(((1000/8)-5)/6)　=　20.0
((((1000*0)+1)+9)*2)　=　20
((((1000*0)+2)*6)+8)　=　20
((((1000*0)+2)*7)+6)　=　20
((((1000*0)+2)*8)+4)　=　20
((((1000*0)+2)+9)+9)　=　20
((((1000*0)+2)*9)+2)　=　20
((((1000*0)+3)*5)+5)　=　20
((((1000*0)+3)*7)-1)　=　20
((((1000*0)+3)*8)-4)　=　20
((((1000*0)+3)*9)-7)　=　20
((((1000*0)+4)*5)*1)　=　20
((((1000*0)+4)*5)/1)　=　20.0
((((1000*0)+4)*7)-8)　=　20
((((1000*0)+4)+9)+7)　=　20
((((1000*0)+8)+9)+3)　=　20
((((1000+1)/7)-3)/7)　=　20.0
((((1000+2)/6)-7)/8)　=　20.0
((((1000*2)/5)/5)/4)　=　20.0
((((1000/5)-2)/9)-2)　=　20.0
((((1000/5)+3)/7)-9)　=　20.0
((((1000/5)+7)/9)-3)　=　20.0
((((1000/5)+8)/8)-6)　=　20.0
((((1000/5)/8)-6)+1)　=　20.0
((((1000/8)-5)/2)/3)　=　20.0
Printing a good expression
(((1000*0)+4)*5)　=　20.0