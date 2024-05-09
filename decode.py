def decode_segment_with_parity(segment):
    ones_count = segment.count('1')
    # Якщо кількість одиниць парна - добре, непарна - помилка
    error = ones_count % 2 != 0
    # Видалення біта парності
    data = segment[:-1]
    return data, error

def decode_message_with_parity(encoded_message, info_bits):
    decoded_bits = ""
    error_segments = []
    segments = [encoded_message[i:i + info_bits + 1] for i in range(0, len(encoded_message), info_bits + 1)]

    for i, segment in enumerate(segments):
        data, error = decode_segment_with_parity(segment)
        decoded_bits += data
        if error:
            # Запам'ятовуємо номер сегмента, де виявлено помилку
            error_segments.append(i + 1)

    return decoded_bits, error_segments

def bits_to_text(bits):
    # Перевірка, чи кількість бітів ділиться на 8
    if len(bits) % 8 != 0:
        raise ValueError("Неправильна кількість бітів")

    # Розділення бітів на групи по 8
    bytes_arr = [bits[i:i+8] for i in range(0, len(bits), 8)]

    # Перетворення кожної групи бітів в ціле число
    byte_values = [int(byte, 2) for byte in bytes_arr]

    # Перетворення цілих чисел у символи
    text = ''.join(chr(byte) for byte in byte_values)

    return text

def main():
    info_bits = int(input("Введіть інформаційну кількість бітів: "))
    encoded_file_path = input("Введіть шлях до файлу з закодованим повідомленням: ")
    output_file_path = "result.txt"
    # Читання закодованого повідомлення з файлу
    with open(encoded_file_path, 'r') as file:
        encoded_message = file.read()

    decoded_bits, error_segments = decode_message_with_parity(encoded_message, info_bits)
    decoded_message = bits_to_text(decoded_bits)

    # Вивід інформації про помилки
    if error_segments:
        print(f"Помилки виявлені у сегментах: {', '.join(map(str, error_segments))}.")
    else:
        print("Помилок у повідомленні не виявлено.")

     # Запис декодованого повідомлення у файл
    with open(output_file_path, 'w') as file:
        file.write(decoded_message)

    print(f"Декодоване повідомлення збережено у файлі {output_file_path}.")


if __name__ == "__main__":
    main()
