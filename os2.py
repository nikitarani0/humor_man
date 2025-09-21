import os
filename="check.txt"
if os.path.exists(filename):
    print(os.path.abspath(filename))
    print(os.path.getsize(filename))
else:
    with open(filename,"w") as f:
        f.write("")
