import semicolons
import spacing

fileName = "test.js"

oldFile = open(fileName, "r")
# spacing.addSpaceBeforeBrace(oldFile)
spacing.lineSpacing(oldFile)

newFile = open("new"+fileName, "w")
newFile.write(semicolons.addSemicolons(oldFile))

newFile.close()