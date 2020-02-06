def addSemicolons(file):
	for line in file:
		currentLine = list(line)
		print(currentLine)
		if currentLine[len(currentLine) - 1] != "{" or currentLine[len(currentLine) - 1] != "}":
			print("good")

addSemicolons(open("test.js", "r"))