import struct

#pack()
#unpack()

valores = (4,10,5.4,10.8)
# i mayuscula es integer sin signo
s = struct.Struct("II ff")
packed = s.pack(*valores)
file = open("bin.bin","wb")
file.write(packed)
file.close()


#leo
file_read = open("bin.bin","rb")
file_read.seek(0)   #me posiciono
content = file_read.read()
data = s.unpack(content)
print(data)