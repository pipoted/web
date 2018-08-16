import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'g.cn'
port = 80

s.connect((host, port))

ip, port = s.getsockname()
print('本机ip和port{}{}'. format(ip, port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)

request = http_request.encode('utf-8')
print('请求', request)
s.send(request)


response = s.recv(1024)

print('相应', response)
print('相应的str格式', response.decode('utf-8'))

