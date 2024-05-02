word=str(input("Enter the word: "))
letter=str(input("Check the repetition of a letter: "))
output=0
for i in word:
	if(i==letter):
	     output=output+1
print(output)	     
