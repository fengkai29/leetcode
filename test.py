# import shutil,os
# new_path='/root/python_test/data/gp_fz'
# for derName, subfolders, filenames in os.walk('/root/python_test/data/gp'):
#     for i in filenames:
#         if i.endswith('.jpg'):
#             shutil.copy(os.path.join(derName,i),os.path.join(new_path,i))


# import base64
# import cv2
# from PIL import Image
# from io import StringIO, BytesIO
#
# with open('/Users/fengkai/Desktop/train_test_ori/group1_M00_00_2A_rBIeXFwoN8SAE314AADp3opfXq0628.jpg','rb') as f:
#     base64_data = base64.b64encode(f.read())
#     s = base64_data.decode()
#     print(s)
#     imgdata = base64.b64decode(s)
#     img = Image.open(BytesIO(imgdata))
#     img = img.convert('RGB')
#     img.show()

# matrix =[
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
#
# print(matrix[3][1])
#image转base64
# import base64
# with open("C:\\Users\\wonai\\Desktop\\1.jpg","rb") as f:#转为二进制格式
#     base64_data = base64.b64encode(f.read())#使用base64进行加密
#     print(base64_data)
#     file=open('1.txt','wt')#写成文本格式
#     file.write(base64_data)
#     file.close()
#
# import os, base64
#
# with open("C:\\Users\\wonai\\Desktop\\1.txt", "r") as f:
#     # str = "iVBORw0KGgoAAAANSUhEUgAAANwAAAAoCAIAAAAaOwPZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQuSURBVHhe7ZptmoMgDIR7rh6o5+lpvEwP01XUGshAokgX+8z+7PKRTF6SoN7e/KMCnSlw68wemkMF3oSSEHSnAKHsLiQ0iFCSge4UIJTdhYQGEUoy0J0ChLK7kNAgQkkGulOAUHYXEhpEKMlAdwpcG8rhcRv/HkN3stIgW4F88DYoX89nObjmANuOc0eMXpHHcyX9+mowhgHKmdlChM0BZzvzet6DSSW7xjEWk8Hu+/O1x7zF1237/Uu4t/O46V6sZuARoZb9KqbO7On4rJlykqcYYnNAjSbx3Gmrj6WTzxirVlA+90F82G+nm4fX3zOxgqyKqRaUU7b8FpRDOeyjJa7k5oByT1yWse4mxfDC3NrrprnQtQeUMuUXoURmCGHdKfl/oTS8MElxu2mudO0BXUCZL8efVGU0EmsQjkGpM2H8y/CwGtW1C3el8ywxhHKWxgOlaPNj0VcRRW+OoiKvCXF0o6YeXWLQDaNQyMf1Clhsi22D9HUNXOBCVZamaBmiO5BxRdRQOt3M3oFUAD4/HDolSChx7AvXzRIJQtgsUfMu6HB+HglNLc5d5KiwpcAqTH7Idk/lvLD9Z0rUx4vYWL2UJ4WY6XbdL91ML57+EjsRNEMnw/LCrKklN9NNkbuLvKsdabjM/ZMByh+PDWuuw6kDEYXPzeSfzGARlNG1M1ENRCfGLlUuJ5MVTg+UyxGzC+1+KN/DkDyuTSVbqo7vNnagfKPTrH9b8pQtgQ/PRCifDTaUJaIWw8adUycklLrcppkyCZfkJ5cYlSZnQTkmsYf58OYAlMpg6JnlhYlC9uxhIdWvbr1NS8Ahc9pgQlkkai3fOorVUK4JGeYTJIgVTm+mnCqrmSfOgDJ0mOlOlhcmClk3M0KmPzeF0mnDGVB6LjqbmKB8p5GRQ34DStRCdpEpp5MRNWRNocwsjk9i7nyqugzPYTWUSZuqe0qVucAT5tgH9ITmxEdCdihjpcCVAgfI8uJ4pgx3K3UhgBeRQ9dtbJmjp1TnYmsKoSH1UGqKE23mxlrsri4yKsuAFnZ5BrAugypw0/IdSvHmxHJbEI6lREzj0asuOc7TR8BONdd9pNKCo4LRNY9CdgCEXjqObDhQvsFpy7z7DsqHP9khxp9DzNeKbSR+Iy3/n31tqVFYe17xFUZkTu507+4px4USFwBRm32lbzFyXphgRMtn3cwqqaef8a0UrMHlaJYM8RC1Iq2DeOXvKUdVjALmzromST8+4N+Egm9rrwzl/DpAVlddnE9su36Jyx6ECtkUxufaUMJOzfwQsxldUbnTLyO/ckCcNsS112yDmkkGF/4xKL8rHndrowChbKMrV61QgFBWiMepbRQglG105aoVChDKCvE4tY0ChLKNrly1QgFCWSEep7ZRgFC20ZWrVihAKCvE49Q2ChDKNrpy1QoF/gDXIhmWmc+CSAAAAABJRU5ErkJggg=="
#     imgdata = base64.b64decode(f.read())
#     file = open('1.jpg', 'wb')
#     file.write(imgdata)
#     file.close()
#

# def Add(num1,num2):
#         while (num2!=0):
#             temp = num1^num2
#             num2 = (num1&num2)<<1
#             num1 = temp
#         return num1
# m = 9
# j = 8
#
# print(Add(m,j))
# s = '2e24'
# t = s[0:2]
# print(t[::-1])
# flag = 0
# a = [0]
# if flag not in a:
#     print(1)

# m = int(input())
#
# for i in range(m):
#     b = []
#     a = int(input())
#     x = [n+1 for n in range(a)]
#     x.reverse()
#     b.append(x[0])
#     for j in range(1,a):
#         temp = b[len(b)-1]
#         del b[len(b)-1]
#         b.insert(0,temp)
#         b.insert(0,x[j])
#     tem = b[a-1]
#     del b[a-1]
#     b.insert(0,tem)
#     for k in range(len(b)-1):
#         print(b[k],end=' ')
#     print(b[len(b)-1])
# x = 500
# countx = 0;
# while x:
#     countx += 1
#     x = x & (x - 1)
#
# print(countx)

# a = [[0,10,0],[0,0,0]]
# print(a[0].count(0))

# import sys
#
# line = sys.stdin.readline().strip()
# line1 = list(map(int, line.split()))
#
# a = []
# for i in range(line1[0]):
#     line = sys.stdin.readline().strip()
#     line2 = list(map(int, line.split()))
#     a.append(line2)
#
# for i in range()
# s = '1 2 3'
# ls = list(s.split(' '))
# print(ls)
import numpy as np

a = np.array([[[1,2],[2,3]],[[1,2],[4,5]]])
a = a.reshape(4,2)
print(a)


