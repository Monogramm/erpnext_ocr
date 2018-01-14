from PIL import Image
import pytesseract

# im = Image.open("sample1.jpg")
im = Image.open("Picture_010.tif")

text = pytesseract.image_to_string(im, lang = 'eng')

# print(text)
# for t in text:
#     print t
text.split(" ")

print(text)
text_list = []
string = ""
# for t in text:
#     if t != " " and t != "\n":
#         string += t
#     else:
#         text_list.append(string)
#         string = ""
#
# print text_list
# for t in text_list:
#     print t
