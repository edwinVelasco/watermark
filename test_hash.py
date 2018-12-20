import hashlib
pdf = open('p.pdf', 'rb')
data = pdf.read()
pdf.close()

#print(data)
#print('\n')
sha1 = hashlib.sha1(data)
print(sha1.hexdigest())
print(len(sha1.hexdigest()))
print('\n')

sha224 = hashlib.sha224(data)

print(sha224.hexdigest())
print(len(sha224.hexdigest()))
print('\n')