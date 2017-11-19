# Python3

Laboratory Project 3
Project on Binomial and Poisson Distributions


1.	Experimental Bernoulli Trials
Introduction: Simulation of the rolling of three dice 1000 times and the random variable X is the number of the count of get “three SIX” in 10000 experiment. Count one success if there were three six showed up in one experiment. 
Methodology: The methodology I used is generate three random numbers from 1 to 6. Whenever the random generator generates 6 count increase. When the count increased to 3 then all the experiment success.

Result: get the probability of P(success).
 











2.	Calculations using the Binomial Distribution

Introduction: simulate the rolling of the three dice 1000 times using formula for the Binomial distribution to calculate the probability distribution for the random variables X.
Methodology: With the probability of success p and probability of failure q = 1-p. Repeat rolling dice 1000 times. From the experiments will get Bernoulli trials and use Binomial formula, to the plot obtained from the 1000 experiments in Problem 1.

Conclusion: Plotted in the same scale to easy compare the plot from problem 1. Not much differences.
Result:	
 




3.	Approximation of Binomial by Poisson Distribution

Introduction: Simulate the rolling of the three dice 1000 times using formula for the occurrence of a particular event during a time interval that has duration one unit of time. Count of time the event has occurred during the interval. The occurrences are independent of each other and the event occurs at an average rate of parameter λ times per unit of time.
Methodology: This experiment is considered large amount of n trials which is 1000 that greater or equal to 50 and the np is less or equal 5. Therefore, with Poisson distribution formula p(X=x) = λ^x *e^(- λ) / x!  to the plot obtained from the 1000 experiments in Problem 1.


Conclusion:  Plotted in the same scale to easy compare the plot from problem 1. Not much differences.
Result: 
 

