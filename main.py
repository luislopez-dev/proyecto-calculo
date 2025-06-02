import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sympy as sp

plt.style.use('dark_background')

# Solicitar la función al usuario
def ingresar_funcion():
    while True:
        try:
            expr = input("Ingresa la función (en términos de 'x', ej. '2*x**3 - 6*x + 1'): ")
            x = sp.symbols('x')
            y = sp.sympify(expr)  # Convierte el string a expresión simbólica
            return y
        except:
            print("Error: Ingresa una función válida (usa 'x' como variable y operadores matemáticos estándar).")

# Solicitar los puntos a evaluar
def ingresar_puntos():
    while True:
        try:
            puntos_str = input("Ingresa los puntos x a evaluar (separados por comas, ej. '0, 1, 2'): ")
            puntos = [float(p.strip()) for p in puntos_str.split(',')]
            return puntos
        except:
            print("Error: Ingresa números válidos separados por comas.")

# Obtener datos del usuario
print("\n" + "="*50)
y = ingresar_funcion()
puntos = ingresar_puntos()
print("="*50 + "\n")

# Calcular la derivada
x_sym = sp.symbols('x')
y_prime = sp.diff(y, x_sym)

# Evaluar la función y su derivada en los puntos
results = []

for punto in puntos:
    
    y_val = y.subs(x_sym, punto)
    
    y_prime_val = y_prime.subs(x_sym, punto)

    comportamiento = "creciente" if y_prime_val > 0 else ("decreciente" if y_prime_val < 0 else "punto crítico")
    
    results.append((punto, y_val, y_prime_val, comportamiento))

# Crear datos para el gráfico
x_vals = np.linspace(min(puntos) - 1, max(puntos) + 1, 400)
y_vals = [y.subs(x_sym, val) for val in x_vals]

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, y_vals, label=f'$y = {sp.latex(y)}$', color='cyan', linewidth=2)

# Marcar los puntos evaluados
colores = ['magenta', 'yellow', 'lime', 'red', 'orange']
for i, (punto, y_val, _, comp) in enumerate(results):
    color = colores[i % len(colores)]  # Ciclar colores si hay muchos puntos
    ax.scatter(punto, y_val, color=color, s=100, zorder=5, edgecolors='white')
    ax.text(punto, y_val + 0.3, f'({punto:.1f}, {y_val:.1f})\n{comp}', 
            fontsize=9, ha='center', color='white')

# Mostrar resultados en consola
print("\nRESULTADOS:")
for p, y_val, y_prime_val, comp in results:
    print(f"En x = {p:.2f}: y = {y_val:.2f}, y' = {y_prime_val:.2f} → {comp}")


# Añadir detalles
ax.axhline(0, color='white', linewidth=0.5, linestyle='--')
ax.axvline(0, color='white', linewidth=0.5, linestyle='--')
ax.set_title(f"Gráfico de $y = {sp.latex(y)}$", fontsize=14, color='white')
ax.set_xlabel("x", fontsize=12, color='white')
ax.set_ylabel("y", fontsize=12, color='white')
ax.grid(True, linestyle='--', alpha=0.4, color='gray')
ax.legend(fontsize=12, facecolor='#333333')

plt.show(block=True)
input("Presione Enter para cerrar la gráfica...")
plt.close()