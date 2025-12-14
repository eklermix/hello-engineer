# Файл converter.py
# Автор: Хабаров Михаил Максимович
# Этот файл является частью проекта 'hello-engineer'

def run_converter():
    print("\n - Инженерный калькулятор систем счисления -")
    mode = input("Выберите исходную систему (dec, bin, hex): ").lower()
    number_str = input("Введите число для конвертации: ")
    
    if mode == 'dec':
        try:
            dec_number = int(number_str)
            print(f"Двоичное: {bin(dec_number)[2:]}")
            print(f"Шестнадцатеричное: {hex(dec_number)[2:]}")
        except ValueError:
            print("Ошибка: введено неверное десятичное число.")
    elif mode == 'bin':
        try:
            dec_number = int(number_str, 2)
            print(f"Десятичное: {dec_number}")
            print(f"Шестнадцатеричное: {hex(dec_number)[2:]}")
        except ValueError:
            print("Ошибка: введено неверное двоичное число.")
    elif mode == 'hex':
        try:
            dec_number = int(number_str, 16)
            print(f"Десятичное: {dec_number}")
            print(f"Двоичное: {bin(dec_number)[2:]}")
        except ValueError:
            print("Ошибка: введено неверное шестнадцатеричное число.")
    else:
        print("Ошибка: выбран неверный режим. Доступные режимы: dec, bin, hex.")

# Эта конструкция позволяет запускать код только тогда, когда файл исполняется напрямую
if __name__ == "__main__":
    run_converter()