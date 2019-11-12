# JSON-MERGER-PYTHON
A Python utility that merge multiple JSON file to a new merged file with some parameters like path to folder, base name of input files, base name of output file, maximum size of merged file.

## Operating System
 Wherever python runs. (**Almost in everywhere OS**)

## Input Parameters:
- Path to the folder containing input JSON files.
- Base name of Input files.
- Base name of Output files.
- Maximum merged JSON file size (in bytes).

## Result:
 A Merged JSON file will be created.
 
## Features:
- File size of merged file will **never exceed the maximum file size.**
- Input File name will be checked and should be strictly in the format of *(Input_base_name)(numeric)(.json)*. **eg.** data1.json , data2.json
- Processing input files in **increasing order** based on their number added after input base name so that, if any file is mergerd and results as exceeding the maximum file size then this utility will not merge that file. And after that no more file will be processed.
- For output files, Utility will **check for existing of merged file** in folder and accordingly increase the counter and create new merged file with **incremented number** after the base name. Example : if merge1.json and merge2.json is existed then it will create merge3.json
- Each output file will contain the **JSON array** *(Completely formatted).*
- Utility is generic solution so that, **any kink of JSON array can be merged**. e.g. data1.json contains two keys : "student" and "employee" and data2.json contains only "student " then, merged file will contanin "student" and "employee" both.
- It can **support all characters** *(non-english also).*

## Algorithmic Complexity
### For I/O Operation:
* Read all **K files** in **N valid input files**. where Kth file is the last file merged after encounting the maximum file size reached for merge file. *(Best possible way)*
* **Write only one merge file.** *(Best possible way)*

### For loops:
- (N+N+NlogN+K+MlogM) = **(2N+NlogN+K+MlogM)** *where, N - Number of files in folder, K - number of input files that are merged, M - Number of existing merged file in folder.* *(Best possible way)*
 
### For Miscellaneous:
* Fetching list of files in folder **only one time.** *(Best Possible way).*
* Opening file **K times** and closing file **K times.** *(Best possible way)*
