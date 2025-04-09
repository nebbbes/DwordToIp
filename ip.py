def dword_to_ip(dword):
    # Конвертируем отрицательные DWORD в беззнаковые
    if dword < 0:
        dword += 2**32
    # Разбиваем на 4 октета
    octets = [
        (dword >> 24) & 0xFF,
        (dword >> 16) & 0xFF,
        (dword >> 8) & 0xFF,
        dword & 0xFF
    ]
    return ".".join(map(str, octets))

def main():
    try:
        # Чтение DWORD из файла
        with open('dword.txt', 'r') as f:
            dwords = [line.strip() for line in f.readlines() if line.strip()]
        
        # Обработка и конвертация
        ips = []
        for dword_str in dwords:
            try:
                dword = int(dword_str)
                ip = dword_to_ip(dword)
                ips.append(ip)
                print(f"DWORD: {dword_str} -> IP: {ip}")  # Вывод в PowerShell
            except ValueError:
                print(f"Ошибка: '{dword_str}' не является числом")
        
        # Запись IP в файл
        with open('ip.txt', 'w') as f:
            for ip in ips:
                f.write(f"{ip}\n")
        
        print("\nРезультат сохранён в ip.txt")
    
    except FileNotFoundError:
        print("Ошибка: файл dword.txt не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()