import sys
import os


def count(line, dic):
    words = line.split(" ")
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
dir = sys.argv[1]
content = ""
dic = {}

for file in os.listdir(dir):
    f = open(dir+"/"+file,"r",errors="ignore")
    file_line = f.read()
    count(file_line,dic)
    content = content + ' \r ' + file_line
    f.close()
f = open("sum","w")
f.write(content)
f.close()

cant = 0
for k,v in dic.items():
    cant += v
print("cant palabras total" + str(cant))
print("cant palabras unicas" + str(len(dic)))
print("a continuacion frecuencia de palabras " )
for k,v in dic.items():
    print(" {} -> {}".format(k,v))