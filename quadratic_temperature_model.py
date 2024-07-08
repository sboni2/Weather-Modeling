import matplotlib.pyplot as plt
import numpy as np


def quadratic_temperature_model(time, a, b, c):
  temperature = (a * (time**2) + b * time + c)
  return temperature


a = float(input("Enter the coeefecient for the quadratic term a: "))
b = float(input("Enter the coeefecient for the linear term b: "))
c = float(input("Enter the constant term c: "))
time_values = np.linspace(0, 10, 50)
temperature_values = quadratic_temperature_model(time_values, a, b, c)
plt.plot(temperature_values,
         time_values,
         label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Quadratic Temperature Model')
plt.legend()
plt.grid(True)
plt.show()
