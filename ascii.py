from PIL import Image
img=Image.open(r'c:\Users\PC\Desktop\proyecto-practica\header_right.png').convert('L')
img=img.point(lambda x: 255 if x > 200 else 0)
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)
w,h=img.size
target_w = 200
target_h = int(h * (target_w/w))
img = img.resize((target_w, target_h))
w,h=img.size
txt=''
for y in range(h):
    txt += ''.join('#' if img.getpixel((x,y)) > 128 else ' ' for x in range(w)) + '\n'
with open('ascii_hr.txt', 'w') as f:
    f.write(txt)
