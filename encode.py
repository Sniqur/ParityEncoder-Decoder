def encode_message(info_bits, text, input_file_path, encoded_file_path):
    """Кодує повідомлення, додаючи біти перевірки, і записує вхідне та кодоване повідомлення у файли."""
    # Записуємо вхідне текстове повідомлення у файл
    with open(input_file_path, "w") as input_file:
        input_file.write(text)

    # Перетворюємо текст у бітову послідовність
    bits = ''.join(format(ord(char), '08b') for char in text)

    # Ділимо на сегменти та додаємо біти парності
    segments = [bits[i:i + info_bits] for i in range(0, len(bits), info_bits)]
    encoded_segments = [segment + ('0' if segment.count('1') % 2 == 0 else '1') for segment in segments]

    # Записуємо кодоване повідомлення у інший файл

    with open(encoded_file_path, "w") as encoded_file:
        encoded_file.write(''.join(encoded_segments))


info_bits = int(input("Введіть інформаційну кількість бітів: "))
text = input("Введіть текстове повідомлення: ")

input_file_path = "input_message.txt"
encoded_file_path = "encoded_message.txt"

encode_message(info_bits, text, input_file_path, encoded_file_path)

print(f"Вхідне повідомлення було збережено у файлі '{input_file_path}'.")
print(f"Закодоване повідомлення було збережено у файлі '{encoded_file_path}'.")
