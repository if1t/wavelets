import matplotlib.pyplot as plt
import os
import numpy as np

def save_wavelet_spectrum(spectrum, scales, filename, wavelet_name, output_dir, gender):
    """
    Сохраняет вейвлет-спектр в виде графика.

    Args:
        spectrum (np.array): Вейвлет-спектр.
        scales (list): Шкалы для вейвлет-спектра
        filename (str): Имя файла сигнала (для имени графика).
        wavelet_name (str): Название вейвлета (для имени графика).
        output_dir (str): Каталог для сохранения графика.
        gender (str): Пол носителя сигнала
    """
    if spectrum is None:
        return
    try:
        gender_dir = os.path.join(output_dir, gender)
        os.makedirs(gender_dir, exist_ok=True)
        output_path = os.path.join(gender_dir, f"{os.path.splitext(filename)[0]}_{wavelet_name}.png")

        plt.figure(figsize=(10, 6))
        plt.plot(scales, spectrum)
        plt.title(f'Вейвлет-спектр ({wavelet_name}) для {filename}')
        plt.xlabel("Шкала (частота)")
        plt.ylabel("Амплитуда коэффициентов")
        plt.grid(True)
        plt.savefig(output_path)
        plt.close()
        print(f"Спектр для {filename} сохранен в {output_path}")

    except Exception as e:
        print(f"Ошибка при сохранении спектра для {filename}: {e}")
