from PIL import Image, ImageDraw

picture = Image.new("RGB",(960, 540), (255,255,255))
paint = ImageDraw.Draw(picture)

with open(r"C:\Users\Admin\Desktop\laba2\DS5.txt", "r") as file:
    for numbers in file:
        y_x = numbers.split()
        y = int(y_x[0])
        x = int(y_x[1])
        paint.point((x,y), fill=(0, 0, 0))

picture.show()
picture.save("finalpicture.png")