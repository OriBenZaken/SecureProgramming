
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
		"""
		In order to get the original plaintext we need to get the original output of
		AES the which for the plaintext encryption.
		In this way: ciphertext ^ AES_output_for_enc = plintext.
		We do it by write to the cloud '\x00' bytes from byte in position 0 until byte in position len(ciphertext).
		The cloud will xor the zeros with the AES_output_for_enc and this way we get eventually the 
		AES_output_for_enc as the new ciphertext in the cloud.
		In each write operation we aggregate the old ciphertext.
		At the final step - we read the new ciphertext, which is AES_output_for_enc and xor it with the old
		ciphertext. This is how we get the original plaintext.
		"""
		while old_enc_byte:
			old_ciphertext += old_enc_byte
			new_ciphertext += cloud.Read(position=i)
			i += 1
			old_enc_byte = cloud.Write(position=i, newbyte=b'\x00')

		pt = "".join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(old_ciphertext,new_ciphertext))
		file.write(pt)