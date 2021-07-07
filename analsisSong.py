song = ['동해물과 백두산이 마르고 닳도록\n',
'하느님이 보우하사 우리나라 만세\n',
'무궁화 삼천리 화려강산\n',
'대한사람 대한으로 길이 보전하세\n']

with open('song.txt', 'w') as f:
    f.writelines(song)
f.close()

with open('song.txt', 'r') as file:
  with open('newSong.txt', 'w') as newfile:
    wordCount = 0 
    lineNum = 0
    for line in file: 
      stripLine = line.strip()
      print(stripLine)
      lineNum += 1
      newfile.write(f'{lineNum} : {stripLine}\n')
      for word in stripLine.split(' '):
        wordCount += 1
    print('단어의 수 :', wordCount)
  newfile.close()
file.close

with open('newSong.txt', 'r') as newfile:
  line = newfile.read()
  print(line)
newfile.close()