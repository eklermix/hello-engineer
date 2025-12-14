a = int(input("Сколько байт? "))

kb = a / 1024
mb = kb / 1024

print("Результаты для ", a, " байт:")
print("КБ: ", kb)
print("МБ: ", mb)
print("DEC: ", a)
print("BIN: ", bin(a)[2:])
print("HEX: ", hex(a)[2:].upper())