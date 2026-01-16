# FaultTolerantSafra-mCRL2-Artifact
Repository for specification files (.mcrl2) &amp; formulas (.mcf) for my MSc Thesis. (Link TODO)

# Overview
This repository contains the model specifications based on a fault-sensitive and fault-tolerant version of Safra's algorithm for termination detection, as presented [here](https://doi.org/10.1007/978-3-030-91014-3_5).
These specifications are intended to be used with [mCRL2](https://www.mcrl2.org/web/index.html), specifically version 202507.0.
You can find the full artifact for my thesis, including the developed .lts & .pbes files, on Zenodo. (Link TODO)
In Chapter 6 of my thesis, we spell out what options we set to generate our files. These are also  (largely) used in the _.py_ scripts provided here.

Note that for many of the specifications (and especially the fault-tolerant models), generating the models and checking the formulas in the mCRL2 IDE is impractical. 
Instead, we recommend either using the mCRL2 GUI, or using the _.py_ scripts provided in this repository.
We run mCRL2 on Windows. If you use a different OS, or if mCRL2 is installed in a different location, you may have to adjust the first parameter of _commandList_ in the _.py_ files.

## *_Reduced 
For each configuration (_N_), we create both a 'normal' and a reduced specification. In the reduced spec, we have disabled the actions that make reflective loops in the model, e.g. "reportSeq". 
Properties using the _mu X_ operator can only be checked on the reduced specifications. 

## *_NoCr
As the name implies, the specifications marked with "NoCr" have crashes disabled in the actual specification, such that no crashes will occur in the resulting models, even for _C>0_.

## Tol_Bug_Demonstration
We discovered a bug in the fault-tolerant algorithm, for all _N >= 2_. In this folder, we show that the Safety property is violated, and provide a counter-example showing the violation. This "EVI_" file can be examined using mCRL2's [ltsgraph](https://mcrl2.org/web/user_manual/tools/release/ltsgraph.html) tool.

## Order for generating models
We generate the _.lps_ and _.lts_ files by hand, from the _.mcrl2_ files. Note that, to adjust variables _S_ and _M_, we need to adjust the _.mcrl2_ files. Note that our scripts use a specific format for the names of the _.lts_ files.
Given these _.lts_ files, we can first use [_ConvertLts.py_](https://github.com/Andy-Tatman/FaultTolerantSafra-mCRL2-Artifact/blob/main/ConvertLts.py) to reduce the _.lts_ file.
Next, using the _\_bisim.lts_ files, we can generate our _.pbes_ files to check using [_CreatePbes.py_](https://github.com/Andy-Tatman/FaultTolerantSafra-mCRL2-Artifact/blob/main/CreatePbes.py).
Finally, we can use [_CheckPbes.py_](https://github.com/Andy-Tatman/FaultTolerantSafra-mCRL2-Artifact/blob/main/CheckPbes.py) to check our generated _.pbes_ files. (Note: if you are not using Windows, you may be able to use a higher number of threads in this file.)

We used [_GraphInfoLts.py_](https://github.com/Andy-Tatman/FaultTolerantSafra-mCRL2-Artifact/blob/main/GraphInfoLts.py) to collect the number of states for our (bisimilar) files, and [_Time.Pbes.py_](https://github.com/Andy-Tatman/FaultTolerantSafra-mCRL2-Artifact/blob/main/TimePbes.py) to benchmark how long it took to verify our Safety and Liveness _.pbes_ files.
