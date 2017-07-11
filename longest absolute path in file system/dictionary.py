def longest_dir_path(path):
    longest_so_far = -1
    height_at_level = {-1: 0}
    level = 0

    for line in path.split('\n'):
        level = line.count('\t');
        string = line.lstrip('\t')
        if '.' in string:
            longest_so_far = max(longest_so_far, len(string) + height_at_level[level-1])
        else:
            height_at_level[level] = (height_at_level[level-1] + len(string) + 1)
    return longest_so_far

longest_dir_path("dir\n\tsubdir1\n\t\tsubdir2\n\t\t\tfile.ext\n\tsubdir22\n\t\tfile.ext");