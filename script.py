import time, glob, shutil

outfilename = 'all_' + str((int(time.time()))) + ".tex"

filenames = glob.glob('*.tex')

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.tex'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
