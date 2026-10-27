import socket
web_site =  input("Enter website: ")
ip = socket.gethostbyname(web_site)
print("IP address of", web_site, "is", ip)