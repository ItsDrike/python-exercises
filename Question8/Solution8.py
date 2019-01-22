import urllib.request
from PIL import Image

urllib.request.urlretrieve("https://picsum.photos/500/300?image=0", "image.jpg")

im = Image.open('image.jpg')
pix = im.load()
w, h = im.size
for x in range(w):
    for y in range(h):
        pix[x, y] = (255 - pix[x, y][0], 255 - pix[x, y][1], 255 - pix[x, y][2])
im.save('image.jpg')
