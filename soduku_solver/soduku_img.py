"""
Create Soduku Image file from list of list
"""

import puzzle
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


cwd = Path(__file__).parent


def blank_soduku(filename="soduku_blank.png"):
    """Create blank soduku image
    """
    im_size = (380, 440)
    draw_area = (380, 380)
    bg_color = (255, 255, 255)  # white
    outline_color = (0, 0, 0)  # black
    line_width = 2
    padding = 10

    im = Image.new("RGB", im_size, bg_color)
    draw = ImageDraw.Draw(im)

    # Draw Lines
    for i in range(10):
        x0 = i * 40 + padding
        x1 = x0
        y0 = padding
        y1 = draw_area[0] - y0

        if not (i % 3):
            width = line_width + 2
        else:
            width = line_width

        draw.line([x0, y0, x1, y1], fill=outline_color, width=width)  # Vertical lines
        draw.line([y0, x0, y1, x1], fill=outline_color, width=width)  # Horizontal lines

    filepath = cwd / filename
    im.save(filepath)


def draw_soduku(soduku=puzzle.evil, text="Soduku", file_name="soduku.png"):
    """draw numbers on blank soduku image
    """
    outline_color = (0, 0, 0)  # black
    padding = 10

    header_font = ImageFont.truetype("arial.ttf", size=40)
    number_font = ImageFont.truetype("arial.ttf", size=30)

    # Check if blank soduku image exits
    blank_soduku = cwd / "soduku_blank.png"
    if not (blank_soduku.exists() or blank_soduku.is_file()):
        blank_soduku()

    im = Image.open(blank_soduku)
    draw = ImageDraw.Draw(im)

    for i, row in enumerate(soduku):
        for j, item in enumerate(row):
            if item:
                x = i * 40 + padding + 12
                y = j * 40 + padding + 4
                draw.text((x, y), str(item), font=number_font, fill=outline_color)

    text_size = draw.textsize(text, font=header_font)
    draw.text((int((im.size[0] - text_size[0]) / 2), 380), text, font=header_font, fill=outline_color)

    im.save(file_name)
    # im.show()


if __name__ == "__main__":
    draw_soduku()
