import console_gfx

def to_hex_string(data):
    hex_string = ""
    hex_dict = {
        0: "0", 1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6", 7: "7",
        8: "8", 9: "9", 10: "a", 11: "b",
        12: "c", 13: "d", 14: "e", 15: "f"}
    for num in data:
        current = hex_dict[num]
        hex_string += current
    return hex_string

def count_runs(flat_data):
    current_strip = 1
    runs = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            current_strip += 1
            if current_strip > 15:
                runs += 1
                current_strip = 1
        elif flat_data[i] != flat_data[i - 1]:
            current_strip = 1
            runs += 1
    return runs

def encode_rle(flat_data):
    encoded = []
    count = 1
    current = flat_data[0]
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            count += 1
            if count > 15:
                encoded.append(count - 1)
                encoded.append(current)
                count = 1
        if flat_data[i] != flat_data[i - 1]:
            encoded.append(count)
            encoded.append(current)
            current = flat_data[i]
            count = 1
    encoded.append(count)
    encoded.append(current)
    return encoded

def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data) - 1, 2):
        length += rle_data[i]
    return length

def decode_rle(flat_data):
    decoded = []
    for i in range(0, len(flat_data) - 1, 2):
        count = flat_data[i]
        value = flat_data[i + 1]
        for i in range (count):
            decoded.append(value)
    return decoded

def string_to_data(data_string):
    data = []
    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11,
        'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for i in data_string:
        data.append(hex_dict[i])
    return data

def to_rle_string(rle_data):
    hex = '0123456789abcdef'
    final = ''
    for i in range (0, len(rle_data), 2):
        final = final + str(rle_data[i])
        final = final + hex[rle_data[i + 1]] + ":"
    final = final[:-1]
    return final


def string_to_rle(rle_string):
    string = rle_string.split(":")
    final = []

    for i in string:
        length = int(i[:-1])
        value = int(i[-1],16)

        final.append(length)
        final.append(value)

    return final

def main():
    def menu():
        print()
        print("RLE Menu")
        print("-" * 8)
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")

        file_data = []
        rle_string = ""
        hex_string_rle = ""
        hex_string_flat = ""

    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        menu()
        selection = int(input("Select a Menu Option: "))

        if selection == 0:
            break
        if selection == 1:
            file_name = input("Enter name of file to load: ")
            console_gfx.load_file(file_name)
            print()

        if selection == 2:
            file_data = console_gfx.test_image
            print("Test image data loaded.\n")

        if selection == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            decoded = decode_rle(rle_data)
            encoded = encode_rle(decoded)

        if selection == 4:
            hex_string = input("Enter the hex string holding RLE data: ")
            rle_data = string_to_data(hex_string)
            decoded = decode_rle(rle_data)
            encoded = encode_rle(decoded)
            print(f"Decoded RLE: {decode_rle(rle_data)}\n")
        if selection == 5:
            hex_string_flat = input("Enter the hex string holding flat data: ")
            flat_data = string_to_data(hex_string_flat)
        if selection == 6:
            print('Displaying image...')
            if file_data:
                console_gfx.display_image(file_data)
            else:
                print("No image data loaded.\n")
        if selection == 7:
            if decoded:
                print('RLE representation:', end = " ")
                print(to_rle_string(encoded))
            else:
                print("No image data loaded.\n")
        if selection == 8:
            if decoded:
                print('RLE hex values: ', end = " ")
                print(to_rle_string(encoded))
            else:
                print("No image data loaded.\n")
        if selection == 9:
            if decoded:
                print('Flat hex values: ', end = "")
                print(to_hex_string(decoded))
            else:
                print("No image data loaded.\n")

if __name__ == "__main__":
    main()
