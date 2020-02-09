def addSemicolons(file):
	textFile = ""

	for line in file:
		currentLine = list(line)
		# print(currentLine)

		for y in range(0, len(currentLine) - 1):
			if currentLine[y] != " ":
				firstChar = currentLine[y]
				break

		if firstChar == "+":
			textFile = textFile[:-2] + "\n"
			# print(textFile)

		lastChar = ""

		if len(currentLine) > 1:
			lastChar = currentLine[(len(currentLine) - 2)]
		else:
			lastChar = currentLine[0]
		
		if lastChar != "{" and lastChar != "}" and lastChar != ";" and lastChar != "\n" and lastChar != "+":
			for y in range(0, len(currentLine) - 1):
				textFile += currentLine[y]
			textFile += ";\n"
		else:
			textFile += line

		firstChar = ""

	# print(textFile)
	return textFile

def removeSemicolons(file):
	print("")