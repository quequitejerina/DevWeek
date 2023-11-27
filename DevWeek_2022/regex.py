import re

regex = (r"^.{9,11}$ \n"
	r"^\D+[1234]\D+[1234]\D+ \n"
	r"^.{4}[\._?].+$ \n"
	r"^..r\d.[A-Za-z]+3[a-z]$ \n"
	r"^.+[03].*u..$ \n"
	r"^[A-Q].{6}[lMN].+$ \n"
	r"^.((\d+)|(o\D)).{0,99}$ \n"
	r"^.{1,13}V.{1,13}$ \n"
	r"^[\w\d]+[!_][\w\d]+$ \n"
	r"^[Cc]{1,3}.{0,42}[sSZ]$ \n"
	r"^[\d\D]{11,14}$ \n"
	r"^.+a[^A-Z].{3}$")

test_str = ""

matches = re.finditer(regex, test_str, re.MULTILINE)
print(matches)

for matchNum, match in enumerate(matches, start=1):
    print(matchNum)
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
