from os.path import join
import sys
from glob import glob
from ntpath import basename

# Need two arguments
if len(sys.argv) != 3:
	print 'Invalid number of arguments passed'
	print '2 arguments expected, first argument is the installed directory, second is the source directory'
	exit(1)

# First argument is where symengine header files are installed.
install_dir = sys.argv[1]

# Second argument is folder containing symengine header files.
symengine_dir = sys.argv[2]

installed_files = [basename(x) for x in glob(join(install_dir, '*.h'))]
print 'Total number of installed header files : %d' % len(installed_files)

all_files = [basename(x) for x in glob(join(symengine_dir, '*.h'))]
print 'Number of header files to be installed : %d' % len(all_files)

# res = True if all are installed
res = True

for fl in all_files:
    if not fl in installed_files:
        print '%s is not installed!' % fl
        res = False

if res:
    print 'All header files are installed!'
    exit(0)
else:
    exit(1)
