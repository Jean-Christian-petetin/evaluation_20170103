tablTheme = []
tablQuest = []
tablQcm = []
tablRep = []
line = ""

subStrHash = "##"
subStrHash2 = "#"
subStrMinus = "-"

def affichQuestion():
	i = 0
	with open("questions.qs","r") as qs:
		for line in qs:
			line = line.rstrip()
			#if line.startswith("##"):
			if line.count(subStrHash):
				tablTheme.append(line)
				tablQuest.append("")
				tablQcm.append("")
				print line
		        	i += 1		
		    	#elif line.startswith("#"):
			elif line.count(subStrHash2):
				tablTheme.append("")
				tablQuest.append(line)
				tablQcm.append("")
				print line
				i += 1
		    	#elif line.startswith("-"):
			elif line.count(subStrMinus):
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

def aRefaire():
	i = 0
	with open("questions.qs","r") as qs:
		for line in qs:
			line = line.rstrip()
			if line.count(subStrHash):
				tablRep.append("")
				i += 1
			elif line.count(subStrHash2):
				tablRep.append(raw_input(""))
				i += 1
			elif line.startswith("-"):
				i += 1
				tablRep.append("")
		print tablRep

affichQuestion()
