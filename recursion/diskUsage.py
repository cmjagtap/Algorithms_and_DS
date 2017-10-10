#A recursive function for reporting disk usage of a file system.
import os
def disk_usage(path):
	total=os.path.getsize(path)
	if os.path.isdir(path):
		for file_name in os.listdir(path):
			childpath = os.path.join(path, file_name)
			total += disk_usage(childpath)
	print ( format(total), path)
	return total
print disk_usage('.')
