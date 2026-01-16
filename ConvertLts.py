import subprocess
import os 

OVERWRITE_EXISTING = False

# RUN THIS SCRIPT FROM THE FINALSpecs folder!
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
SENSI_OPTIONS = ["m1_s1", "m2_s1", "m1_s2", "m2_s2"]
SENSI_FILE_END = ".lts"
SENSI_RED_FILE_END = "_red.lts"


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
TOL_FILE_END = ".lts"
TOL_RED_FILE_END = "_red.lts"

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
    
tol_files_n4 = [] 
for mid in TOL_OPTIONS:
    tol_files_n4.append(TOL_N4 + TOL_N4_FILE_BEGIN + mid + TOL_N4_CR + TOL_FILE_END)
tol_files_n4_red = [] 
for mid in TOL_OPTIONS:
    tol_files_n4_red.append(TOL_N4_RED + TOL_N4_FILE_BEGIN + mid + TOL_N4_CR + TOL_RED_FILE_END)
    
commandList = ["C:\\Program Files\\mCRL2\\bin\\ltsconvert.exe", \
                # Reduce the LTS, generate an equivalent LTS preserving strong bisimilarity 
                "--equivalence=bisim", \
                # Do not do a reachability check on the LTS (= speed up)
                "--no-reach", \
                # Removes state information, resulting in smaller files 
                # (if it was not already removed when generating the original LTS)
                "--no-state", \
                # the LTS we are working from 
                ".\\Safra_n2_Sensi_Reduced\\Sensi_n2_m1_s1_red.lts", \
                # The resulting LTS
                ".\\Safra_n2_Sensi_Reduced\\Sensi_n2_m1_s1_red_bisim.lts", \
                ]

INDEX_LTS_ORIG = 4
INDEX_LTS_NEW = INDEX_LTS_ORIG+1

def getNewLtsName(ltsFileName : str) : 
    ltsSplit = ltsFileName.split("\\") 
    ltsAddr = ltsSplit[0] + "\\\\" + ltsSplit[1] + "\\\\"
    ltsRemoveAddr = ltsSplit[-1] #ltsFileName.split("\\")[-1] 
    ltsClean = ltsRemoveAddr.split(".", 1)[0]
    
    return ltsAddr + ltsClean + "_bisim.lts"

def reduceLTS(ltsFileName : str) :
    commandList[INDEX_LTS_ORIG] = ltsFileName
    commandList[INDEX_LTS_NEW] = getNewLtsName(ltsFileName)
    if OVERWRITE_EXISTING or not os.path.isfile(commandList[INDEX_LTS_NEW]):
        result = subprocess.run(commandList) 
        # print("result = ") 
        # print(result.returncode)
        # exit(1)
        if result.returncode != 0:
            print("ERROR")
            print(result)
            exit(1)


# Run the specific section you are interested in. 
# Note that the larger instances (N4 sensi, N3 tol & up) will take a LONG time.

# SENSI models

# print("Running Sensi N2")
# for ltsFile in sensi_files_n2: 
#     reduceLTS(ltsFile)
# for ltsFile in sensi_files_n2_red:
#     reduceLTS(ltsFile)

# print("Running Sensi N3")
# for ltsFile in sensi_files_n3: 
#     reduceLTS(ltsFile)
# for ltsFile in sensi_files_n3_red:
#     reduceLTS(ltsFile)

# print("Running Sensi N4")
# for ltsFile in sensi_files_n4: 
#     reduceLTS(ltsFile)
# for ltsFile in sensi_files_n4_red:
#     reduceLTS(ltsFile)


# # TOLERANT MODELS

print("Running Tol N2")
for ltsFile in tol_files_n2: 
    reduceLTS(ltsFile)
for ltsFile in tol_files_n2_red:
    reduceLTS(ltsFile)

print("Running Tol N3")
for ltsFile in tol_files_n3: 
    reduceLTS(ltsFile)
for ltsFile in tol_files_n3_red:
    reduceLTS(ltsFile)

# only for m1s1
# print("Running Tol N4")
# for ltsFile in tol_files_n4: 
#     reduceLTS(ltsFile)
# for ltsFile in tol_files_n4_red:
#     reduceLTS(ltsFile)