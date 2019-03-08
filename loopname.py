import os 
dir_path=[]
def walklevel(some_dir, level=0):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

dir_path= os.path.dirname(os.path.realpath('_file_'))
for root,dirs,files in walklevel(os.getcwd()):
	for rn in dirs:
		print rn
		
