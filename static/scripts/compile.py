import sys
import os
import shutil

def run(command):
	os.system(command)

path = os.path.join(os.path.dirname(__file__), "..", "iterations")
path = os.path.abspath(path)

print(path)

def downloadFile(url, path):
	os.system("curl -# '%s' | gzip -d > '%s'" % (url, path))

def processLines(pathA, pathB, p):

	with open(pathA, "r") as f:
		
		linesA = f.readlines()
		linesB = []

		for i in xrange(0, len(linesA)):
			linesB.append(p(i, linesA[i], linesA))

	with open(pathB, "w") as f:
		f.write("".join(linesB))


for fileName in os.listdir(path):
	
	filePath = os.path.join(path, fileName)

	if not filePath.endswith(".framer"):
		continue

	appCoffeePath = os.path.join(filePath, "app.coffee")
	appCoffeeTempPath = os.path.join(filePath, "app.tmp.coffee")
	appJSPath = os.path.join(filePath, "app.js")

	print "Compiling '%s'" % appCoffeePath

	# Convert coffee single line comments to block comments

	def isCommentLine(line):
		return line.strip().startswith("# ")

	def processCSLine(index, line, lines):

		try: lastLine = lines[index-1]
		except IndexError: lastLine = ""
		try: nextLine = lines[index+1]
		except IndexError: nextLine = ""
			
		if isCommentLine(line):
			
			# Single comment line
			if not isCommentLine(lastLine) and not isCommentLine(nextLine):
				return line.replace("# ", "### ").strip("\n") + " ###\n"

			# Start the block
			if not isCommentLine(lastLine):
				return line.replace("# ", "### ")

			# End the block
			if not isCommentLine(nextLine):
				return line.replace("# ", "").strip("\n") + " ###\n"

			return line.replace("# ", "")


		return line

	processLines(appCoffeePath, appCoffeeTempPath, processCSLine)

	run("/usr/local/bin/coffee -pbc --no-header '%s' > '%s'" % (
		appCoffeeTempPath, appJSPath))

	# Clean up a bunch of loose hanging */

	with open(appJSPath, "r") as f:
		data = f.read()

	data = data.replace("\n */", " */")
	data = data.replace("\n\n\n", "\n\n")

	with open(appJSPath, "w") as f:
		f.write(data)

	os.remove(appCoffeeTempPath) 

