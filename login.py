#!/usr/bin/env python3
import cgi
import cgitb
import secret
import os
from http.cookies import SimpleCookie
from templates import login_page,secret_page,after_login_incorrect
cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")


print("Content-Type: text/html")
c = os.environ.get("HTTP_COOKIE")

cookie_pairs = c.split(";")
for p in cookie_pairs:
	key,value = p.split("=")
	if k == "username":
        c_username = value
    elif k == "password":
        c_password = value



cookie_ok = c_username == secret.username and c_password == secret.password
if cookie_ok:
	username = c_username
	password = c_password

form_ok = username == secret.username and password == secret.password
if form_ok:
	print("Set-Cookie: username=",username)
	print("Set-Cookie: password=",password)
print()
#print(login_page())
if not username and not password:
	print(login_page())
elif username == secret.username and password == secret.password:
	print(secret_page(username,password))
else:
	print(after_login_incorrect())


