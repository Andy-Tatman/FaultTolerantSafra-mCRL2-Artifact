import subprocess
import os 

OVERWRITE_EXISTING = False

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
SENSI_OPTIONS = ["m1_s1", "m2_s1", "m1_s2", "m2_s2"]
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

PROPS_ADDR = "..\\PropertiesThesis\\"

SENSI_NORM_FORMS = \
    ["P1_AllNodesCanAnno.mcf", "P2_AllNodesCanSendRecvBasic.mcf", "P4_CanAnnounceWithDone.mcf", \
      "P5_CanAnnounceWithoutDone.mcf", "P7_BasicNeverTooNew.mcf",  "P11_SeqLimitSensi.mcf"]
SENSI_NORM_SPECIFIC = \
    {2 : "P_Safety_N2.mcf", 
     3 : "P_Safety_N3.mcf",
     4 : "P_Safety_N4.mcf",} 

SENSI_RED_FORMS = []
SENSI_RED_SPECIFIC = \
    {2 : ["P0_AlwaysEventuallyAnnounce_N2.mcf", "P_Liveness_N2.mcf"], 
     3 : ["P0_AlwaysEventuallyAnnounce_N3.mcf", "P_Liveness_N3.mcf"],
     4 : ["P0_AlwaysEventuallyAnnounce_N4.mcf", "P_Liveness_N4.mcf"]}
    
TOL_NORM_FORMS = \
    ["P1_AllNodesCanAnno.mcf", "P2_AllNodesCanSendRecvBasic.mcf", "P3_AllNodesCanCrash.mcf", \
     "P4_CanAnnounceWithDone.mcf", "P5_CanAnnounceWithoutDone.mcf", "P7_BasicNeverTooNew.mcf", \
     "P8_TokenNeverTooNew.mcf", "P9_idNeverInCrashedSets.mcf", "P12_SeqLimitTol.mcf"]
TOL_NORM_SPECIFIC = \
    {2 : "P_Safety_N2.mcf", 
     3 : "P_Safety_N3.mcf",
     4 : "P_Safety_N4.mcf",} 
    
TOL_RED_FORMS = ["P10_Tol_SkipAddition.mcf"]
TOL_RED_SPECIFIC = \
    {2 : ["P0_AlwaysEventuallyAnnounce_N2.mcf", "P6_Tol_AnnCrAnn_N2.mcf", "P_Liveness_N2.mcf"], 
     3 : ["P0_AlwaysEventuallyAnnounce_N3.mcf", "P6_Tol_AnnCrAnn_N3.mcf", "P_Liveness_N3.mcf"],
     4 : ["P0_AlwaysEventuallyAnnounce_N4.mcf", "P6_Tol_AnnCrAnn_N4.mcf", "P_Liveness_N4.mcf"]}


def getFormName(formulaFileName : str, ltsFileName : str) -> str :
    """When creating a formula,
       use this to get the file name."""
    ltsSplit = ltsFileName.split("\\") 
    ltsAddr = ltsSplit[0] + "\\\\" + ltsSplit[1] + "\\\\"
    ltsRemoveAddr = ltsSplit[-1] #ltsFileName.split("\\")[-1] 
    ltsClean = ltsRemoveAddr.split(".", 1)[0]
    if formulaFileName[1] == "_":
        if formulaFileName[2] == 'S' :
            # Safety
            pbesFileName = ltsAddr + "PSafety_" + ltsClean + ".pbes" 
            return pbesFileName
        else:
            # Liveness
            pbesFileName = ltsAddr + "PLiveness_" + ltsClean + ".pbes" 
            return pbesFileName 
    else:
        PNumber = formulaFileName.split("_", 1)[0] 
        pbesFileName = ltsAddr + PNumber + "_" + ltsClean + ".pbes"
        return pbesFileName
    


commandList = ["C:\\Program Files\\mCRL2\\bin\\lts2pbes.exe", \
                # preprocesses modal operators
                "-p", \
                # for the formula: e.g.:
                "--formula=..\\PropertiesThesis\\P0_AlwaysEventuallyAnnounce_N2.mcf", \
                # the LTS we are working from:
                ".\\Safra_n2_Sensi_Reduced\\Sensi_n2_m1_s1_red_bisim.lts", \
                # where we place the resulting PBES
                ".\\Safra_n2_Sensi_Reduced\\P0_Sensi_n2_m1_s1_red_bisim.pbes"]
INDEX_FORM = 2 
INDEX_LTS = 3
INDEX_PBES = 4

FORM_PREPEND = "--formula=..\\PropertiesThesis\\"
FORM_POSTPEND = ".mcf"
PBES_POSTPEND = ".pbes"


def createPBES(ltsFile : str, formFile : str) :
    """ltsFile & pbesFile should include the address, from the folder where this .py is called."""
    commandList[INDEX_FORM] = FORM_PREPEND + formFile
    commandList[INDEX_LTS] = ltsFile
    commandList[INDEX_PBES] = getFormName(formFile, ltsFile)
    if OVERWRITE_EXISTING or not os.path.isfile(commandList[INDEX_PBES]):
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

print("Running Sensi N2")
for ltsFile in sensi_files_n2: 
    for formFile in SENSI_NORM_FORMS:
        createPBES(ltsFile, formFile)
    createPBES(ltsFile, SENSI_NORM_SPECIFIC[2])
for ltsFile in sensi_files_n2_red:
    for formFile in SENSI_RED_SPECIFIC[2]:
        createPBES(ltsFile, formFile)

print("Running Sensi N3")
for ltsFile in sensi_files_n3: 
    for formFile in SENSI_NORM_FORMS:
        createPBES(ltsFile, formFile)
    createPBES(ltsFile, SENSI_NORM_SPECIFIC[3])
for ltsFile in sensi_files_n3_red:
    for formFile in SENSI_RED_SPECIFIC[3]:
        createPBES(ltsFile, formFile)

print("Running Sensi N4")
for ltsFile in sensi_files_n4: 
    for formFile in SENSI_NORM_FORMS:
        createPBES(ltsFile, formFile)
    createPBES(ltsFile, SENSI_NORM_SPECIFIC[4])
for ltsFile in sensi_files_n4_red:
    for formFile in SENSI_RED_SPECIFIC[4]:
        createPBES(ltsFile, formFile)


# TOLERANT MODELS

print("Running Tol N2")
for ltsFile in tol_files_n2: 
    for formFile in TOL_NORM_FORMS:
        createPBES(ltsFile, formFile)
    createPBES(ltsFile, TOL_NORM_SPECIFIC[2])
for ltsFile in tol_files_n2_red:
    for formFile in TOL_RED_FORMS+TOL_RED_SPECIFIC[2]:
        createPBES(ltsFile, formFile)

print("Running Tol N3")
for ltsFile in tol_files_n3: 
    for formFile in TOL_NORM_FORMS:
        createPBES(ltsFile, formFile)
    createPBES(ltsFile, TOL_NORM_SPECIFIC[3])
for ltsFile in tol_files_n3_red:
    for formFile in TOL_RED_FORMS+TOL_RED_SPECIFIC[3]:
        createPBES(ltsFile, formFile)