from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    message = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if chr(b) == "#" and message[-4:] == "####":
                return message[:-4]
            message += chr(b)
    return message

print("Decoded message:", decode_image("encoded_image.png"))
