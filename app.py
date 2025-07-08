from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route("/review-card")
def review_card():
    name = request.args.get("name", "Friend")

    # Create image
    img = Image.new("RGB", (768, 768), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load font
    font_path = "arial.ttf"
    try:
        font = ImageFont.truetype(font_path, 40)
    except:
        font = ImageFont.load_default()

    # Add text
    message = f"Hi {name}, ready to grow your reviews with Prymeta?"
    draw.text((50, 100), message, fill="black", font=font)

    # Add "Leave us a review!" button look
    draw.rectangle([(50, 200), (500, 260)], fill="white", outline="black")
    draw.text((60, 210), "Leave us a review!", fill="black", font=font)

    # Save image
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype="image/png")

if __name__ == "__main__":
    app.run()
