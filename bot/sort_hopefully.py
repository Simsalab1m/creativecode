words = list()

#read in words from file
filename = 'five.txt'
with open (filename) as fin:
    for line in fin:
        words.append(line.strip())

#write to new text file
filename = 'words_tracery.txt'
with open(filename, 'w') as fout:
    for word in words:
        fout.write(word + '","')
