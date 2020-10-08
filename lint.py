import os, glob
pyfile = []
for file in glob.glob("*.py"):
	os.system("pylint"+ " " + file)
