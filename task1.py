import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

t = np.linspace(0, 1, 500, endpoint=False)
square_signal = signal.square(2 * np.pi * 5 * t)

plt.plot(t, square_signal)
plt.title('Прямоугольный сигнал')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()
