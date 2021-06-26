fpw = open('temp.txt', 'w')  # opening
contentw = fpw.write('Hey! This is Python Tutorial.')
fpw.close()

fp = open('temp.txt', 'r')   # opening
content = fp.read()          # reading
print(content)
fp.close()