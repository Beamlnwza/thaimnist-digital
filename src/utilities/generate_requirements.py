import subprocess

# Run the pip freeze command to get a list of installed packages
result = subprocess.run("pip freeze", stdout=subprocess.PIPE, shell=True)

# Split the output into a list of package names
packages = result.stdout.decode("utf-8").strip().split("\n")

# Write the list of packages to a requirements.txt file
with open("requirements.txt", "w") as f:
    f.write("\n".join(packages))

print("The requirements.txt file has been generated.")