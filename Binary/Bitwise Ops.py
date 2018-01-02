#https://stackoverflow.com/questions/10670379/find-xor-of-all-numbers-in-a-given-range
#https://codereview.stackexchange.com/questions/153262/calculate-xor-of-many-consecutive-and-non-consecutive-numbers
#https://stackoverflow.com/questions/45335975/trying-to-complete-google-foo-bar-level-3-queue-to-do-and-keep-exceeding-time

def f(n):    
  #XOR of range repeats after 4 numbers    
  return [n, 1, n + 1, 0][n % 4]
  
def XorRange(beg, end):   
  """    Returns XOR of all values between a and b. Works bc XOR is associative and commutative    """    
  return f(beg - 1) ^ f(end)
