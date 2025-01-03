import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def chaos_game(iterations):
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    point = np.random.rand(2)
    points = [point]
    
    for _ in range(iterations):
        random_vertex = vertices[np.random.randint(0, len(vertices))]
        
        point = (point + random_vertex) / 2
        points.append(point)
    
    return np.array(points)

def start_simulation():
    try:
        iterations = int(iteration_entry.get())
        if iterations <= 0:
            raise ValueError("Jumlah iterasi harus lebih besar dari 0.")
    except ValueError as e:
        messagebox.showerror("Error", f"Input tidak valid: {e}")
        return
    points = chaos_game(iterations)

    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], s=0.1, c='blue', alpha=0.6)
    plt.title(f"Chaos Game: {iterations} Iterations")
    plt.axis("equal")
    plt.show()

root = tk.Tk()
root.title("Chaos Game Simulation")
ttk.Label(root, text="Chaos Game Simulation", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text="Masukkan jumlah iterasi:").grid(row=1, column=0, pady=5, padx=5)
iteration_entry = ttk.Entry(root)
iteration_entry.grid(row=1, column=1, pady=5, padx=5)
start_button = ttk.Button(root, text="Mulai Simulasi", command=start_simulation)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
