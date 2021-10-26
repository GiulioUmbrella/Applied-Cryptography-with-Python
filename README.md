# Applied cryptography with python

## Goals

## Binary class
The binary class is a wrapper for the all the binary operations. It overloads the standard math symbol (e.g., '+') for higher clarity. The class has two fields:
1. abs_value: a binary representation of the absolute value of an integer
2. sign: the bit sign (+1 or -1)

The zero value has a +1 sign.

All the operations are performed calling methods of the signed_binary module.

## Binary signed ops
This module handles all the sign-related operations and delegates the computation to the binary_ops module.

The functions return two values:
1. The absolute value in base two
2. The sign of the result.

1. Multiplication: perform the absolute product of the operand and then assigns the sign.

2. Division: like the multiplication.

3. Addition: the addition has two cases.
    1. The operands have the same sign: perform the sum of the absolute values and assigns the common sign.
    Eg 2+2 = 4, -2-2 = 4
    2. The operands have different signs. In this case, the function identifies the operands with grater absolute value and performs the subtraction, then it chooses the right sign to return.

To ensure a coherent representation of the zero, the functions check if the value is zero and set the sign to one.

## Binary ops
Lower level operation
For addition and multiplication, the module assumes that both values are positive. For the subtraction, the module assumes that the RHT is smaller than the LRT.  

* Addition: without lose of generality, I assume one of the addends to be bigger than the other. The sum is performed summing two bits in the same position and the carry from the previous result (with a zero initial carry). The operation can be executed with a look-up table with in input the two addends and the carry as key. The output value is the sum of the two bits and the carry. If the final carry is one, append a one to the final result.

* Multiplication: also for the multiplication, I assume one of the two operands to be bigger than the other. First, I produce a list of the value than will be summed. For each operations I increase the number of shifts

* Subtraction:
In the subtraction, I assume a value to be bigger than the other.


* Euclidian Division
The division produces a quotient and a reminder. 

* Power: the power uses the square and multiply techniques, using the partial products to
