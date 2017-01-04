tablTheme = []
tablQuest = []
tablQcm = []
tablRep = []
line = ""

def fetch():
	i = 0
	with open("questions.qs","r") as qs:
		for line in qs:
			line = line.rstrip()
			if line.startswith("##"):
				tablTheme.append(line)
				tablQuest.append("")
				tablQcm.append("")
				print line
		        	i += 1		
		    	elif line.startswith("#"):
				tablTheme.append("")
				tablQuest.append(line)
				tablQcm.append("")
				print line
				i += 1
		    	elif line.startswith("-"):
				if i-1 < len(tablQcm):
					j = i-1
					if tablQuest[j] != "" and tablQcm[j] == "":
						tablQcm[j] = line
						print tablQcm[j]
					else:
						tablTheme.append("")
						tablQuest.append("")
						tablQcm.append(line)
						print tablQcm[i]
						i += 1
				else:
					tablTheme.append("")
					tablQuest.append("")
					tablQcm.append(line)
					print tablQcm[i]
					i += 1

fetch()
