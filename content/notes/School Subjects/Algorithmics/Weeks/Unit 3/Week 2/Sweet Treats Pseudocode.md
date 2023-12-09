---
title: Sweet Treats Pseudocode
---

> [!info]
> 
> Complete the following algorithm using pseudocode to instruct the factory’s robotic arm to sort the sweets into their individual colour buckets so that the packing process can begin.  

Begin sorting  
	While sweet in tub  
		Grab sweet  
		Check sweet colour  
		If colour = pink  
			Then place the sweet bucket  
		Else if colour = green  
			Then place in the green bucket  
		Else if colour = purple  
			Then place in the purple bucket  
		Else if colour = orange  
			Then place in the orange bucket 
		Else if colour = yellow
			Then place in the yellow bucket
	End While  
End sorting

> [!info]
> 
> Extend upon the algorithm you developed in Exercise 1 to allow the program to count the total number of sweets sorted and the quantity of each colour placed into the individual buckets.

Begin sorting  
	Set total sweets to zero
	Set pink, green, purple and yellow to zero
	While sweet in tub  
		Grab sweet  
		Add 1 to total sweets
		Check sweet colour  
		If colour = pink  
			Then place the sweet bucket 
			Add 1 to pink count 
		Else if colour = green  
			Then place in the green bucket 
			Add 1 to green count  
		Else if colour = purple  
			Then place in the purple bucket  
			Add 1 to purple count 
		Else if colour = orange  
			Then place in the orange bucket 
			Add 1 to orange count 
		Else if colour = yellow
			Then place in the yellow bucket
			Add 1 to yellow count 
	End While  
End sorting

> [!info]
> 
> On a scale of 1 to 10, how likely are you to use pseudocode to help you design your next program? Justify your response.

Probably like a 2, since typing in a hybrid language is generally not too useful in terms of time, since the in languages where the syntax is simple (like Python), pseudocode is almost equivalent to the syntax.