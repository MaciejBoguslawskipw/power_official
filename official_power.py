import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Stała wartość indukcji magnetycznej (przykładowo 1 Tesla)
B = 1  # Tesla

# Funkcje do obliczeń napięć
def oblicz_napiecie():
    try:
        # Pobranie danych od użytkownika
        N = int(entry_num_turns.get())  # Liczba zwojów
        A = float(entry_area.get())  # Pole powierzchni ramki w metrach kwadratowych
        f = float(entry_frequency.get())  # Częstotliwość obrotu w Hz

        # Sprawdzanie, czy dane mają sens (wartości muszą być większe od zera)
        if N <= 0 or A <= 0 or f <= 0:
            raise ValueError("Wszystkie wartości muszą być większe od zera.")

        # Obliczanie napięcia na podstawie wzoru Faradaya
        omega = 2 * np.pi * f  # Prędkość kątowa
        theta = 0  # Zakładamy, że kąt wynosi 0 dla maksymalnego napięcia
        max_voltage = N * A * B * omega * np.cos(theta)
        rms_voltage = max_voltage / np.sqrt(2)

        # Wyświetlenie wyników w etykiecie
        label_result.config(text=f'Napięcie maksymalne: {max_voltage:.2f} V\nNapięcie skuteczne: {rms_voltage:.2f} V')

        # Rysowanie wykresu w osobnym oknie
        rysuj_wykres(max_voltage, f)

    except ValueError as e:
        messagebox.showerror("Błąd", f"Proszę podać poprawne wartości.\n{str(e)}")

# Funkcja do rysowania wykresu funkcji sinusoidalnej w osobnym oknie
def rysuj_wykres(amplitude, frequency):
    try:
        # Wyznaczenie stałej czasowej tau na podstawie częstotliwości
        tau = 1 / frequency  # Stała czasowa w sekundach

        # Generowanie czasu w sekundach (np. dla 2 okresów sygnału)
        t = np.linspace(0, 2 * tau, 1000)  # Zakres czasu w sekundach
        y = amplitude * np.sin(2 * np.pi * frequency * t)  # Napięcie sinusoidalne w czasie

        # Tworzenie nowego okna dla wykresu
        wykres_window = tk.Toplevel(window)
        wykres_window.title("Wykres funkcji sinusoidalnej z czasem")
        wykres_window.geometry("600x600")

        # Tworzenie wykresu
        fig, ax = plt.subplots()
        ax.plot(t, y, label='Funkcja sinusoidalna', color='b')
        ax.set_title('Wykres funkcji sinusoidalnej (czas)')
        ax.set_xlabel('Czas [s]')
        ax.set_ylabel('Amplituda [V]')
        ax.legend()

        # Wstawianie wykresu do okna Tkinter
        canvas = FigureCanvasTkAgg(fig, master=wykres_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Dodanie funkcji zmiany rozmiaru wykresu
        def on_resize(event):
            canvas.get_tk_widget().config(width=event.width, height=event.height)
            fig.set_size_inches(event.width / 100, event.height / 100)
            canvas.draw()

        wykres_window.bind("<Configure>", on_resize)
    except Exception as e:
        messagebox.showerror("Błąd", f"Problem podczas rysowania wykresu: {str(e)}")

# Inicjalizacja okna głównego
window = tk.Tk()
window.title("Obliczanie napięcia indukowanego")
window.geometry("600x600")

# Interfejs użytkownika
label_instruction = tk.Label(window, text="Podaj dane:")
label_instruction.pack(pady=10)

# Liczba zwojów
label_num_turns = tk.Label(window, text="Liczba zwojów:")
label_num_turns.pack()
entry_num_turns = tk.Entry(window)
entry_num_turns.pack(pady=5)

# Pole powierzchni ramki
label_area = tk.Label(window, text="Pole powierzchni ramki (m²):")
label_area.pack()
entry_area = tk.Entry(window)
entry_area.pack(pady=5)

# Częstotliwość obrotu
label_frequency = tk.Label(window, text="Częstotliwość obrotu (Hz):")
label_frequency.pack()
entry_frequency = tk.Entry(window)
entry_frequency.pack(pady=5)

# Przycisk obliczania
button_calculate = tk.Button(window, text="Oblicz napięcie", command=oblicz_napiecie)
button_calculate.pack(pady=20)

# Etykieta wyników
label_result = tk.Label(window, text="Wyniki:", font=("Helvetica", 12))
label_result.pack(pady=10)

# Uruchomienie aplikacji
window.mainloop()