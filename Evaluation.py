tablTheme = []
tablQuest = []
tablQCM = []
line = ""

def fetch():
    i = 0
    with open("questions.qs","r") as qs:
        for line in qs:
            line = line.rstrip()
            if line.startswith("##"):
                tablTheme.append(line)
                tablQuest.append("")
		print line
                i += 1
            elif line.startswith("#"):
                tablQuest.append(line)
                tablTheme.append("")
		print line
                i += 1
	    if line.startswith("-"):
		tablQCM.append(line)
		print line

	#print tablTheme
	#print tablQuest

fetch()

	
