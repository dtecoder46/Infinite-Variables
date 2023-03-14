stringx=""

lines=6

for line in range(0,lines):

  stringy=stringx.replace("x",str(line))
  
  stringy+="Hello"
  
  print(stringy)