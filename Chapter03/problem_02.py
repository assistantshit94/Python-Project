letter = '''Dear <|name|>,\nYou are selected!\nThanks and regards,\n<Date>'''
print(letter.replace("<|name|>", "Shital").replace("<Date>", "2023-10-10"))

name = "Shital is a good   girl"
print(name.find("good"))
print(name.replace("good", "bad"))

print(name.replace("  ", " "))