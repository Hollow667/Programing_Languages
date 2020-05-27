# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespaces
from helpers import display
display('Not a warning')

## installing packages
'''
# Install an individual package
pip install colorama
# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama
'''

## Creating a virtual environment
'''
# Install virtual environment
pip install virtualenv

# Windows systems
python -m venv <folder_name?

# OSX/Linux (bash)
virtualenv <folder_name>
'''

## Using virtual environments
'''
# Windows systems
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell
../<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate
'''

