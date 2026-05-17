def ajustar_temperatura_debye(file_path):
    import numpy as np
    from scipy.optimize import curve_fit
    from scipy.integrate import quad
    import matplotlib.pyplot as plt
    # Función de capacidad calorífica de Debye
    def debye_heat_capacity(T, theta_D):
        N = 1  # Normalizado para simplificar
        k_B = 1.38e-23  # Constante de Boltzmann
        integral, _ = quad(lambda x: (x**4 * np.exp(x)) / ((np.exp(x) - 1)**2), 0, theta_D / T)
        return 9 * N * k_B * (T / theta_D)**3 * integral

    # Leer los datos desde un archivo
    def read_data(file_path):
        T_data=[]
        C_data=[]
        with open(file_path,"r") as algo:
            for i in algo:
                i.strip().split()
                T_data.append(float(i[0]))
                C_data.append(float(i[1]))
        return T_data, C_data

    # Leer datos
    T_data, C_data = read_data(file_path)

    # Ajuste de la curva
    params, _ = curve_fit(debye_heat_capacity, T_data, C_data, p0=[300])  # p0 es una estimación inicial de theta_D

    # Parámetro ajustado
    theta_D_ajustado = params[0]
    print(f'Temperatura de Debye ajustada: {theta_D_ajustado:.2f} K')

    # Gráfico de resultados
    T_fit = np.linspace(min(T_data), max(T_data), 100)
    C_fit = debye_heat_capacity(T_fit, theta_D_ajustado)

    plt.plot(T_data, C_data, 'o', label='Datos experimentales')
    plt.plot(T_fit, C_fit, '-', label=f'Ajuste de Debye (Theta_D = {theta_D_ajustado:.2f} K)')
    plt.xlabel('Temperatura (K)')
    plt.ylabel('Capacidad Calorífica (J/K)')
    plt.legend()
    plt.show()

# Ejemplo de llamada a la función
print(ajustar_temperatura_debye('cvrrr.txt'))