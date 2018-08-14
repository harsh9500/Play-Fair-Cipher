import socket
import random
host='localhost'
port=12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
cipher=s.recv(1024).decode()

matrix=[['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','T','P']]

def findIndex(a):
	for i in range(5):
		if a in matrix[i]:
			ind=matrix[i].index(a)
			return (i,ind)


decipher=""
for i in range(0,len(cipher),2):
	lno1,i1=findIndex(cipher[i])
	lno2,i2=findIndex(cipher[i+1])
	if lno1==lno2:
		index1,index2=(i1-1),(i2-1)
		if index1==-1:
			index1=4
		if index2==-1:
			index2=4
		decipher+=chr(ord(matrix[lno1][index1])+32)
		decipher+=chr(ord(matrix[lno2][index2])+32)
	elif i1==i2:
		index1,index2=(lno1-1),(lno2-1)
		if index1==-1:
			index1=4
		if index2==-1:
			index2=4
		decipher+=chr(ord(matrix[index1][i1])+32)
		decipher+=chr(ord(matrix[index2][i2])+32)
	else:
		decipher+=chr(ord(matrix[lno1][i2])+32)
		decipher+=chr(ord(matrix[lno2][i1])+32)


print("Decrypted text = "+decipher)