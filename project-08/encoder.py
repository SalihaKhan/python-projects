import base64

# -----------------------------
# 1. Encoding Function
# -----------------------------
def encode_text(text: str, shift: int = 3) -> str:
    # Step 1: Shift characters
    shifted = ''.join(chr((ord(char) + shift) % 256) for char in text)
    # Step 2: Base64 encode
    encoded_bytes = base64.b64encode(shifted.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

# -----------------------------
# 2. Decoding Function
# -----------------------------
def decode_text(encoded_text: str, shift: int = 3) -> str:
    # Step 1: Base64 decode
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    shifted_back = ''.join(chr((ord(char) - shift) % 256) for char in decoded_bytes.decode('utf-8'))
    return shifted_back

# -----------------------------
# 3. CLI Logic
# -----------------------------
def main():
    print("=== Encoder-Decoder ===")
    mode = input("Enter 'e' to encode or 'd' to decode: ").strip().lower()

    if mode == 'e':
        text = input("Enter text to encode: ")
        shift = int(input("Enter shift value (default is 3): ") or 3)
        result = encode_text(text, shift)
        print("Encoded text:", result)

    elif mode == 'd':
        encoded_text = input("Enter text to decode: ")
        shift = int(input("Enter shift value used during encoding: ") or 3)
        result = decode_text(encoded_text, shift)
        print("Decoded text:", result)

    else:
        print("Invalid option. Use 'e' or 'd'.")

# -----------------------------
# 4. Script Entry Point
# -----------------------------
if __name__ == "__main__":
    main()
