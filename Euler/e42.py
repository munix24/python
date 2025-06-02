letters='abcdefghijklmnopqrstuvwxyz'
letters2=[i for i in letters]
print(letters2)

def word_value(word):
    value=0
    for letter in word.lower():
        #print(letter)
        value=value+letters2.index(letter)+1 #+1 since python is 0 based
    return value

#def is_triangle(num):

def triangle_num(limit):
    triangle_num_list=[]
    for _ in range(1, limit):
        triangle_num_list.append(int((_ / 2) * (_ + 1)))
    return triangle_num_list

#print(word_value('sky'))
triangle_nums = triangle_num(100)

i=0
with open('p042_words.txt') as f:
    for line in f:
       ##print(line)
        for str in line.split(','):
            word = str.strip('"')
            word_val = word_value(word)
            if word_val in triangle_nums:
                i=i+1
print(i)
            
