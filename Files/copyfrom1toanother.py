
#Open one file (here = job.txt) and read the content of the file.
# Then create a new file and copy the content (first 10 letter/character) of 1st file to the newly created file.

with open("job.txt") as myfile:
    content = myfile.read()

with open("copyofjob.txt",'w') as file :
    file.write(content[:10])