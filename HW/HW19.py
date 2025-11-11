file_names = ['file1.py', 'file2.txt', 'file3.pptx', 'file4.doc']

for file_split in file_names:
    print('%s => 파일명 : %s, 확장자 : %s' % (file_split, file_split[:file_split.index('.')], file_split[file_split.index('.'):]))