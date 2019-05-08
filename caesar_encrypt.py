def caesarCipherEncryptor(string, key):
    # Write your code here. ord(letter) = ascii value of letter
	str_new = ""
	for char in range(len(string)):
		temp = string[char]
		if((ord(temp) + key) > ord("z")): #if a wrap-around is needed
			if(key > 26): #if multiple wrap-arounds are needed
				key = key%26
				num = ord(temp) + key
				str_new += chr(num)
			else:
				diff = (ord(temp) + key) - ord("z") #if only one wrap-around is needed
				num = ord("a") + diff - 1
				str_new += chr(num)
		else:
			#normal (no BC)
			num = ord(temp) + key
			str_new += chr(num)
	print(str_new)
	return str_new