fin = open('words.txt', 'r')
words = fin.read().splitlines()
fin.close()


print(words)