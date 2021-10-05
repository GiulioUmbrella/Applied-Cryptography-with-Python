# Cryptography application
The goal is an implementation of cryptography operation .


## Evaluation

## Binary class
Perform the basic operation on an object composed of binary digits.

Big endian format.

### Constructor
The class receives in input as integer (assumed in base 10) and coverts in base 2. The class may also receives a list of 0 and 1 and use it as a

### Operations

* + : sum of two binary objects. The function is implemented bit by bit as the sum of three bits. The
* - : subtraction
* * : multiplication
* / : euclidian division

The following operation works similary. First, they check the number of digits. Then they go through the bit looking for differences.

* ==: equivalence
* > : first check the lenght
* >=:
* % : perform the division and return the reminder



## Phi class
Perform the Euler Phi function on an integer

## RSA class
Perform the operation of RSA cryptosystem


# BugFix
1. The length is fine with multiplication and addition, but it does not make sense for subtractions


# Implementation
* Product of sequence
* Modular product of sequence
* RSA toy example - from algebra cerruti
* Implement binary class for handling binary element
    * constructor
    * print function (override basic obj function )
    * override sum, product, quotient and subtraction
    *

# Test
* add class for unit testing
