from itertools import chain
import os
import sys

print("Do you want to search file.")
print ("1. word list in the dictory")
print ("2. On the basis extension")
A = float(input("Enter the choice: "))
x = ('Bomb','bomb','Vl sem B.Sc.(Hon) F S Time Table','CONTENTS copy')
Document = ('.docx','.pdf','doc','csv','.xlsx','.xlsm','.xlsb','.xltx','.xltm','.xls','.xlt','.xls','.xml','.xlam')
Image = ('.apng','.avif','.gif','.jpg','.jpeg','.jfif','.pjpeg','.pjp','.png','.svg','.webp','.bmp','.ico','.cur','.tif','.tiff','.heic')
Video = ('.mp4','.mov','.wmv','.avi','.avchd','.flv','.f4v','.swf','.mkv')
Rape = ()
Murder = ()
Terrorism = ()
paths = ('C:','D:')

if (A == 1):
    print("Which Case")
    print("1.Murder")
    print("2.Rape")
    print("3.Terrorism")
    Madhu = float(input("Enter Your Choice: "))
    Z = open('D:\Outputs\Murder\output.txt','w+')
    sys.stdout = Z
    if (Madhu == 1):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.startswith(Murder):
                    print(os.path.join(root, file))
    Z.close()
    N = open('D:\Outputs\Rape\output.txt','w+')
    sys.stdout = N
    if (Madhu == 2):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.startswith(Rape):
                    print(os.path.join(root, file))
    N.close()
    I = open('D:\Outputs\Terrorism\output.txt','w+')
    sys.stdout = I
    if (Madhu == 3):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.startswith(x):
                    print(os.path.join(root, file))
    I.close()
if (A==2):
    print("Which File type you want to search")
    print("1.Picture")
    print("2.Document")
    print("3.Video")
    D = float(input("Enter Choice: "))
    L = open('D:\Outputs\Picture\output.txt','w+')
    sys.stdout = L
    if (D == 1):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.endswith(Image):
                    print(os.path.join(root, file))
    L.close()
    M = open('D:\Outputs\Document\output.txt','w+')
    sys.stdout = M
    if (D == 2):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.endswith(Document):
                    print(os.path.join(root, file))
    M.close()
    Q = open('D:\Outputs\Video\output.txt','w+')
    sys.stdout = Q
    if (D==3):
        for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
            for file in files:
                if file.endswith(Video):
                    print(os.path.join(root, file))
    Q.close()
