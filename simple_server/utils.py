import time

def log(*args, **kwargs):
	format: str = '%Y/%m/%d %H:%M:%S'
	value = time.localtime(int(time.time()))
	dt = time.strftime(format, value)
	print(dt, *args, **kwargs)
