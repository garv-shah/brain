---
title: "Writing Pseudocode"
---

> [!info]
> 
> Write an algorithm in pseudocode to find the area of a shape from the list {square, rectangle, circle}. 
> 
> Consider what inputs would be required for each shape.

Begin AreaShape(Inputs: shapeType, d1, d2)
	Set Area to zero
	If (Shape is a square OR Shape is a rectangle) Then
		Area = d1 * d2
	Else if (Shape is a circle) Then
		Area = pi * d1 ^ 2
	Else
		Print "invalid shape"
	End If
	
	Print Area
End AreaShape

> [!info]
> 
> Design an algorithm to find all the common elements in two sorted lists of numbers. For example, for the list A {2,5,5,5} and list B {2,2,3,5,5,7} the output should be 2,5,5.  
> 
> Think about what is the maximum number of comparisons your algorithm makes if the lengths of the two given lists are _m_ and _n_, respectively?

Begin InCommon(Inputs: list1, list2)
	Set CommonList to empty
	
	Set list1_counter to 1
	Set list2_counter to 1
	
	Repeat until (counter for list1 is larger than list length OR counter for list2 is larger than list length)
		If (list1[list1_counter] is equal to list2[list2_counter]) Then
			add list1[list1_counter] to CommonList
			Increment both counters
		Else If (list1[list1_counter] < list2[list2_counter]) Then
			Increment list1_counter
		Else If (list1[list1_counter] > list2[list2_counter]) Then
			Increment list2_counter
		End If
	End Loop
	Return CommonList
End InCommon
