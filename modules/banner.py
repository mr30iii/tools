import os
from PIL import Image, ImageDraw, ImageFont
from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

FONT_FILE = "esternal.sharp.ttf"  # Your TTF font
TEXT_SIZE = 100
CREDIT_SIZE = 40
MAX_WORDS = 4
FOLDER_NAME = "RAJA-TOOLS"

# --------- USER INPUT ----------
print(Fore.CYAN + "\n==============================")
print(Fore.CYAN + "     RAJA-X TERMINAL + IMAGE BANNER")
print(Fore.CYAN + "==============================\n")

text = input(Fore.GREEN + "Enter your banner text (max 4 words): ").strip()

if len(text.split()) > MAX_WORDS:
    print(Fore.RED + "❌ Error: Only 4 words allowed!")
    exit()

# --------- TERMINAL BANNER ----------
f = Figlet(font="slant")
banner_text = f.renderText(text)
print(Fore.GREEN + banner_text)
print(Fore.MAGENTA + "Credit: RAJA\n")

# --------- IMAGE BANNER ----------
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

img_width = max(1200, len(text)*200)
img_height = 400
img = Image.new("RGB", (img_width, img_height), color=(0,0,0))
draw = ImageDraw.Draw(img)

# Load fonts
try:
    font = ImageFont.truetype(FONT_FILE, TEXT_SIZE)
    credit_font = ImageFont.truetype(FONT_FILE, CREDIT_SIZE)
except:
    print(Fore.RED + "TTF Font not found, using default font.")
    font = ImageFont.load_default()
    credit_font = ImageFont.load_default()

# Draw banner text
bbox = draw.textbbox((0,0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
draw.text(((img_width-text_width)/2, (img_height-text_height)/2 - 40),
          text, font=font, fill=(0,255,0))

# Draw Credit in image
credit = "Credit: RAJA"
bbox_credit = draw.textbbox((0,0), credit, font=credit_font)
cw = bbox_credit[2] - bbox_credit[0]
ch = bbox_credit[3] - bbox_credit[1]
draw.text(((img_width-cw)/2, img_height-ch-20), credit, font=credit_font, fill=(255,0,255))

# Save image
image_path = os.path.join(FOLDER_NAME, f"{text.replace(' ','_')}_banner.png")
img.save(image_path)

print(Fore.CYAN + f"\n✅ Banner Image Created Successfully!")
print(Fore.CYAN + f"Saved at: {image_path}\n")
