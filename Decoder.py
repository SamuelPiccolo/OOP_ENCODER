import sys
import base64

def decode_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    decoded_data = base64.b64decode(data)

    with open(output_file, "wb") as f:
        f.write(decoded_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decode.py input_file output_file")
        sys.exit(1)

    decode_file(sys.argv[1], sys.argv[2])
    print("File decoded successfully")