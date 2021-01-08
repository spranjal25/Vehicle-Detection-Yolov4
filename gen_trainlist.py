import os
img_files = []
print(os.getcwd())

os.chdir(os.path.join('data').os.path.join('obj'))

print(os.getcwd())
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.jpg'):
        img_files.append('data/data/obj/' + filename)
os.chdir('..')
print(os.getcwd())
with open('train.txt', 'w') as outfile:
    for image in img_files:
        outfile.write(image)
        outfile.write('\n')
    outfile.close()
# os.chdir('master')
print(os.getcwd())