def len_longest_dir_path(path):
    """
    returns the length of the longest file name (including directory) in file system
    """
    if (not path): 
        return 0
    
    longest_so_far = -1
    height_at_level = {-1: 0}
    level = 0

    #parse path into list and iterate
    for line in path.split('\n'):
        #tabs, '\t', specifies the directory level. For example 0 '\t' means root
        level = line.count('\t');
        string = line.lstrip('\t')
        
        #if file
        if '.' in string:
            longest_so_far = max(longest_so_far, len(string) + height_at_level[level-1])
        #if directory add 1 to len(string) for suffix, '/'
        else:
            height_at_level[level] = (height_at_level[level-1] + len(string) + 1)
    return longest_so_far

path=''
print(len_longest_dir_path(path)) #0

path='dir\n\tsubdir1\n\t\tsubdir12\n\t\t\tfile.ext\n\tsubdir2\n\t\tsubdir22\n\t\t\tfile.ext'
print(len_longest_dir_path(path)) #29
