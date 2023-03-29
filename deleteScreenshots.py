import os, magic

def find():

	for root, dirs, files in os.walk(os.path.dirname(os.getcwd()):
		for name in files:
			try:
				if "Screenshot" in name and ".ktx" in name:
					os.remove(name)
			except:
				continue
	return




find()

