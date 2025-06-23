from PIL import Image

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Add a delimiter to mark end of message
    message += "#####"

    for row in range(height):
        for col in range(width):
            if index < len(message):
                r, g, b = img.getpixel((col, row))
                ascii_val = ord(message[index])
                encoded.putpixel((col, row), (r, g, ascii_val))
                index += 1

    encoded.save(output_path)
    print("✅ Encoding complete. Image saved as", output_path)

encode_image("original_image.png", "This is a secret message", "encoded_image.png")