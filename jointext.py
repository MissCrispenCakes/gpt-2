# Get list of file Names
import glob
filenames = glob.glob("*.txt") # Add all texts into one file
with open('corpus.txt', 'w') as outfile:
       for fname in filenames:
            with open(fname) as infile:
                  outfile.write(infile.read())
outfile.close()