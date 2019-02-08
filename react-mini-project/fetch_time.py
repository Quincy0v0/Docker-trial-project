import os, datetime
fetched_dir = './fetched_info/'
if not os.path.isdir(fetched_dir):
	os.makedirs(fetched_dir)
with open(os.path.join(fetched_dir,'time.txt'),'wb') as f:
	f.write('%s\n'%datetime.datetime.now())
