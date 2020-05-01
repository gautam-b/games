"""
Create Soduku Image file from list of list
"""

import puzzle
from PIL import Image, ImageDraw, ImageFont


def draw_soduku(soduku=puzzle.evil, text="Soduku", file_name="soduku.png"):

    im_size = (380, 440)
    draw_area = (380, 380)
    bg_color = (255, 255, 255)  # white
    outline_color = (0, 0, 0)  # black
    line_width = 2
    padding = 10

    im = Image.new("RGB", im_size, bg_color)
    draw = ImageDraw.Draw(im)

    header_font = ImageFont.truetype("arial.ttf", size=40)
    number_font = ImageFont.truetype("arial.ttf", size=30)

    # Draw Lines
    for i in range(10):
        x0 = i * 40 + padding
        x1 = x0
        y0 = padding
        y1 = draw_area[0] - y0

        if not (i % 3):
            draw.line([x0, y0, x1, y1], fill=outline_color, width=line_width + 2)  # Vertical line
            draw.line([y0, x0, y1, x1], fill=outline_color, width=line_width + 2)  # Vertical line
        else:
            draw.line([x0, y0, x1, y1], fill=outline_color, width=line_width)  # Vertical line
            draw.line([y0, x0, y1, x1], fill=outline_color, width=line_width)  # Vertical line

    for i, row in enumerate(soduku):
        for j, item in enumerate(row):
            if item:
                x = i * 40 + padding + 12
                y = j * 40 + padding + 4
                draw.text((x, y), str(item), font=number_font, fill=outline_color)

    draw.text((20, 380), text, font=header_font, fill=outline_color)

    im.save(file_name)


if __name__ == "__main__":
    draw_soduku()
