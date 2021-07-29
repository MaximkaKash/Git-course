my_text = []
file_obj = open("Text.txt", "r")
# for line in file_obj:
#     print(line)
#     print("///")
file_obj.seek(0)
file_contents = file_obj.read()
print(file_contents)
file_obj.close()

