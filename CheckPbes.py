import subprocess

# Run this script from the Root folder of the repo!
# If mCRL2 is installed in a different location (in Windows), adjust the first 
# field of commandList. 
# If you are running this on Linux, you may need to adjust the "\\".
# Recommended: >= 32 GB of RAM. 
# (checking Safety for N3 m2 s2 cr2 will exceed 32GB on Windows 11, 
#   resulting in heavy disk usage.)

SENSI_N2 = ".\\Safra_n2_Sensi"
SENSI_N2_RED = SENSI_N2 + "_Reduced"
SENSI_N3 = ".\\Safra_n3_Sensi"
SENSI_N3_RED = SENSI_N3 + "_Reduced"
SENSI_N4 = ".\\Safra_n4_Sensi"
SENSI_N4_RED = SENSI_N4 + "_Reduced"

# the proper file begin = PN for some formula N / PSafety / PLiveness
SENSI_N2_FILE_BEGIN = "_Sensi_n2_"
SENSI_N3_FILE_BEGIN = "_Sensi_n3_"
SENSI_N4_FILE_BEGIN = "_Sensi_n4_"
SENSI_OPTIONS = ["m1_s1", "m2_s1", "m1_s2", "m2_s2"]
SENSI_FILE_END = "_bisim.pbes"
SENSI_RED_FILE_END = "_red_bisim.pbes"

SENSI_NORM_FORMS = list(map( lambda s : "\\"+s, \
    ["P1", "P2", "P4", "P5", "P7", "P11", "PSafety"]))

SENSI_RED_FORMS = list(map( lambda s : "\\"+s, \
    ["P0", "PLiveness"]))

sensi_forms_n2 = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_NORM_FORMS:
        sensi_forms_n2.append(SENSI_N2 + pn + SENSI_N2_FILE_BEGIN + mid + SENSI_FILE_END)
        
sensi_forms_n2_red = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_RED_FORMS:
        sensi_forms_n2_red.append(SENSI_N2_RED + pn + SENSI_N2_FILE_BEGIN + mid + SENSI_RED_FILE_END)

sensi_forms_n3 = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_NORM_FORMS:
        sensi_forms_n3.append(SENSI_N3 + pn + SENSI_N3_FILE_BEGIN + mid + SENSI_FILE_END)
        
sensi_forms_n3_red = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_RED_FORMS:
        sensi_forms_n3_red.append(SENSI_N3_RED + pn + SENSI_N3_FILE_BEGIN + mid + SENSI_RED_FILE_END)
        
sensi_forms_n4 = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_NORM_FORMS:
        sensi_forms_n4.append(SENSI_N4 + pn + SENSI_N4_FILE_BEGIN + mid + SENSI_FILE_END)
        
sensi_forms_n4_red = []
for mid in SENSI_OPTIONS:
    for pn in SENSI_RED_FORMS:
        sensi_forms_n4_red.append(SENSI_N4_RED + pn + SENSI_N4_FILE_BEGIN + mid + SENSI_RED_FILE_END)


TOL_N2 = ".\\Tol_Safra_n2_Crashes"
TOL_N2_RED = TOL_N2 + "_Reduced"
TOL_N3 = ".\\Tol_Safra_n3_Crashes"
TOL_N3_RED = TOL_N3 + "_Reduced"
TOL_N4 = ".\\Tol_Safra_n4_Crashes"
TOL_N4_RED = TOL_N4 + "_Reduced"

# the proper file begin = PN for some formula N / PSafety / PLiveness
TOL_N2_FILE_BEGIN = "_Tol_n2_"
TOL_N3_FILE_BEGIN = "_Tol_n3_"
TOL_N4_FILE_BEGIN = "_Tol_n4_"
TOL_OPTIONS = ["m1_s1", "m2_s1", "m1_s2", "m2_s2"]
TOL_N2_CR = "_cr1"
TOL_N3_CR = "_cr2"
TOL_N4_CR = "_cr3"
TOL_FILE_END = "_bisim.pbes"
TOL_RED_FILE_END = "_red_bisim.pbes"

TOL_NORM_FORMS = list(map( lambda s : "\\"+s, \
    ["P1", "P2", "P3", "P4", "P5", "P7", "P8", "P9", "P12", "PSafety"]))

TOL_RED_FORMS = list(map( lambda s : "\\"+s, \
   ["P0", "P6", "P10", "PLiveness"]))

tol_forms_n2 = []
for mid in TOL_OPTIONS:
    for pn in TOL_NORM_FORMS:
        tol_forms_n2.append(TOL_N2 + pn + TOL_N2_FILE_BEGIN + mid + TOL_N2_CR + TOL_FILE_END)
        
tol_forms_n2_red = []
for mid in TOL_OPTIONS:
    for pn in TOL_RED_FORMS:
        tol_forms_n2_red.append(TOL_N2_RED + pn + TOL_N2_FILE_BEGIN + mid + TOL_N2_CR + TOL_RED_FILE_END)

tol_forms_n3 = []
for mid in TOL_OPTIONS:
    for pn in TOL_NORM_FORMS:
        tol_forms_n3.append(TOL_N3 + pn + TOL_N3_FILE_BEGIN + mid + TOL_N3_CR + TOL_FILE_END)
        
tol_forms_n3_red = []
for mid in TOL_OPTIONS:
    for pn in TOL_RED_FORMS:
        tol_forms_n3_red.append(TOL_N3_RED + pn + TOL_N3_FILE_BEGIN + mid + TOL_N3_CR + TOL_RED_FILE_END)


commandList = ["C:\\Program Files\\mCRL2\\bin\\pbessolve.exe", \
                # The number of threads we use. When using powershell (as opposed to eg the mcrl GUI),
                # thread count appears to be limited to approx 5...
                "--threads=4",\
                # The actual PBES we are checking
                ".\\Safra_n2_Sensi_Reduced\\P0_Sensi_n2_m1_s1_red.pbes"]

INDEX_PBES = 2

def checkPBES(pbesFile : str) : 
    """pbesFile should include the address, from the folder where this .py is called."""
    commandList[INDEX_PBES] = pbesFile
    result = subprocess.run(commandList, capture_output=True, text=True)
    #capture_output=True captures the stdout & -err.
    # print(result.stdout.rstrip()) 
    if result.returncode != 0:
        print(result.stderr)
        print("ERROR")
        print(result)
        exit(1)
    elif result.stdout.rstrip() != "true":
        print("PBES does not hold!")
        print(result)
        exit(2)

ctr = 0

# Run the specific section you are interested in. 
# Note that the larger instances (N4 sensi, N3 tol & up) will take a LONG time.

print("Running Sensi N2")
for p in sensi_forms_n2 + sensi_forms_n2_red:
    checkPBES(p)
    ctr += 1
    if ctr%4 == 0:
        print("Done " + str(ctr) + " so far.")

print("Running Sensi N3")
for p in sensi_forms_n3 + sensi_forms_n3_red:
    checkPBES(p)
    ctr += 1
    if ctr%4 == 0:
        print("Done " + str(ctr) + " so far.")
        
print("Running Sensi N4")
for p in sensi_forms_n4 + sensi_forms_n4_red:
    checkPBES(p)
    ctr += 1
    if ctr%1 == 0:
        print("Done " + str(ctr) + " so far.")

print("Running Tol N2")
for p in tol_forms_n2 + tol_forms_n2_red:
    checkPBES(p)
    ctr += 1  
    if ctr%4 == 0:
        print("Done " + str(ctr) + " so far.")
    
print("Running Tol N3")
for p in tol_forms_n3 + tol_forms_n3_red:
    print(p) 
    checkPBES(p)
    ctr += 1
    if ctr%1 == 0:
        print("Done " + str(ctr) + " so far.")

# By default, this should equal 4*9=36 for 1 batch of Sensi (norm+red), 
# or 4*14 = 56 for 1 batch of Tol (norm+red) 
# * 1 batch = 1 group of N's formulas
print("No false formula found, all " + str(ctr) + " formulas checked hold.")
if ctr % 4 != 0:
    print("Warning, ctr mod 4 is not 0, did something get changed?")
