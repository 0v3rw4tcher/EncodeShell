import base64, binascii
last_encoded = ""
last_encoded_text = ""
last_decoded = ""
while (1):
    try:
        Input_ = str(input("""|_
  |_. """))
        Input = Input_.split(" ")
        if (Input[0].lower() == "hex"):
            Hex = binascii.hexlify(Input_[4:].encode())
            last_encoded = Hex
            last_encoded_text = Input_[5:]
            print(Hex.decode())
        elif (Input[0].lower() == "b64e"):
            b64 = base64.b64encode(Input_[5:].encode())
            last_encoded = b64
            last_encoded_text = Input_[5:]
            print(b64.decode())
        elif (Input[0].lower() == "b32e"):
            b32 = base64.b32encode(Input_[5:].encode())
            last_encoded = b32
            last_encoded_text = Input_[5:]
            print(b32.decode())
        elif (Input[0].lower() == "b16e"):
            b16 = base64.b16encode(Input_[5:].encode())
            last_encoded = b16
            last_encoded_text = Input_[5:]
            print(b16.decode())
        elif (Input[0].lower() == "b85e"):
            b85 = base64.b85encode(Input_[5:].encode())
            last_encoded = b85
            last_encoded_text = Input_[5:]
            print(b85.decode())
        elif (Input[0].lower() == "b64d"):
            b64 = base64.b64decode(Input_[5:].encode())
            last_decoded = b64
            print(b64.decode())
        elif (Input[0].lower() == "b32d"):
            b32 = base64.b32decode(Input_[5:].encode())
            last_decoded = b32
            print(b32.decode())
        elif (Input[0].lower() == "b16d"):
            b16 = base64.b16decode(Input_[5:].encode())
            last_decoded = b16
            print(b16.decode())
        elif (Input[0].lower() == "b85d"):
            b85 = base64.b85decode(Input_[5:].encode())
            last_decoded = b85
            print(b85.decode())
        elif (Input[0].lower() == "hexd"):
            Hex = binascii.unhexlify(Input_[5:])
            last_decoded = Hex
            print(Hex.decode())
        elif (Input[0].lower() == "lastenc"):
            if (Input[1].lower() == "hex"):
                Hex = binascii.hexlify(last_encoded)
                last_encoded = Hex
                last_encoded_text = last_encoded.decode()
                print(Hex.decode())
            elif (Input[1].lower() == "b64e"):
                b64 = base64.b64encode(last_encoded)
                last_encoded = b64
                last_encoded_text = last_encoded.decode()
                print(b64.decode())
            elif (Input[1].lower() == "b32e"):
                b32 = base64.b32encode(last_encoded)
                last_encoded = b32
                last_encoded_text = last_encoded.decode()
                print(b32.decode())
            elif (Input[1].lower() == "b16e"):
                b16 = base64.b16encode(last_encoded)
                last_encoded = b16
                last_encoded_text = last_encoded.decode()
                print(b16.decode())
            elif (Input[1].lower() == "b85e"):
                b85 = base64.b85encode(last_encoded)
                last_encoded = b85
                last_encoded_text = last_encoded.decode()
                print(b85.decode())
        elif (Input[0].lower() == "lastenctext"):
            if (Input[1].lower() == "hex"):
                Hex = binascii.hexlify(last_encoded_text.encode())
                last_encoded = Hex
                last_encoded_text = last_encoded_text
                print(Hex.decode())
            elif (Input[1].lower() == "b64e"):
                b64 = base64.b64encode(last_encoded_text.encode())
                last_encoded = b64
                last_encoded_text = last_encoded_text
                print(b64.decode())
            elif (Input[1].lower() == "b32e"):
                b32 = base64.b32encode(last_encoded_text.encode())
                last_encoded = b32
                last_encoded_text = last_encoded_text
                print(b32.decode())
            elif (Input[1].lower() == "b16e"):
                b16 = base64.b16encode(last_encoded_text.encode())
                last_encoded = b16
                last_encoded_text = last_encoded_text
                print(b16.decode())
            elif (Input[1].lower() == "b85e"):
                b85 = base64.b85encode(last_encoded_text.encode())
                last_encoded = b85
                last_encoded_text = last_encoded_text
                print(b85.decode())
        elif (Input[0] == "stat"):
            print(
f"""
Status :
\tLast encoded text : {last_encoded_text}
\tLast encode : {last_encoded.decode()}
"""
        )
        elif (Input[0] == "help"):
            print(
"""
Commands :
\tEncode :
\t\tBase :
\t\t\tb16e : Base16 encode
\t\t\tb32e : Base32 encode
\t\t\tb85e : Base85 encode
\t\t\tb64e : Base64 encode
\t\tHexa :
\t\t\thex : Text to hexadecimal
\tDecode :
\t\tBase :
\t\t\tb16d : Base16 decode
\t\t\tb32d : Base32 decode
\t\t\tb85d : Base85 decode
\t\t\tb64d : Base64 decode
\t\tHexa :
\t\t\thexd : Hexadecimal to text
\tOthers :
\t\tstat : Get status of the script
\t\texit : Exit (Or just ALT+F4 or CTR+C)
\t\thelp : Help and show command list
"""
        )
        elif (Input[0] == "exit"):
            exit()
    except Exception as e:
        print("We have some issues with your command, see 'help' : ", e)