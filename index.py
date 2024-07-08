import matplotlib.pyplot as plt
import numpy as np

f = open("Weather.txt", "r")

def quadratic_model(f, time):
    a = float(f.readline())
    b = float(f.readline())
    c = float(f.readline())
    temperature = (a * time * time + b * time + c)
    return temperature


time_values = np.linspace(0, 10, 50)
temperature_hardcoded = quadratic_model(f, time_values)

plt.plot(temperature_hardcoded,
         time_values,
         label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(read from file)')
plt.show()
