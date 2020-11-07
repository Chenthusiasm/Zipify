import os

for root, dirs, files in os.walk("."):
    print("root: ", root, "\n")
    print("directories:\n")
    for d in dirs:
        print("\t", d)
    print("files:\n")
    for f in files:
        print("\t", f)
