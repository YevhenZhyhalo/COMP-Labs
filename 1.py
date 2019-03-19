#! /usr/bin/python
import math
import os



def count_letters(filename):
	length = 0
	str1 = open(filename, 'r',encoding="ascii", errors="surrogateescape")
	for line in str1:
		length+=len(line)
	return length

def count_freq(filename):
	check_string = open(filename, 'r', encoding="ascii", errors="surrogateescape")
	count = {}
	for line in check_string:
		for word in line:
			  if word in count:
				    count[word] += 1
			  else:
		    		count[word] = 1
	return count

def count_chances(count, sum):

	chanses = {}
	for letter in count:
			  chanses[letter] = count[letter]/sum


	return chanses



def print_mass(count):
	for key in count:
	  	if count[key] > 0:
	    		print("{0} = {1}".format(repr(key) ,count[key]))

def count_entropy(filename):
	entr=0
	freqs=count_freq(filename)
	sum=count_letters(filename)
	chanses=count_chances(freqs,sum)


	#print_mass(chanses)#OUTPUT OF CHANSES


	for key in chanses:
		entr+= -chanses[key]*math.log(chanses[key],2)

	return entr

def compare(filename):
	print('------------------' + filename + '.txt.gz--------------------')
	entropy=count_entropy(filename + '.txt.gz')
	entropy_lenght=count_letters(filename + ".txt.gz")*entropy
	file_length=os.path.getsize(filename + ".txt.gz")
	#arc1=os.path.getsize(filename + ".tar")
#	arc2=os.path.getsize(filename + ".txt.gz")
	#arc3=os.path.getsize(filename + ".zip")
	print('entropy                               ',round(entropy,3))
	print('letters counter                       ',count_letters(filename + ".txt"))
	print('infomation aproach (bytes)          ',round(entropy_lenght/8 ,3))
	print('file length(bytes)                    ',file_length)
	#print('tar(bytes)                            ',arc1)
	#print('gz(bytes)                             ',arc2)
	#print('zip(bytes)                            ',arc3)



##print('Show Path To file')

compare('tigerbase')
compare('evangeliebase')
compare('ugandabase')
