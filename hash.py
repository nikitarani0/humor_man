import hashlib
pwd=input()
print(hashlib.md5(pwd.encode()).hexdigest())
print(hashlib.sha256(pwd.encode()).hexdigest())