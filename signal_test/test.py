from blinker import Namespace

namespace = Namespace()

login_signal = namespace.signal('login')

def login_log(sender):
	return 'this is a test'

login_signal.connect(login_log)
