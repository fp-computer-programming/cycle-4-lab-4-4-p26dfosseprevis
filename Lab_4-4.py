#*** You must write a comment for every chunk of code you write from now on along with your author tag***
#Create a Python file named lab_4-4.py
#Use the find method to return the index of the first occurrence of the letter "t" in the word "flibbertigibbet".
word = "flibbertigibbet"
t = word.find("t")
print(t)
#Using this value, print the letter immediately following the first "t". hint: you may need to store the index value as a variable!
print(word[t + 1])
#Create a variable storing your first name written in lowercase. Using a string method, print this variable in uppercase.
name = "dylan"
print (name.swapcase())
#Use the split method to split the following sentence at each comma: "I wish, I wish, I was a fish."
fish = "I wish, I wish, I was a fish."
print(fish.split(","))