import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=True)

# mc.set('username', 'xiao', time=120)

mc.set_multi({
	'username': 'xiao',
	'age'     : 12,
	'password': 'xzx199110'
}, time=120)

username = mc.get('username')
mc.delete('username')
username2 = mc.get('username')
print(username2)
