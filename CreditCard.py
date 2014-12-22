#  File: CreditCard.py

#  Description:Luhn's Test

#  Student Name:Evan Johnston

#  Student UT EID:eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created:9/22/13

#  Date Last Modified:9/22/13
def main():
	cc=int(input("Enter 16-digit credit card number: "))

	d16=cc%10

	n16_cc=cc//10
	d15=n16_cc%10

	n15_cc=n16_cc//10
	d14=n15_cc%10

	n14_cc=n15_cc//10
	d13=n14_cc%10

	n13_cc=n14_cc//10
	d12=n13_cc%10

	n12_cc=n13_cc//10
	d11=n12_cc%10

	n11_cc=n12_cc//10
	d10=n11_cc%10

	n10_cc=n11_cc//10
	d09=n10_cc%10

	n09_cc=n10_cc//10
	d08=n09_cc%10

	n08_cc=n09_cc//10
	d07=n08_cc%10

	n07_cc=n08_cc//10
	d06=n07_cc%10

	n06_cc=n07_cc//10
	d05=n06_cc%10

	n05_cc=n06_cc//10
	d04=n05_cc%10

	n04_cc=n05_cc//10
	d03=n04_cc%10

	n03_cc=n04_cc//10
	d02=n03_cc%10

	n02_cc=n03_cc//10
	d01=n02_cc%10

	#above section sets d01-d16 to each digit of cc

	d15a=d15*2
	d13a=d13*2
	d11a=d11*2
	d09a=d09*2
	d07a=d07*2
	d05a=d05*2
	d03a=d03*2
	d01a=d01*2

	#above section sets d01a-d15a to odd digits of cc * 2

	d15b=d15a%10
	d13b=d13a%10
	d11b=d11a%10
	d09b=d09a%10
	d07b=d07a%10
	d05b=d05a%10
	d03b=d03a%10
	d01b=d01a%10

	#above section sets d01b-d15b to 1st digit of the odd digits *2

	d15c=d15a//10
	d13c=d13a//10
	d11c=d11a//10
	d09c=d09a//10
	d07c=d07a//10
	d05c=d05a//10
	d03c=d03a//10
	d01c=d01a//10

	#above section sets d01c-d15c to 2nd digit of the odd digits *2

	d15d=d15b+d15c
	d13d=d13b+d13c
	d11d=d11b+d11c
	d09d=d09b+d09c
	d07d=d07b+d07c
	d05d=d05b+d05c
	d03d=d03b+d03c
	d01d=d01b+d01c

	#above section sets d01d-d15d to sum of odd digits *2

	sum=d01d+d03d+d05d+d07d+d09d+d11d+d13d+d15d+\
	d02+d04+d06+d08+d10+d12+d14+d16

	#above section sets sum to the sum of all digits collected

	if sum%10==0: print ("Valid credit card number")
	else: print ("Invalid credit card number")

	#above section is a conditional return of the validity of the cc based on Luhn's Test
main()

