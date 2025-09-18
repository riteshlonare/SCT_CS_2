from PIL import Image

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("=== Simple Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Use E or D.")
        return

    image_path = input("Enter the image filename (e.g., image.jpg): ")
    key = int(input("Enter encryption/decryption key (e.g., 25): "))
    output_path = input("Enter output filename (e.g., encrypted.png): ")

    if choice == 'E':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
