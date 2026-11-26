# Algorithms.python
	This is a personal educational project to learn logics, algorithms and programming. Overall I am interested in understand how algorithms works, taking into account its limits and possibilities. For that reason, you will find verification algorithms as prime verification, biyective function verification or wff PL verification.
	The use of the different algorithms is free and you can use as you want. Also I thanks all the commentaries and possible feedback.

## Objetives

- Learn Python(functions, definition)
- Understand effective algorithms (making algorithms and explore his limits)
- Create algorithms see useful(As compound interest)
- See Python limits (as float python problem)

## Method

I am studying the book "An introduction to Gödel's Theorems" by Peter Smith and I am doing the excercies that the author present in "www.logicmatters.net". From the algorithms excercies I translate some of then to Python. I also ask to ChatGPT to guide me in my problems and also it explain to me the most relevant python tools that I can use.

## What can you find in the repository?

You will find scripts around:

### 1.Logics:
- algfbf.py :here there are some functions to decide wheather a formula is wf or not. This algorithm is incomplete and present some errors.
- esbiyectiva.py : here there are three different functions: (es_sobreyectiva(imag, codom), es_inyectiva(imagenes) and es_biyectiva(imag,codom)). es_sobreyectiva verify if one function is surjective putting as arguments the list of images and codominiums.es_inyectiva verify if one functioin is injective putting as arguments the list of images from the fontion. es_biyectiva verify if one function is surjective and injective.

### 2.Maths:
- algoritmoprime.py : define the function esprimo(n) and verify if one number is prime.
- algoritmoeucl.py : define the function eucl(a,b) and define the greatest common divisor of two numbers applying the Euclide's algorithm.
- algenumber.py : here I define two algorithms to calculate the e number giving the number of operations you want to do over n (For that you have incr(n) to explore the method of limits(that is (1+1/n)**n) or taylor(n)to explore the method of taylor(that is 1+1/2!+1/3!...1/n!)). Also you have ecalc(m,n,o,n) where you can see how to aproximate to e calculating values in exponential or sum increasing. Also that algorithm present a error verification taking the e provided from math library. You have also a factorial calculation algorithm called fact(n). Finally there are two algorithms that explore the python limits of that calculation, and you can find the exact moment the calculation fails. Also you can compare both with camparalimcontay(n,m).

### 3.Encoding:

- algcodificar.py : define one biyective function codificar(m,n) that encode one pair of numbers in one single one. Also from the result you can find that original pairs with fst(k), snd(k) and decodificar(k).

- algenumerarpares.py : makes the same than alcodificar but it use other method. The interest of that method is that is banch the pairs in groups of sums, that is 1.(0,0), 2,3 as (1,0) and (0,1), 4,5,6 as (2,0), (1,1), (0,2)... Also you can visualize that order with the function dib_zigzag1(diagonales) and dib_zigzag2(diagonales) where you can se that distribution in the console. 

### 4.Finance Algorithms:

- algintcompuesto.py : is a simple algorithms where you can canculate the compund interest. There is algint(x,i,n) where x is the initial ammount, i the interest and n the number of times you will receive that interest. algint_masm(x,i,n,m) does the same thing but adding some ammount more each time.
