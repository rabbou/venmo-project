import re
import emoji 

def user_to_csv(fname,suffix,name_delta):
	return;

def reduce_trnx(fname,suffix,name_delta):
	return;

def validate_usr(orig,new):
	return;


def replace_emoji(fname,suffix,name_delta):
	f = open(fname,"r")
	newlines = []
	for line in f:
		newlines.append(emoji.demojize(line))
	f.close()
	print("done iterating through the original")

	split_ind = (len(suffix) + 1)*-1
	mod_fname = fname[:split_ind] + name_delta + fname[split_ind:]

	print("beginning to write to {}".format(mod_fname))
	f2 = open(mod_fname,"w")
	for a in newlines:
		f2.write(a)
	f2.close()

	print("done")
	return;

def reduce_data(fname,suffix,name_delta):
	unproc = set()

	pcount = 0
	f = open(fname,"r")
	for x in f: 
		pcount += 1
		temp = tuple([y.strip() for y in x.split(",")])
		unproc.add(temp)
		print(temp)
	f.close()

	split_ind = (len(suffix) + 1)*-1
	mod_fname = fname[:split_ind] + name_delta + fname[split_ind:]
	
	g = open(mod_fname,"w")
	acount = 0
	popped = 1
	try: 
		while(popped):
			popped = unproc.pop()
			g.write("{}\n".format(popped))
			acount+=1
	except KeyError: 
		g.close()
		print("wrote reduced form to new file: {}".format(mod_fname))
		print("length of the new set {}".format(acount))
		print("length of the old set {}".format(pcount))
	return;

def validate(orig,new):
	print("test")
	f1 = open(orig, "r")
	s1 = set()
	for line1 in f1:
		s1.add(line1.strip())
	f1.close()

	f2 = open(new, "r")
	s2 = set()

	for line2 in f2:
		s2.add(line2.strip())
	f2.close()

	print("length of set in f1 = {}".format(len(s1)))
	print("length of set in f2 = {}".format(len(s2)))
	a = (s2 ^ s1)
	print("differences in original and new= {}".format(len(a)))
	if(a == set()):
		print("It seems that the new file has the same set!")
	return;


if __name__ == "__main__":
	# reduce_usr("/media/sf_E_DRIVE/data/test3.usrs","usr","_reduced")
	# validate_usr('a','b')
	# validate_usr("/media/sf_E_DRIVE/data/test3.usrs","/media/sf_E_DRIVE/data/test3_reduced.usrs")
	# replace_emoji('/media/sf__DRIVE/data/test3.trnx','trnx','_emojiless')

	# reduce_data('/media/sf_L_DRIVE/venmo-project/webscrapper/rone.usrs','usrs','_new')
	# validate('rone_new.usrs','tester')
	# reduce_data('rone.trnx','trnx','_new')
	validate('rone_new.trnx','tester.trnx')