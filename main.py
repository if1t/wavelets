import os
from data_loader import load_pulse_data, preprocess_signal
from wavelet_analyzer import calculate_wavelet_transform, calculate_wavelet_spectrum, get_wavelet_scales
from visualization import save_wavelet_spectrum

def main(data_dir, output_dir, wavelet_names):
    """
    Основная функция для обработки данных и построения вейвлет-спектров.

    Args:
        data_dir (str): Путь к каталогу с данными.
        output_dir (str): Путь к каталогу для сохранения результатов.
        wavelet_names (list): Список названий вейвлетов для анализа.
    """
    pulse_data = load_pulse_data(data_dir)
    if not pulse_data:
         print("Нет данных для обработки. Завершение.")
         return

    for wavelet_name in wavelet_names:
        wavelet_output_dir = os.path.join(output_dir, wavelet_name)
        os.makedirs(wavelet_output_dir, exist_ok=True)

        for filename, (signal, gender) in pulse_data.items():
             processed_signal = preprocess_signal(signal)
             coeffs = calculate_wavelet_transform(processed_signal, wavelet_name)
             spectrum = calculate_wavelet_spectrum(coeffs)
             scales = get_wavelet_scales(processed_signal, wavelet_name)
             save_wavelet_spectrum(spectrum, scales, filename, wavelet_name, wavelet_output_dir, gender)


if __name__ == '__main__':
    data_directory = 'data'  # Путь к сигналам
    output_directory = 'output'  # Каталог для сохранения результатов
    wavelets_to_use = ['db4', 'sym5', 'coif1']  # Вейвлеты

    main(data_directory, output_directory, wavelets_to_use)
