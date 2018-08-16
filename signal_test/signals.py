from blinker import Namespace

namespace = Namespace()

login_signal = namespace.signal('login')

def login_log(sender):
	print('user is login')

login_signal.connect(login_log)
	
