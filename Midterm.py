# Kristin Goselin
# Midterm - 3/20/19
import re
import sys
import string

spr = "*****************************************"
file = open('ALevel.java', mode='r')
readCode = file.read()

# finding the class statements and then removing them with regex
br = re.findall(
r'class\s+[A-Za-z]+({)\s*[\w\s(\[\]\)\{\}\/=\.;"?+<>,*]+(\})(\s+class\s+[A-Za-z]+({)\s*[\w\s(\[\]\)\{\}\/=\.;"?+<>,*]+(\}))*',
    readCode)

if not br:
    print("Something went wrong, please make sure your class brackets are formatted correctly.")

Cclass = re.compile(r'class\s+[\w]*{')
Bclass = re.compile(r'class\s+[A-Za-z]+{\n')



if not Bclass.search(readCode) and Cclass.search(readCode):
    print("Something went wrong, check your class declaration.")
    sys.exit();

if Bclass.search(readCode):
    noClass = Bclass.sub("", readCode)

else:
    print("Something went wrong, check your class declaration.")
    sys.exit();
print(spr)

# comments regex
comm = re.compile(r'(\/\*\s+[a-zA-Z\s\-\,\.]*\*\/)')
# one line comment regex
oneComm = re.compile(r'(\/{2}[\w\s\!]*$)', re.MULTILINE)
# multiline comments
if comm.search(noClass):
# without comments
    woComm = comm.sub(" ", noClass, count=2)
# single line comments
if oneComm.search(woComm):
    noComm = oneComm.sub("", woComm, count=2)
print(spr)

#Getting rid of spaces
nospace = re.compile(r'(\s{2,})')

if nospace.search(woComm, oneComm):
    oneComm = nospace.sub("",woComm)



# using regex to find and get rid of the imports
impoState = re.compile(r'import\s+java\.(io.\*|util.Scanner|text.\*|awt.\*|util.regex.\*);', re.MULTILINE)

impoCheck = re.compile(r'import\s+[\w.*]*;?')

if not impoState.search(oneComm) and impoCheck.search(oneComm):
    print("Something went wrong, check your import statements.")
    print(impoCheck.findall(oneComm))
    sys.exit()

if impoState.search(oneComm):
    noImpo = impoState.sub("", oneComm)

print(spr)

# Using regex to find and remove the last bracket
publicStatic = re.compile(r'public\s+static\s+void\s+main\s+(\(String\s+\[\]\s+arg(s|ss)\)\{)')
check = re.compile(r'public\s*sta(\w+)\s*\w*\s*\w*\s*[\(\w\s\[\]\)]*\{*')

if not publicStatic.search(noImport) and check.search(noImport):
    print("Something went wrong, check your public static statements.")
    sys.exit()

if publicStatic.search(noImport):
    nopublic = publicStatic.sub("", noImport)

print(spr)

# Finding and removing string declarations
string = re.compile(r'(public\s+|private\s+)*String\s+([A-Za-z]*)(\s*\=\s*(\"([A-Za-z\s+])*\"|sc\.next\(\)))*;')
check1 = re.compile(r'(public\s+|private\s+)*St\w+\s*\w+[\w=\s".()]*;?')

if not string.search(nopublic) and check1.search(nopublic):
    print("Something went wrong, check your strings.")
    sys.exit()

if string.search(nopublic):
    nostrings = string.sub("", nopublic)


print(spr)

# Finding and removing variables
numregex = re.compile(
    r'(public\s+|private\s+)*int\s+[\w]*(;|\s*\=[\s.\w\(\)]*;)')
numcheck = re.compile(r'(public\s+|private\s+)*(?<![rlo\s])i\w+\s+\w+(?![p,])\s*(;|\=?\s*\w+.\w+\(?\)?;|\=\s+\d;)*')

boolregex = re.compile(r'(public\s+|private\s+)*boolean\s+\w+\s*(;|=\s?(false|true);)')
boolcheck = re.compile(r'(public\s+|private\s+)*bo\w+\s+\w([=\s\w])*;?')

if numcheck.search(nostrings) and not numregex.search(nostrings):
    print("Something went wrong, check your int declaration statements")
    sys.exit()
else:
    nonum = numregex.sub("", nostrings)

if not boolregex.search(nonums) and boolcheck.search(nonums):
    print("Something went wrong, check your boolean declaration statements")
    sys.exit()

if boolregex.search(nonums):
    nobool = boolregex.sub("", nonums)


print(spr)

# Finding and removing any system.out.prints
sysregex = re.compile(
    r'System.out.print(ln)?\((\"[\w\s?<+>=.]+\"(\s*\+\s*\w+)*(\s*\+\s*\"\s*[\w\s]+\")?)?(\s*\+\s*\w+)?(\w\+\w)?(\s*\+\s*\"\s*[\w\s?<+>=.]+\")?\);')
check2 = re.compile(
    r'Sy\w+\.\w+\.?\w+\(?\"?[\w\s?.<>=+]+\"?\s*\+*\s*[\w\s]*\+*\s*\"*[\w\s?.<>=+]*\"*\s*\+*\s*[\w\s]*\+*\s*\"*[\w\s?.<>=+]*\"*\)?;?')

if check2.search(nobool) and not sysregex.search(nobool):
    print("Something went wrong, check your System output statements")
    sys.exit()

if sysregex.search(nobool):
    nosys = sysregex.sub("", nobool)

print(spr)


# Finding and removing assignment statements
scan = re.compile(r'Scanner\s+(\w)+\s*\=\s*new\s+Scanner\(System\.in\);')
scancheck = re.compile(r'Sc\w+\s+\w+\s*[=\s\w]+\(?\w*\.?\w*\)?;?')
assign = re.compile(r'\w+\s*=\s*[\w\s\+\-\/\*\%\.\(\)]*;')

if not scan.search(nosys) and scancheck.search(nosys):
    print("Something went wrong, check your Scanner declarations")
    sys.exit()

if scan.search(nosys):
    noscan = scan.sub("", nosys)

if assign.search(noscan):
    noassign = assign.sub("", noscan)


print(spr)

# Finding and removing while statements
whregex = re.compile(r'while(\([A-Za-z]+\s*[<=>!]+\s*[0-9A-Za-z]+\)){([A-Za-z.()"\s+-\/?;]*)}')
check3 = re.compile(r'wh\w+\s*\(?[\w\s<=>\/]+\)?{?[A-Za-z.()"\s+-\/?;]?}?')

if not whregex.search(noassign) and check3.search(noassign):
    print("Something went wrong, check your while loop declarations")
    sys.exit()

if whregex.search(noassign):
    nowh = whregex.sub("", noassign)


print(spr)

# Finding and removing if statements
ifregex = re.compile(
    r'if(\s*\([A-Za-z0-9\s<>=!-+)]*){([A-Za-z.()"<>+-+!0-9;=]*)}(else if{[A-Za-z.()"<>+-+!0-9;=]*})*(else{[A-Za-z.()"<>+-+!0-9;=]*})*')
check4 = re.compile(
    r'if\s*\(?\s*[\w+=><\/\s]+\)?\{[\w\s<>=!-+)]*\}?\s*(else if\s*\(?\s*[\w+=><\/]+\)?\{[\w\s<>=!-+)]*\})*(else\s*\{?[\w\s<>=!-+)]*\}?)*')

if not ifregex.search(nowh) and check4.search(nowh):
    print("Something went wrong, check your if statements")
    sys.exit()


if ifregex.search(nowh):
    noif = ifregex.sub("", nowh)

print(spr)

# Finding and removing object declaration statements
objregex = re.compile(r'Person\s+\w+\s*\=\s*new\s+Person\(\w+,\s+\w+\);')
objcheck = re.compile(r'P\w+\s*\w+\s*\=?\s*[\w\s(),]+;')

if not objregex.search(noif) and objcheck.search(noif):
    print("Something went wrong, check your object declaration statements")
    sys.exit()

if objregex.search(noif):
    noobj = objregex.sub("", noif)

print(spr)

# Finding and removing person info
pregex = re.compile(r'you\.printInfo\(\);')
pcheck = re.compile(r'\w+\.\w+\(?\)?;?')

if not pregex.search(noobject) and pcheck.search(noobj):
    print("Something went wrong, check your method statements.")
    sys.exit()

if pregex.search(noobj):
    nop = pregex.sub("", noobj)

print(spr)

obclass = re.compile(
    r'(public|private)\s+\w+\((int|String|double)\s+\w(,\s+(int|String|double)\s+\w)*(,\s+(int|String|double)\s+\w)*\){}')
obcheck = re.compile(r'(public|private)*\s*\w*\s*\(?[\w\s,]+\)?{}')

if not obclass.search(nop) and obcheck.search(nop):
    print("Something went wrong, check your object class declaration statements")
    sys.exit()

if obclass.search(nop):
    noob = obclass.sub("", nop)


print(spr)

# Finding and removing the object method declaration statements
opening = re.compile(r'(public|private)\s+(static\s+)*void\s+\w+\([\w,\s]*\){')
opencheck = re.compile(r'(public|private)*\s*\w+\s*\w+\s*\w*\(?[\w\D\s]*\)?{')

if not opening.search(noob) and opencheck.search(noob):
    print("Something went wrong, check your method declaration statements")
    sys.exit()

if opening.search(noob):
    noopen = opening.sub("", noob)


print(spr)

# Compiker
test = re.compile(r'\w')

if test.search(noopen):
    print("Something went wrong, check your code again.")
    sys.exit()

file.close()

print("Your code was successfully compiled! No errors detected.")
