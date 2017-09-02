#TODO take file / dir as input
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
#https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python

import os, glob
path='./'                                                       #'./'for cur dir
#listing = os.listdir(path)                                     #another dir method
#for infile in listing:
with open('linecount.csv', 'wt') as out_file:                   #open output file (cur dir) for write. creates file if it doesnt exist
    out_file.write('filename, start,end,length,sub,avg len/sub\n')       #write headings to output
    iFileTot=0                                                  #file total  
    iLineTot=0                                                  #line total per file
    iSubLenTot=0                                               	#sub length total
    iSubCntTot=0                                                #sub count total
    for filename in glob.glob(os.path.join(path, '*.*')):       #loop through all files in cur dir
        try:
            lFileTypeSkip = ['.py', 'dsr', 'dsx','frx','csv']   #skip file extensions
            #if filename[-3:].lower()=='.py' or filename[-3:].lower()=='dsr' or filename[-3:].lower()=='dsx' or filename[-3:].lower()=='frx':
            if any(x in filename[-3:].lower() for x in lFileTypeSkip): 
                continue                                        #skip file
            out_file.write(filename+'\n')                       #write filename to output
            iLineCur=0                                          #line cur num
            iLineStart=0                                        #line start num
            
            iSubCnt=0                                           #sub count in file
            iSubLen=0                                          	#sub length
            iSubLenFil=0                                       	#sub length in file
            sSubName=''                                      	#sub name
            lStringStart = ['Private Function', 'Public Function', 'Private Sub','Public Sub']  #string matches to begin counting
            lStringEnd   = ['End Function', 'End Sub']                                          #string matches to end counting
            with open(filename) as file:                        
                for line in file:                               #loop through all lines in file
                    iLineCur+=1                                 #store file line num
                    #if any(x in line for x in lStringStart):   #if any strings are found in line
                    if line.startswith(tuple(lStringStart)):    #if any strings are found in beg of line
                        sSubName=line[:line.find('(')]          #method name (from beggining of line to first '('
                        iLineStart=iLineCur                     #store start line num
                    if iLineStart !=0 and line.startswith(tuple(lStringEnd)):   
                        iSubCnt+=1                           	#inc string count by 1 
                        iSubLen=iLineCur-iLineStart+1          	#+1 for inclusive
                        iSubLenFil+=iSubLen                   	#string line length for file
                        out_file.write(',' + str(iLineStart) + ',' + str(iLineCur) + ',' + str(iSubLen)+','+sSubName +'\n')
                        iLineStart=0                            #reset start line num
                if(iLineCur!=0 and iSubLenFil!=0 and iSubCnt!=0):
                    out_file.write('Total:,,'+ str(iLineCur) +','+str(iSubLenFil)+','+str(iSubCnt)+ ','+str(iSubLenFil/iSubCnt)+'\n')
                    iFileTot+=1                                 #inc file total by 1
                    iLineTot+=iLineCur                          #line count for all files
                    iSubCntTot+=iSubCnt                      	#string count for all files
                    iSubLenTot+=iSubLenFil                    	#string line length for all files
        except UnicodeDecodeError:                              #could not read file so skip it
            continue
    if(iFileTot!=0):
        out_file.write('\n')
        out_file.write(',,Tot lines,Tot length,Tot sub,avg len/sub\n')          #write headings to output
        out_file.write(',,'+ str(iLineTot)+','+str(iSubLenTot)+','+str(iSubCntTot) +','+str(iSubLenTot/iSubCntTot)+',\n')
        out_file.write('\n')
        out_file.write('File Total,,lines/file,sub length/file,sub/file\n')     #write headings to output
        out_file.write(str(iFileTot)+',,'+ str(iLineTot/iFileTot)+','+str(iSubLenTot/iFileTot)+','+str(iSubCntTot/iFileTot) +',\n')
print('\n')
print('done')
input()
