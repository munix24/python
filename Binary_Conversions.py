#binary conversions
#http://www.devdungeon.com/content/working-binary-data-python
def space_per_interval(string, interval):
    return ' '.join([string[i:i+interval] for i in range(0, len(string), interval)])

def chr2dec(char):
    return ord(char)

def chr2bin(char):
    return bin(ord(char))

def str2bin(string):
    return ''.join(bin(ord(c))[2:].zfill(8) for c in string)
    #''.join('{0:08b}'.format(ord(c), 'b') for c in string), 

def str2dec(string):
    return ''.join(ord(c) for c in string)

def bin2dec(binstring):
    return int(binstring, 2)

def bin2chr(binstring):
    return chr(int(binstring, 2))

def binstr2dec(binstring):
    """
    convert string of bits to decimal. binstring has to be length 8 with no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ' '.join(str(int(char, 2)) for char in string_blocks)

def binstr2str(binstring):
    """
    convert string of bits to equivalent string. binstring has to be length 8 with no prefix
    """
    string_blocks = (binstring[i:i+8] for i in range(0, len(binstring), 8))
    return ''.join(chr(int(char, 2)) for char in string_blocks)
	
	
##print((str2bin('cod')))
##print(binstr2dec(str2bin('cod')))