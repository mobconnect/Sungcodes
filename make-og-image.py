from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
OUTPUT = Path("og-image.png")

image = Image.new("RGB", (WIDTH, HEIGHT), "#24163e")
draw = ImageDraw.Draw(image)

top = (36, 22, 62)
bottom = (112, 66, 196)

for y in range(HEIGHT):
    ratio = y / (HEIGHT - 1)
    colour = tuple(
        round(top[i] + (bottom[i] - top[i]) * ratio)
        for i in range(3)
    )
    draw.line((0, y, WIDTH, y), fill=colour)

draw.ellipse((850, -160, 1370, 360), fill="#9b6bcb")
draw.ellipse((-230, 430, 270, 930), fill="#633795")
draw.ellipse((920, 420, 1250, 750), fill="#c9a9f2")

font_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
]

regular_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
]

def get_font(paths, size):
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

brand_font = get_font(font_paths, 54)
title_font = get_font(font_paths, 76)
body_font = get_font(regular_paths, 32)
small_font = get_font(regular_paths, 24)

draw.rounded_rectangle(
    (82, 72, 158, 148),
    radius=18,
    fill="#ffffff"
)

draw.text(
    (120, 110),
    "S",
    font=brand_font,
    fill="#7042c4",
    anchor="mm"
)

draw.text(
    (184, 110),
    "Sungcodes",
    font=brand_font,
    fill="#ffffff",
    anchor="lm"
)

draw.text(
    (82, 245),
    "Find a code.",
    font=title_font,
    fill="#ffffff"
)

draw.text(
    (82, 330),
    "Write something new.",
    font=title_font,
    fill="#e9cfff"
)

draw.text(
    (86, 455),
    "Music & Lyrics Studio",
    font=body_font,
    fill="#f2eafb"
)

draw.text(
    (86, 525),
    "Discover music codes • Create original song drafts",
    font=small_font,
    fill="#e7dcef"
)

image.save(OUTPUT, "PNG", optimize=True)
print(f"Created {OUTPUT} at {WIDTH}x{HEIGHT}")
