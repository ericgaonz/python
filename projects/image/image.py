from PIL import Image, ImageDraw, ImageFont

def generate_numbered_image(number, output_path):
    image = Image.open('TICKET.jpg')

    # 在图像上绘制编号
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Arial.ttf', 50)  # 指定字体和字号
    text_color = (0, 0, 0)  # 黑色
    text_position = (888, 1350)  # 文本位置
    draw.text(text_position, 'NO. %s' % number, font=font, fill=text_color)

    # 保存图像
    image.save(output_path)

for i in range(1, 3):
    strNumber = '%03d' % i
    generate_numbered_image(strNumber, './images/TICKET-NO.%s.jpg' % strNumber)
