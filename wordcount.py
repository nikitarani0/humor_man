with open("data.txt","r") as f:
    data = f.read()
lines = data.split("\n")
words = data.split()
chars = len(data)
print(len(lines))
print(len(words))
print(chars)