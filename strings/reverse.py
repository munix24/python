x='asdf'

def rev(inp):
	return ''.join(inp[-x] for x in range(1,len(inp)+1))

print(rev(x))
