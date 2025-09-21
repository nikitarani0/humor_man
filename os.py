# 1. Current dir, list files
import os
print("CWD:", os.getcwd())
print("Files:", os.listdir("."))

# 2. Absolute path, check exists
print("Abs path:", os.path.abspath("data.txt"))
print("Exists:", os.path.exists("data.txt"))

# 3. Create / remove directory
os.makedirs("testdir", exist_ok=True)   # create
os.rmdir("testdir")                      # remove (empty dir)

# 4. File size and permissions
st = os.stat("data.txt")
print("Size bytes:", st.st_size)
print("Mode:", oct(st.st_mode))
# check read permission:
print("Readable?", os.access("data.txt", os.R_OK))

# 5. Walk directory & count files and total lines
total_files = 0
total_lines = 0
for root, dirs, files in os.walk("."):
    for f in files:
        total_files += 1
        with open(os.path.join(root, f), "r", errors="ignore") as fh:
            total_lines += sum(1 for _ in fh)
print("Files:", total_files, "Lines:", total_lines)

# 6. Run a shell command (example: ls)
import subprocess
proc = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(proc.stdout)
