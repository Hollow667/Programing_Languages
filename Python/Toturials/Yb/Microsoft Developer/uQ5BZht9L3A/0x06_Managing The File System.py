## Working with paths
from pathlib import Path

# Where am I?
cwd = Path.cwd()
print(cwd)
               
# Combine parts to create full path and file name
new_file = Path.joinpath(cwd, 'new_file.txt')                         
print(new_file)

# Dies this exist?
print(new_file.exists())


## working with directories
from pathlib import Path
cwd = Path.cwd()

# Get the parrent directory
parent = cwd.parent

# Is this a directory?
print(parent.is_dir())

# Is this a file
print(parent.is_file())

# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)

## Working with files
from pathlib import Path
cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# Get the file name
print(demo_file.name)

# Get the extension
print(demo_file.suffix)

# Get the folder
print(demo_file.parent.name)

if(demo_file.exists()):
    # Get the size
    print(demo_file.stat().st_size)
else:
    print('File ' + demo_file.absolute().__str__() +  ' does not exits')
