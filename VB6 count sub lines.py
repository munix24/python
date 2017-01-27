import os, glob
path='./'        #'./'for cur dir
#listing = os.listdir(path)                                     #another dir method
#for infile in listing:
with open('linecount.csv', 'wt') as out_file:                   #open output file (cur dir) for write. creates file if it doesnt exist
    out_file.write('filename, start,end,length,sub,ave len/sub\n')       #write headings to output
    iFileTot=0                                                  #file total  
    iLineTot=0                                                  #line total per file
    iLineLenTot=0                                               #line length total within strings
    iStringTot=0                                                #string count total
    for filename in glob.glob(os.path.join(path, '*.*')):       #loop through all files in cur dir
        try:
            lFileTypeSkip = ['.py', 'dsr', 'dsx','frx','csv']         #skip file extensions
            #if filename[-3:].lower()=='.py' or filename[-3:].lower()=='dsr' or filename[-3:].lower()=='dsx' or filename[-3:].lower()=='frx':
            if any(x in filename[-3:].lower() for x in lFileTypeSkip): 
                continue                                        #skip file
            out_file.write(filename+'\n')                       #write filename to output
            iLineCur=0                                          #line cur
            iLineStart=0                                        #line start
            iLineLen=0                                          #line length
            iLineLenFil=0                                       #line length cumulative
            
            iStringFil=0                                        #string count in file
            sStringName=''                                      #string name
            lStringStart = ['Private Function', 'Public Function', 'Private Sub','Public Sub']  #string matches to begin counting
            lStringEnd   = ['End Function', 'End Sub']                                          #string matches to end counting
            with open(filename) as file:                        
                for line in file:                               #loop through all lines in file
                    iLineCur+=1                                 #store file line num
                    #if any(x in line for x in lStringStart):   #if any strings are found in line
                    if line.startswith(tuple(lStringStart)):    #if any strings are found in beg of line
                        sStringName=line[:line.find('(')]       #method name (from beggining of line to first '('
                        iLineStart=iLineCur                     #store start line num
                    if iLineStart !=0 and line.startswith(tuple(lStringEnd)):    
                        iLineLen=iLineCur-iLineStart+1          #+1 for inclusive
                        iStringFil+=1                           #inc string count by 1
                        iLineLenFil+=iLineLen                   #store line num
                        out_file.write(',' + str(iLineStart) + ',' + str(iLineCur) + ',' + str(iLineLen)+','+sStringName +'\n')
                        iLineStart=0                            #reset start line num
                if(iLineCur!=0 and iLineLenFil!=0 and iStringFil!=0):
                    out_file.write('Total:,,'+ str(iLineCur) +','+str(iLineLenFil)+','+str(iStringFil)+ ','+str(iLineLenFil/iStringFil)+'\n')
                    iFileTot+=1                                 #inc file total by 1
                    iLineTot+=iLineCur
                    iStringTot+=iStringFil
                    iLineLenTot+=iLineLenFil
        except UnicodeDecodeError:                              #could not read file so skip it
            continue
    if(iFileTot!=0):
        out_file.write('\n')
        out_file.write(',,Tot lines,Tot length,Tot sub,ave len/sub\n')       #write headings to output
        out_file.write(',,'+ str(iLineTot)+','+str(iLineLenTot)+','+str(iStringTot) +','+str(iLineLenTot/iStringTot)+',\n')
        out_file.write('\n')
        out_file.write('File Total,,lines/file,line length/file,sub/file\n')       #write headings to output
        out_file.write(str(iFileTot)+',,'+ str(iLineTot/iFileTot)+','+str(iLineLenTot/iFileTot)+','+str(iStringTot/iFileTot) +',\n')
print('\n')
print('done')
input()
