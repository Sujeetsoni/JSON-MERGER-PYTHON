import os
import ast
import json
path=input("Enter the path of folder in this format- X:\XX\XXX :  ")                #Asking for input no.1 : Path of folder
os.chdir(path)                                                                      #Changing the Current Working Directory to the input folder
lof=os.listdir()                                                                    #Fetching all files of that folder to list
inbasename=input("Enter the base name for input files :  ")                         #Asking for input no.2 : Base name for input files
filelist=[]                                     
for i in lof:                                                                       #Checking each file for desired formated name
    if i.endswith('.json'):
        j = i[:-5]
    if i.startswith(inbasename):
        j=j[(len(inbasename)):]
    if(i.startswith(inbasename) and i.endswith('.json') and j.isnumeric()):         #Also checking for that middle section should be numeric eg. data(numeric).json
        filelist.append(i)
filelist.sort()
outbasename=input("Enter the base name for output files :  ")                       #Asking for input no.3 : Base name for output files 
maxfilesize=int(input("Max merged file size (in bytes) :  "))                       #Asking for input no.4 : Maximum merged file size
merge={}
mergefilesize=0
for file in range(len(filelist)):                                                   #Checking for each file for merging
    statinfo = os.stat(filelist[file])                                              #Checking file size of each file
    filesize=statinfo.st_size
    mergefilesize=mergefilesize+filesize
    if(filesize>maxfilesize or mergefilesize>maxfilesize):                          #Checking file size that doesn't exceeded maximum file size
        break
    else:
        f=open(filelist[file])                                                      #Opening input file for reading
        string=f.read()                                                             #Reading file and store in string
        f.close()
        string=ast.literal_eval(string)
        os.remove(filelist[file])                                                   #Removing the merged file from directory
        for key in string: 
            if key in merge: 
                merge[key] = merge[key] + string[key]                               #Merging file
            else:
                merge[key] = string[key]                                            #Merging file
if(len(merge)==0):                                                                  #If on file is merged then simply out of the program
    pass
else:
    mfilelist=[]
    for i in lof:                                                                   #Checking already existing merge files in directory
        if i.endswith('.json'):
            j = i[:-5]
        if i.startswith(outbasename):
            j=j[(len(outbasename)):]
        if(i.startswith(outbasename) and i.endswith('.json') and j.isnumeric()):    #Also checking for that middle section should be numeric eg. merge(numeric).json
            mfilelist.append(int(j))
    mfilelist.sort(reverse=True)
    if(len(mfilelist)==0):                                                          #If no merge file is existed start with 1
        temp=0
    else:
        temp=mfilelist[0]                                                           #If merge file existed then start with after higest numbered merge file
    mergenumber=temp+1
    mergefilename=outbasename+str(mergenumber)+".json"                              #Creating a file name for merge file
    mergefile = open(mergefilename, "w")                                            #Creating a merge file
    mergefile.write(str(json.dumps(merge)))                                         #Writing on merge file
    mergefile.close()                                                               #Closing a merge file
