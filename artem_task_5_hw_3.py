text = input("Введите текст: ")
text = text.lower()
for x, y in ("черт", "####"), ('ЧЕРТ', "####"):
    text = text.replace(x, y)
print(text)

