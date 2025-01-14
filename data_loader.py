import numpy as np
import os
import struct

def load_pulse_data(data_dir, sample_rate=100):
    """
    Загружает пульсовые сигналы из двоичных файлов.

    Args:
        data_dir (str): Путь к каталогу с данными.
        sample_rate (int): Частота дискретизации сигнала.

    Returns:
        dict: Словарь, где ключи - имена файлов, значения - кортежи (сигнал, пол).
    """
    pulse_data = {}
    for filename in os.listdir(data_dir):
        try:
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'rb') as file:
                raw_data = file.read()
            # Распаковка двухбайтовых данных
            signal = np.array(struct.unpack('<' + 'h' * (len(raw_data) // 2), raw_data), dtype=np.float64)
            # todo Вычисление пола
            gender = 'male'
            pulse_data[filename] = (signal, gender)
        except Exception as e:
            print(f"Ошибка при загрузке файла {filename}: {e}")
    return pulse_data

def preprocess_signal(signal):
    """
    Предварительная обработка сигнала (центрирование).

    Args:
        signal (np.array): Исходный сигнал.

    Returns:
        np.array: Обработанный сигнал.
    """
    return signal - np.mean(signal)
