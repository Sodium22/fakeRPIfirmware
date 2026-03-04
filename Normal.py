"""
Normal mode will be used for all the normal processes and scripts the device will use and will  be the backend of the gui that will still be made
This script will access a folder where all scripts will go
scripts will have to have an indicator of what kind of script they are in a certain line so they can automatically be sorted between bluetooth wifi scanning sniffing and whatever else
more custom scripts will have to be added via code if they need their own category, they can still go into the same folder but have to have a custom indicator which has to be put into this
script and the gui



"""
import time
import os
from pathlib import Path

main = Path(__file__).parent
scripts = main / "Scripts"


C = {}
with open(scripts / "CodeTest.txt") as f:             #scripts for sniffing scanning wifi bluetooth and whatever else will be used/run like this using the exec function
    exec(f.read())





