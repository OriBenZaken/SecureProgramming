
from cloud import *

def breakcloud(cloud):
	"""
	receives 'cloud', an object of type Cloud.
	creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
	you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
	"""
	old_ciphertext = ""
	new_ciphertext = ""
	with open("plain.txt", "wb+") as file:
		i = 0
		old_enc_byte = cloud.Write(position=i, newbyte=b'\x00')
		while old_enc_byte:
			old_ciphertext += old_enc_byte
			new_ciphertext += cloud.Read(position=i)
			i += 1
			old_enc_byte = cloud.Write(position=i, newbyte=b'\x00')

		pt = "".join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(old_ciphertext,new_ciphertext))
		file.write(pt)