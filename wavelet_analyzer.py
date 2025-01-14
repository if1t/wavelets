import pywt
import numpy as np

def calculate_wavelet_transform(signal, wavelet_name, level=None):
    """
    Выполняет дискретное вейвлет-преобразование.

    Args:
        signal (np.array): Входной сигнал.
        wavelet_name (str): Название вейвлета (например, 'db4', 'sym5', 'coif1').
        level (int, optional): Уровень разложения. Если None - вычисляется максимальный возможный.

    Returns:
        list: Список вейвлет-коэффициентов на каждом уровне разложения.
    """
    try:
        wavelet = pywt.Wavelet(wavelet_name)
        if level is None:
            level = pywt.dwt_max_level(len(signal), wavelet.dec_len)
        coeffs = pywt.wavedec(signal, wavelet, level=level)
        return coeffs
    except Exception as e:
        print(f"Ошибка при расчете ДВП для вейвлета {wavelet_name}: {e}")
        return None


def calculate_wavelet_spectrum(coeffs):
    """
    Вычисляет вейвлет-спектр на основе коэффициентов ДВП.

    Args:
        coeffs (list): Список вейвлет-коэффициентов.

    Returns:
        np.array: Вейвлет-спектр (амплитуды коэффициентов на каждом уровне).
    """
    if coeffs is None:
        return None
    spectrum = np.array([np.mean(np.abs(c)) for c in coeffs])
    return spectrum[1:] # обрезаем первый элемент (для вывода на график)


def get_wavelet_scales(signal, wavelet_name, level=None):
    """
    Определяет шкалы (частоты) для вейвлет-спектра.

    Args:
        signal (np.array): Исходный сигнал
        wavelet_name (str): Название вейвлета
        level (int, optional): Уровень разложения

    Returns:
         list: Список шкал для каждого уровня
    """
    wavelet = pywt.Wavelet(wavelet_name)
    if level is None:
            level = pywt.dwt_max_level(len(signal), wavelet.dec_len)
    scales = []
    for i in range(1, level + 1):
        scales.append(2 ** i)

    return [1 / scale for scale in scales]
