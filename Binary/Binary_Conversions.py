#binary conversions
#http://www.devdungeon.com/content/working-binary-data-python
def space_per_interval(string, interval):
    return ' '.join([string[i:i+interval] for i in range(0, len(string), interval)])

def chr2ascii(char):
    #'c' returns 99
    return ord(char)

def chr2bin(char):
    #'c' returns '0b1100011'
    return bin(ord(char))

def str2bin(string):
    #'cc' returns '11000111100011'
    #another method is ''.join('{0:08b}'.format(ord(c), 'b') for c in string)
    return ''.join(bin(ord(c))[2:].zfill(8) for c in string)

def str2ascii(string):
    #'cc' returns '99 99'
    return list(ord(c) for c in string)
##    return ' '.join(str(ord(c)) for c in string)

def bin2ascii(bin):
    #'0b1100011' returns 99
    return int(bin, 2)

def bin2chr(bin):
    #'0b1100011' returns 'c'
    return chr(int(bin, 2))

def binstr2int(binstring):
    """
    convert string of bits to integer. '0110001101100011' returns 99 99. binstring has to be length 8 with no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ' '.join(str(int(char, 2)) for char in string_blocks)

def binstr2str(binstring):
    """
    convert string of bits to equivalent string. '0110001101100011' returns 'cc'. binstring has to be length 8 with no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ''.join(chr(int(char, 2)) for char in string_blocks)

def pad_bits(bits, pad = 8):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits

def int_to_bin(n):
    """converts integer to bit list"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [n % 2] + result
        n = n // 2
    return result

def int_to_bin_rec(n):
    """converts integer to bit list using recursion"""
    if n == 0:
        return []
    return int_to_bin_rec(n // 2) + [n % 2]

##print(chr2bin('c'))

##print((str2bin('cc')))
##print(binstr2dec(str2bin('cod')))

##print((convert_to_bits(128)))
##print((string_to_bits('cc')))
