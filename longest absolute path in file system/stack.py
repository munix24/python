def getLongestPath(input):
  if (input is null or input == ""): 
    return 0;
  list = input.splitlines();  # Parse the string into list
  st = [-1]; #-1 to cancel the path separator before root dir
  lastLevel = -1;  # depth of the last item in st
  maxLen = 0;
  for item in list:
    bareName = item.lstrip('\t');	# Strip leading '\t's
    curLevel = item.count('\t');
    while (curLevel <= lastLevel): # cd .. to the same level as "item"
      st.pop();
      lastLevel -= 1;	
    a=st[-1];	
    st.append(len(bareName)+st[-1]+1);	# accumulated lenth, +1 for pathsep
    lastLevel=curLevel;
    if ('.' in item): 	# Only count "files" with an extension
      maxLen = max(maxLen, st[-1]);
  return maxLen;

longest_dir_path("");
longest_dir_path("dir\n\tsubdir1\n\t\tfile.ext\n\tsubdir22\n\t\tfile.ext");