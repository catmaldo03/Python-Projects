print("Hello!")
print("This program analyzes the amount of word,characters and lines in a text file")
print("Please enter the name of the file you would like to analyze")
textname = input()
textfile = open(textname, "r")
lines = 0
words = 0
characters = 0
for line in textfile:
    lines += 1
    words += len(line.split())
    characters += len(line)
textfile.close()
print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)