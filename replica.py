import sys
import os.path
import dirsync

# The double backslash is required in the path name
# as the backslash is an escape character in Python

# Parsing the command line
if os.path.isdir(sys.argv[1])
    origin = sys.argv[1]
else:
    raise ValueError

if os.path.isdir(sys.argv[2])
    replica = sys.argv[2]
else:
    raise ValueError

# Add scheduler

# Add dirsync options
