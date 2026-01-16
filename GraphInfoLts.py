import subprocess

# Run this script from the Root folder of the repo!
# If mCRL2 is installed in a different location (in Windows), adjust the first 
# field of commandList. 
# If you are running this on Linux, you may need to adjust the "\\".
# Recommended: >= 32 GB of RAM. 

SENSI_N2 = ".\\Safra_n2_Sensi"
SENSI_N2_RED = SENSI_N2 + "_Reduced"
SENSI_N3 = ".\\Safra_n3_Sensi"
SENSI_N3_RED = SENSI_N3 + "_Reduced"
SENSI_N4 = ".\\Safra_n4_Sensi"
SENSI_N4_RED = SENSI_N4 + "_Reduced"

SENSI_N2_FILE_BEGIN = "\\Sensi_n2_"
SENSI_N3_FILE_BEGIN = "\\Sensi_n3_"
SENSI_N4_FILE_BEGIN = "\\Sensi_n4_"
SENSI_OPTIONS = ["m1_s1", "m1_s2", "m2_s1", "m2_s2"]
SENSI_FILE_END = "_bisim.lts"
SENSI_RED_FILE_END = "_red_bisim.lts"


TOL_N2 = ".\\Tol_Safra_n2_Crashes"
TOL_N2_RED = TOL_N2 + "_Reduced"
TOL_N3 = ".\\Tol_Safra_n3_Crashes"
TOL_N3_RED = TOL_N3 + "_Reduced"
TOL_N4 = ".\\Tol_Safra_n4_Crashes"
TOL_N4_RED = TOL_N4 + "_Reduced"

TOL_N2_FILE_BEGIN = "\\Tol_n2_"
TOL_N3_FILE_BEGIN = "\\Tol_n3_"
TOL_N4_FILE_BEGIN = "\\Tol_n4_"
TOL_OPTIONS = ["m1_s1", "m2_s1", "m1_s2", "m2_s2"]
TOL_N2_CR = "_cr1"
TOL_N3_CR = "_cr2"
TOL_N4_CR = "_cr3"
TOL_FILE_END = "_bisim.lts"
TOL_RED_FILE_END = "_red_bisim.lts"

sensi_files_n2 = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n2.append(SENSI_N2 + SENSI_N2_FILE_BEGIN + mid + SENSI_FILE_END)
sensi_files_n2_red = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n2_red.append(SENSI_N2_RED + SENSI_N2_FILE_BEGIN + mid + SENSI_RED_FILE_END)
    
sensi_files_n3 = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n3.append(SENSI_N3 + SENSI_N3_FILE_BEGIN + mid + SENSI_FILE_END)
sensi_files_n3_red = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n3_red.append(SENSI_N3_RED + SENSI_N3_FILE_BEGIN + mid + SENSI_RED_FILE_END)
    
sensi_files_n4 = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n4.append(SENSI_N4 + SENSI_N4_FILE_BEGIN + mid + SENSI_FILE_END)
sensi_files_n4_red = [] 
for mid in SENSI_OPTIONS:
    sensi_files_n4_red.append(SENSI_N4_RED + SENSI_N4_FILE_BEGIN + mid + SENSI_RED_FILE_END)

tol_files_n2 = [] 
for mid in TOL_OPTIONS:
    tol_files_n2.append(TOL_N2 + TOL_N2_FILE_BEGIN + mid + TOL_N2_CR + TOL_FILE_END)
tol_files_n2_red = [] 
for mid in TOL_OPTIONS:
    tol_files_n2_red.append(TOL_N2_RED + TOL_N2_FILE_BEGIN + mid + TOL_N2_CR + TOL_RED_FILE_END)
    
tol_files_n3 = [] 
for mid in TOL_OPTIONS:
    tol_files_n3.append(TOL_N3 + TOL_N3_FILE_BEGIN + mid + TOL_N3_CR + TOL_FILE_END)
tol_files_n3_red = [] 
for mid in TOL_OPTIONS:
    tol_files_n3_red.append(TOL_N3_RED + TOL_N3_FILE_BEGIN + mid + TOL_N3_CR + TOL_RED_FILE_END)
    
commandList = ["C:\\Program Files\\mCRL2\\bin\\ltsinfo.exe", \
                ".\\Safra_n2_Sensi_Reduced\\Sensi_n2_m1_s1_red_bisim.lts"]

INDEX_LTS = 1

def getOptName(ltsFile : str) -> str: 
    for option in set(SENSI_OPTIONS+TOL_OPTIONS):
        if option in ltsFile:
            return option
    return "ERROR OPTION NOT FOUND" 

def printStatesN(ltsFile : str) :
    commandList[INDEX_LTS] = ltsFile
    result = subprocess.run(commandList, capture_output=True, text=True)
    # print(result.stderr)
    for line in result.stderr.split("\n"):
        # print("Line is: " + line)
        if "Number of states" in line:
            print( getOptName(ltsFile) + " " + line.split(" ")[-1][:-1] )
    
print("Running Sensi N2")
for ltsFile in sensi_files_n2+sensi_files_n2_red: 
    printStatesN(ltsFile)

print("Running Sensi N3")
for ltsFile in sensi_files_n3+sensi_files_n3_red: 
    printStatesN(ltsFile)

print("Running Sensi N4")
for ltsFile in sensi_files_n4+sensi_files_n4_red: 
    printStatesN(ltsFile)
    
print("Running Tol N2")
for ltsFile in tol_files_n2+tol_files_n2_red: 
    printStatesN(ltsFile)
    
print("Running Tol N3")
for ltsFile in tol_files_n3+tol_files_n3_red: 
    printStatesN(ltsFile)