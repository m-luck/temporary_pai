import sys
file = sys.argv[1]
new_file = sys.argv[2]
with open(file) as f, open(new_file, "w+") as to:
   firstColumn = [line.split(',')[0] for line in f] 
   to.write(str(firstColumn))
        