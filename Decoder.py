###This project uses cryptography which is a substitution using a cipher
###which has been made into a class with the use of a password
###which determines the use of the correct shift if correct
###within the ascii lanmark images and outputs a decrypted
###file drom the inherited classes
import sys###module imports
import os###checks the file if it exists

class Decoder:###matches the emcoders characters while matching the images to convert acsi
    Character=[
        "a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"]

    ###it matches the encoder image/ascii
    images = None###placeholder needed before decoding
    PASSWORD="cesar"###password to use the right shift cycle , it will run with wrong password but decode wrong

    def __init__(self, right_password):
        if Decoder.images is None:
            raise RuntimeError("the ecoder imgaes_tmp wasnt initialised ")

        ###builds a reverse lookup ascii image to character
        self.image_to_character= {}
        if right_password:
            for character, image in zip(Decoder.Character, Decoder.images):
                key = image.strip()   
                self.image_to_character[key] = character
        else:
            shifted= Decoder.Character[3:] +Decoder.Character[:3]
            for character, image in zip(shifted, Decoder.images):
                key=image.strip()
                self.image_to_character[key]=character
    def reverse_shuffle(self, blocks):
        k =(len(blocks) -1)%5
        n =len(blocks)
        for j in range(n - 1, -1, -1):
            if k ==0:
                if j +3<n:
                    blocks[j],blocks[j+3]=blocks[j+3],blocks[j]
            elif k== 1:
                if j+1<n:
                    blocks[j],blocks[j+1]= blocks[j+1],blocks[j]
            elif k== 4:
                if j-3>=0:
                    blocks[j], blocks[j-3]= blocks[j-3],blocks[j]
            k=(k-1)%5
        return blocks 

    def decode(self, encoded_text):
        decoded_characters = []
        ###it splits the ecoded file into blocks
        blocks = encoded_text.split("-" * 100)
        blocks = [b.strip() for b in blocks if b.strip()]###removes blocks 
        blocks = self.reverse_shuffle(blocks)###reverses the shuffle used by the encoder
        for block in blocks:
            block = block.strip()
            ###skips blocks that hold no value
            if not block or block.startswith("Total encoded characters"):
                continue

            ascii_art=block.strip()  

            if ascii_art in self.image_to_character:
                decoded_characters.append(self.image_to_character[ascii_art])
            else:###in case it doesnt recognise the character in the block
                found=False
                for c in ascii_art:
                    if c not in "A\n":
                        decoded_characters.append(c)
                        found=True
                        break
                if not found:
                    decoded_characters.append("?")

        return "".join(decoded_characters)


if __name__ =="__main__":
    if len(sys.argv) != 3:
        print("Usage: python decoder.py <encoded_file> <password>")
        sys.exit(1)

    encoded_file = sys.argv[1]####checks the encoded files existance
    password=sys.argv[2]

    if not os.path.exists(encoded_file):
        print(f"Error:The file '{encoded_file}'was not found.")
        sys.exit(1)###reads encoced file only

    with open(encoded_file, "r", encoding="utf-8") as f:
        encoded_data = f.read()###imports encoder nd reads it
    
    ###copies encoder.imgaes_tmp to decoder.imgaes_tmp and makes sure they are equal
    from encoder import Encoder
    Decoder.images = Encoder.images
    ###decodes the contents of the encoded file
    right_password=(password == Decoder.PASSWORD)
    decoder = Decoder(right_password)
    message = decoder.decode(encoded_data)

    print("Decoded Message:")
    print(message)
    decoded_file="decoded.txt"
    with open(decoded_file, "w",encoding="utf-8") as f:
        f.write(message)
    print(f"decoded output is in {decoded_file}")
    
