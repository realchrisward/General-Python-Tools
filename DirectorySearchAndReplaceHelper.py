#!/usr/bin/env python
## /\compatability line
"""
Directory Search and Replace Helper
this script searches through all of the files in a dirctory
and will copy them over to a new directory while replacing
"user defined strings" with "new user defined strings"
"""

## import libraries
import os, sys

nargs=len(sys.argv)

if not nargs ==4:
    print("incorrect number of arguments")
else:
    indir=sys.argv[1]
    outdir=sys.argv[2]
    strreptext=sys.argv[3]
    strrepdic={}
    for kvpair in strreptext.split(';'):
        k=kvpair.split("=")[0]
        v=kvpair.split("=")[1]
        strrepdic[k]=v

def walkthedir(xindir,xoutdir,xstrrepdic):
    curdirlist=os.listdir(xindir)
    for f in curdirlist:
        try:
            if os.path.isdir(os.path.join(xindir,f)):
                if not os.path.exists(xoutdir):
                    os.makedirs(xoutdir)
                print('subdirectory - '+f)
                walkthedir(os.path.join(xindir,f),os.path.join(xoutdir,f),xstrrepdic)
            else:
                print('\tworking on file:'+f)
                ## open read file
                with open(os.path.join(xindir,f)) as rf:
                    ## open write file
                    if not os.path.exists(xoutdir):
                        os.makedirs(xoutdir)
                    with open(os.path.join(xoutdir,f),'w') as wf:
                        ## loop through lines
                        for line in rf:
                            ## loop through dict
                            for k in xstrrepdic:
                                if k in line:
                                    print('fixing line:'+line)
                                    line=line.replace(k,xstrrepdic[k])
                            ## write the new version
                            wf.write(line)
                ## close the files
        except Exception as e:
            print('\t\t***error processing file '+f+'\n\t***'+str(e))
def checkargs(xindir,xoutdir,xstrrepdic):
    print(xindir)
    print(xoutdir)
    for k in xstrrepdic:
        print(k,xstrrepdic[k])

if __name__=="__main__":
    #for a in sys.argv:
    #   print(a)
    walkthedir(indir,outdir,strrepdic)
    print('\n...finished...')
    checkargs(indir,outdir,strrepdic)
    input('press ENTER to close')
