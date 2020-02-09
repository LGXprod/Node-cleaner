
def addSpaceBeforeBrace(file):
	textFile = ""

	for line in file:
		currentLine = list(line)
		lastChar = currentLine[(len(currentLine) - 2)]

		if lastChar == "{":
			currentLine.pop((len(currentLine) - 2))
			for y in range((len(currentLine)-3), -1, -1):
				if currentLine[y] == ")" or  currentLine[y] == ">":		
					currentLine[y+1] = " {\n"
			# print(currentLine)
			textFile += "".join(map(str, currentLine))
		else:
			textFile += line
			# print(currentLine)

	print(textFile)

	return textFile

def addTabSpacing(file):
	print("")

def lineSpacing(file):
	print("")