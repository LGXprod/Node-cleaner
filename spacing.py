
def addSpaceBeforeBrace(file):
	textFile = ""

	for line in file:
		currentLine = list(line)
		lastChar = currentLine[(len(currentLine) - 2)]

		if lastChar == "{":
			currentLine.pop((len(currentLine) - 2))

			bracePos = getNewBracePos(currentLine)
			if (bracePos != -5):
				currentLine.insert(bracePos, " {")

			# print(currentLine)
			# textFile += "".join(map(str, currentLine))

			for x in currentLine:
				textFile += x
			# print(textFile)
		else:
			textFile += line
			# print(currentLine)

	# print(textFile)

	return textFile

def getNewBracePos(currentLine):
	if len(currentLine) > 3:
		for y in range((len(currentLine)-1), -1, -1):
			# closing parathesis completes conditional statement and > starts arrow function
			# typical convention is to a space after and then the opening brace in JS
			if currentLine[y] == ")" or  currentLine[y] == ">":	
				return (y+1)	
		return -5
	else:
		return -5

def addTabSpacing(file):
	print("")

def lineSpacing(file):
	textFile = ""

	lines = file.readlines()
	print(lines)

	for y in range(0, len(lines)-1):
		currentLine = lines[y]
		if len(currentLine) >= 2: # Stops index out of range error and disqualifies \n
			for char in currentLine:
				# print(char)
				if char == "{":
					if lines[y+1] != "\n":	
						lines.insert(y+1, "\n")
						break
				# elif char == "}":
				# 	if lines[y-1] != "\n":	
				# 		lines.insert(y-1, "\n")
				# 		break
	
	for line in lines:
		textFile += line

	print(textFile)
		
	# for y in range(0, len(file)):
	# 	print(line[len(line)-1])
	# 	# if line[len(line)-1] == "\n":