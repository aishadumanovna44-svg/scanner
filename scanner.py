import subprocess
import json
import platform

print("--- ЗАПУСК СИСТЕМНОГО СКАНЕРА (БЕЗ БИБЛИОТЕК) ---")

def get_sys_info(command):
    try:
        return subprocess.check_output(command, shell=True).decode('cp866').strip().split('\n')[1].strip()
    except:
        return "Не определено"

# 1. Получаем реальное имя процессора
cpu = get_sys_info("wmic cpu get name")

# 2. Получаем объем ОЗУ (в байтах -> в ГБ)
ram_raw = get_sys_info("wmic computersystem get totalphysicalmemory")
try:
    ram = round(int(ram_raw) / (1024**3), 2)
except:
    ram = "Ошибка ОЗУ"

# 3. Получаем название видеокарты
gpu = get_sys_info("wmic path win32_VideoController get name")

data = {
    "cpu": cpu,
    "ram_total": ram,
    "gpu": [{"name": gpu, "temp": 0}]
}

# Записываем в файл
with open('specs.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f">>> УСПЕХ! Процессор: {cpu}")
print(f">>> Память: {ram} GB")
print(f">>> Видеокарта: {gpu}")