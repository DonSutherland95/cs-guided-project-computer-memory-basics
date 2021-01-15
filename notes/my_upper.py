def my_islower(c):
	cp = ord(c)
​
	"""
	if cp >= 97 and cp <= 122:
		return True
​
	else:
		return False
	"""
​
	#return cp >= 97 and cp <= 122
	return 97 <= cp <= 122
​
​
def my_upper(s):
	result = ""
​
	# send every chracter to my_islower
	for c in s:
		# if char is lowercase
		if my_islower(c):
			# get the ord value
			val = ord(c)
			# subtract 32
			val -= 32
			# convert value back to character
			c = chr(val)
​
		# add to result
		result += c
​
	# return result
	return result
​
a = "Hi There!"
​
print(my_upper(a))
​
"""
print(my_islower('a'))
print(my_islower('z'))
print(my_islower('A'))
print(my_islower('Z'))
print(my_islower('!'))
print(my_islower('~'))
print(my_islower(' '))
"""
​
"""
​
Unicode is the same as ASCII for the first 128 characters.
UTF-8 is the same as ASCII for the first 128 characters.
​
​
A 65
a 97
​
97-65 = 32
"""
​
"""
01100001 a
01100010 b
01100011 c
01100100 d
01100101 e
​
01000001 A
01000010 B
01000011 C
01000100 D
01000101 E
​
1 byte number: 0-255
2 byte number (16 bits): 0-65535
4 byte number (32 bits): 0-4294967295
8 byte number (64 bits): 0-18446744073709551615
"""