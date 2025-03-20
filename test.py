with open("data.txt",mode="w+") as file:
    content = file.read()
    print(content)
    file.write('3')