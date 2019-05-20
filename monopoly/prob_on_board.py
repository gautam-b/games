from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def draw_prob(nums=None, file_name="test.jpg"):
    # img = Image.open("monopoly-board-web.jpg")
    img = Image.open("monopoly_original.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=14)

    if not nums:
        nums = list(range(1, 41))

    bottom_right = f"{nums[0]:.2f}%"
    bottom_left = f"{nums[10]:.2f}%"
    top_left = f"{nums[20]:.2f}%"
    top_right = f"{nums[30]:.2f}%"

    bottom_row = nums[1:10]
    left_col = nums[11:20]
    top_row = nums[21:30]
    right_col = nums[31:40]

    # draw bottom row
    bottom_row.reverse()
    for i, text in enumerate(bottom_row):
        x = (i + 1) * 70 + 80
        y = 760
        text = f"{text:.2f}%"
        draw.text((x, y), text, fill=(255, 0, 0), font=font)

    # draw top row
    left_col.reverse()
    for i, text in enumerate(top_row):
        x = (i + 1) * 70 + 80
        y = 125
        text = f"{text:.2f}%"
        draw.text((x, y), text, fill=(255, 0, 0), font=font)

    # draw left column
    for i, text in enumerate(left_col):
        x = 125
        y = (i + 1) * 70 + 90
        text = f"{text:.2f}%"
        draw.text((x, y), text, fill=(255, 0, 0), font=font)

    # draw right column
    for i, text in enumerate(right_col):
        x = 730
        y = (i + 1) * 70 + 90
        text = f"{text:.2f}%"
        draw.text((x, y), text, fill=(255, 0, 0), font=font)

    # draw four corners
    draw.text((10, 90), top_left, fill=(255, 0, 0), font=font)  # top left
    draw.text((845, 90), top_right, fill=(255, 0, 0), font=font)  # top right
    draw.text((10, 880), bottom_left, fill=(255, 0, 0), font=font)  # bottom left
    draw.text((850, 860), bottom_right, fill=(255, 0, 0), font=font)  # bottom right

    img.save(file_name)


if __name__ == "__main__":
    draw_prob()
