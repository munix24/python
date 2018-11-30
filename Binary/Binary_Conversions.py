#binary conversions
#http://www.devdungeon.com/content/working-binary-data-python
def space_per_interval(string, interval):
    return ' '.join([string[i:i+interval] for i in range(0, len(string), interval)])

def chr_2_ascii(char):
    #'c' returns 99
    return ord(char)

def chr_2_bin(char):
    #'c' returns '0b1100011'
    return bin(ord(char))

def str_2_bin(string):
    #'cc' returns '11000111100011'
    #another method is ''.join('{0:08b}'.format(ord(c), 'b') for c in string)
    return ''.join(bin(ord(c))[2:].zfill(8) for c in string)

def str_2_ascii(string):
    #'cc' returns '99 99'
    return list(ord(c) for c in string)
##    return ' '.join(str(ord(c)) for c in string)

def bin_2_ascii(bin):
    #'0b1100011' returns 99
    return int(bin, 2)

def bin_2_chr(bin):
    #'0b1100011' returns 'c'
    return chr(int(bin, 2))

def binstr_2_int(binstring):
    """
    convert string of bits to integer. '0110001101100011' returns 99 99. 
    binstring has to have a length that is a multiple of 8 and no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ' '.join(str(int(char, 2)) for char in string_blocks)

def binstr_2_str(binstring):
    """
    convert string of bits to equivalent string. '0110001101100011' returns 'cc'. 
    binstring has to have a length that is a multiple of 8 and no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ''.join(chr(int(char, 2)) for char in string_blocks)

def pad_bits(bits, pad = 8):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits

def int_2_binlist(n):
    """converts integer to binary list"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [n % 2] + result
        n = n // 2
    return result

def int_2_binlist_rec(n):
    """converts integer to binary list using recursion"""
    if n == 0:
        return []
    return int_to_bin_rec(n // 2) + [n % 2]

def dec_to_baselist_rec(n, base):
    '''
    converts decimal to bit list in input base using recursion
    example: dec_to_base_rec(.390625, 2) = [0, 1, 1, 0, 0, 1]
    .390625 in base 2 is .011001
    -2, -3, and -6 bits are present so calculation is:
    2 ** -2 + 2 ** -3 + 2 ** -6 = .390625
    '''
    if n == 0 or n >= 1:
        return []
    n2 = n * base #
 
    # left of decimal + dec_to_bin_rec(right of decimal)
    return [int(n2 // 1)] + dec_to_bin_rec(n2 % 1) 

def dec_to_binlist_rec(n):
    '''
    converts decimal to bit list in base 2 using recursion
    example: dec_to_bin_rec(.390625) = [0, 1, 1, 0, 0, 1]
    .390625 in base 2 is .011001
    -2, -3, and -6 bits are present so calculation is:
    2 ** -2 + 2 ** -3 + 2 ** -6 = .390625
    '''
    return dec_to_baselist_rec(n, 2)

def binlist_to_int(binlist):
    '''
    converts binary list of bits to integer
    example: binlist_to_int([1,1,1]) = 7
    '''
    return bitlist_to_int(binlist, 2)
    
def bitlist_to_int(bitlist, base):
    '''
    converts binary list of bits of base to integer
    example: binlist_to_int([1,1,1], 2) = 7
    '''
    ret = 0
    bitlist_len = len(bitlist)
    for i in range(bitlist_len):
        ret += bitlist[bitlist_len - 1 - i] * base ** i
    return ret

def binlist_to_dec(binlist):
    '''
    converts binary list of bits to decimal
    example: binlist_to_int([0, 1, 1, 0, 0, 1]) = .390625
    '''
    return bitlist_to_dec(binlist, 2)
    
def bitlist_to_dec(bitlist, base):
    '''
    converts binary list of bits of base to decimal
    example: binlist_to_int([0, 1, 1, 0, 0, 1], 2) = .390625
    '''
    ret = 0
    bitlist_len = len(bitlist)
    for i in range(bitlist_len):
        a = bitlist[bitlist_len - 1 - i]
        b = base ** (-i - 1)
        ret += bitlist[i] * base ** (-i - 1)
        print(a,b, ret)
    return ret

##print(chr2bin('c'))

##print((str2bin('cc')))
##print(binstr2dec(str2bin('cod')))

##print((convert_to_bits(128)))
##print((string_to_bits('cc')))
