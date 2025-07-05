# SCT_CYB_2 - Image Encryption / Decryption via Pixel Manipulation
# Author: Shivam Raj

from PIL import Image
import random

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    random.seed(key)

    # Swap pixel positions randomly
    for i in range(width):
        for j in range(height):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pixel1 = pixels[i, j]
            pixel2 = pixels[x, y]
            pixels[i, j], pixels[x, y] = pixel2, pixel1

    # Apply a basic operation: invert RGB
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # For simple invert-only, we can just re-invert.
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Invert back
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    # Re-swap pixels using same random sequence in reverse
    random.seed(key)
    swaps = []
    for i in range(width):
        for j in range(height):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            swaps.append(((i, j), (x, y)))

    for swap in reversed(swaps):
        (i, j), (x, y) = swap
        pixel1 = pixels[i, j]
        pixel2 = pixels[x, y]
        pixels[i, j], pixels[x, y] = pixel2, pixel1

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    image_path = input("Enter path to image file: ")
    key = input("Enter a secret key (number or string): ")
    output_path = input("Enter output file name (with .png/.jpg): ")

    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    elif choice == 'd':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Use 'e' or 'd'.")

if __name__ == "__main__":
    main()
# This code provides a simple image encryption and decryption tool using pixel manipulation.
# It allows users to encrypt an image by randomly swapping pixels and inverting colors, and then decrypt it by reversing these operations.