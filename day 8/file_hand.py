# f = open("hello.txt", "a")
# a = input("Enter the data: ")

# f.write(f'\n {a}')

# f.close()

# """f = open("index.html", "r")
# data = f.readlines(15)
# print(data)
# f.close()"""

# with open("index.html", 'r') as html_file:
#     lines = html_file.readlines()

# with open("index.html", 'w') as html_file:
#     for line in lines:
#         html_file.write(line)
#         if '<h2></h2>' in line:
#             html_file.write("    <h3>Hello H3</h3>\n")

# with open("index.html",'r') as html_file:
#     for line in html_file:
#         print(line.strip())

# import os
# check = os.path.exists("index.html")
# print(check)

def detect_file_type(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)   # read first 8 bytes

    # Known magic numbers
    if header.startswith(b"%PDF"):
        return "PDF file"
    elif header.startswith(b"\x89PNG"):
        return "PNG image"
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "JPEG image"
    elif header.startswith(b"PK\x03\x04"):
        return "ZIP archive"
    elif header.startswith(b"MZ"):
        return "Windows EXE file"
    else:
        return "Unknown file type"


file_path = input("Enter file path: ")
result = detect_file_type(file_path)
print("Detected:", result)