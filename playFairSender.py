import socket
host='localhost'
port=12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
matrix=[['l','g','d','b','a'],['q','m','h','e','c'],['u','r','n','i','f'],['x','v','s','o','k'],['z','y','w','t','p']]
s1=""
def findIndex(a):
	for i in range(5):
		if a in matrix[i]:
			ind=matrix[i].index(a)
			return (i,ind)



pt=input("Enter Plaintext -> ")
ct=""
l=len(pt)
i=0
while i<l-1:
	if pt[i]==pt[i+1]:
		s1+=pt[i]+'x'
		i+=1
	else:
		s1+=pt[i]+pt[i+1]
		i+=2
if i==l-1:
	s1+=pt[i]
if len(s1)%2!=0:
	s1+='x'

cipher=""
for i in range(0,len(s1),2):
	lno1,i1=findIndex(s1[i])
	lno2,i2=findIndex(s1[i+1])
	if lno1==lno2:
		index1,index2=(i1+1),(i2+1)
		if index1==5:
			index1=0
		if index2==5:
			index2=0
		cipher+=chr(ord(matrix[lno1][index1])-32)
		cipher+=chr(ord(matrix[lno2][index2])-32)
	elif i1==i2:
		index1,index2=(lno1+1),(lno2+1)
		if index1==5:
			index1=0
		if index2==5:
			index2=0
		cipher+=chr(ord(matrix[index1][i1])-32)
		cipher+=chr(ord(matrix[index2][i2])-32)
	else:
		cipher+=chr(ord(matrix[lno1][i2])-32)
		cipher+=chr(ord(matrix[lno2][i1])-32)

print("Sending Encrypted Text "+cipher)
c.send(cipher.encode())
s.close()


