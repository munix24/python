def len_longest_dir_path(path):
    """
    returns the length of the longest file name (including directory) in file system
    """
    if (not path): 
        return 0
    
    st = [-1] #stack. -1 to cancel the path separator before root dir
    last_level = -1  #depth of the last item in st
    max_len = 0
    
    for line in path.splitlines(): #parse path into list and iterate
        cur_level = line.count('\t')
        bare_name = line.lstrip('\t')
        
        while (cur_level <= last_level): #cd .. to the same level as "item"
            st.pop()
            last_level -= 1
            
        st.append(len(bare_name) + st[-1] + 1) #accumulated lenth, +1 for pathsep
        last_level = cur_level
        
        if ('.' in line): #Only count files with an extension
            max_len = max(max_len, st[-1])
    return max_len

path=''
print(len_longest_dir_path(path)) # 0

path='dir\n\tsubdir1\n\t\tsubdir12\n\t\t\tfile.ext\n\tsubdir2\n\t\tsubdir22\n\t\t\tfile.ext'
print(len_longest_dir_path(path)) # 29
