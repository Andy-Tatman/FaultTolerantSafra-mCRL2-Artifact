#!/bin/bash

# mu calc props:
# P0, Liveness, P5, P10
# NO mu calc props:
# rest

# Props for specific instances (of N)
# P0, P6, Liveness, Safety

# Props for Sensitive only:
# P11
# Props for Tolerant only:
# P3, 6, 8-10, 12
# 
# => rest (P0-2, 4-5, 7, 11, Liveness & Safety) is for both


# Sensi non-reduced forms:
# P1, p2, p4, p5, p7, p11, Safety
# Sensi reduced forms:
# P0, Liveness

# PS C:\Users\andyt\Desktop\School\Thesis_MSc\FINALSpecs> 
#   & 'C:\Program Files\mCRL2\bin\pbessolve.exe' --threads=8 .\Safra_n3_Sensi\P15_Sensi_n3_m2_s2.pbes

# All PBES's made, and props checked (TRUE), for Sensi.

# Tol non-reduced forms:
# P1, P2, P3, P4, P5, P7, P8, P9, P12, Safety
#       * P8-10 (+ 0, Safety,Liveness) are instance specific!
# Tol reduced forms:
# P0, Liveness, P6, P10

# PBESs for Tol n2 made & checked.
# For tol n3: checked = p1, P2, P3, P5, P6, Safety, Liveness
#             All PBES's made
#       P4 is too big for RAM, need to split them up!
# (Numbers above still = old numbers) (double old now)

# After removing P7, P9, P10:
# P8 = P7
# P11 = P8 
# P12 = P9
# P13 = P10
# P14 = P11 
# P15 = P12 
# P16 = P13

# After adjustments:
# All PBES's made, and props checked (TRUE), for Sensi.
# Made the lts for n2 tol (non-red) & n3 tol (non-red)
# Checked P8, P9, P10, P13, Safety for n3 tol (non-red)
# Checked P0, P7, P11, Liveness for n3 tol Reduced
# (Now all +1, as I have since removed P4.)

# From Tol_Safra_n4_m1_s2_c3.lts, not enough memory to generate the PBES for P1...

# Command to run:
# & 'C:\Program Files\mCRL2\bin\lts2pbes.exe' -p --formula=..\PropertiesThesis\P0_AlwaysEventuallyAnnounce_N2.mcf .\Safra_n2_Sensi_Reduced\Sensi_n2_m1_s1_red.lts .\Safra_n2_Sensi_Reduced\TEST.pbes
# split up, ^ = v
# & 'C:\Program Files\mCRL2\bin\lts2pbes.exe' -p 
# --formula=..\PropertiesThesis\P0_AlwaysEventuallyAnnounce_N2.mcf 
# .\Safra_n2_Sensi_Reduced\Sensi_n2_m1_s1_red.lts 
# .\Safra_n2_Sensi_Reduced\TEST.pbes
# (last line = output file)

# After removing P4, all numbers above it are now 1 lower (duh)