import re
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Expresiones regulares para IPv4 e IPv6
regex_ipv4 = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
regex_ipv6 = r"^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$"

def validar_ip():
    ip = entrada_ip.get()
    if re.match(regex_ipv4, ip):
        messagebox.showinfo("Validación", f"La dirección {ip} es una IPv4 válida ✅")
    elif re.match(regex_ipv6, ip):
        messagebox.showinfo("Validación", f"La dirección {ip} es una IPv6 válida ✅")
    else:
        messagebox.showerror("Validación", f"La dirección {ip} NO es válida ❌")

def construir_afn_ipv4():
    G = nx.MultiDiGraph()
    estados = ["q0", "d1", "p1", "d2", "p2", "d3", "p3", "d4", "qf"]
    
    transiciones = [
        ("q0", "d1", "0-255"), ("d1", "p1", "."),
        ("p1", "d2", "0-255"), ("d2", "p2", "."),
        ("p2", "d3", "0-255"), ("d3", "p3", "."),
        ("p3", "d4", "0-255"), ("d4", "qf", "Fin")
    ]
    
    for estado in estados:
        G.add_node(estado)
    for origen, destino, etiqueta in transiciones:
        G.add_edge(origen, destino, label=etiqueta)

    return G

def construir_afn_ipv6():
    G = nx.MultiDiGraph()
    estados = ["q0", "h1", "dp1", "h2", "dp2", "h3", "dp3", "h4", "dp4", "h5", "dp5", "h6", "dp6", "h7", "dp7", "h8", "qf"]
    
    transiciones = [
        ("q0", "h1", "0000-FFFF"), ("h1", "dp1", ":"),
        ("dp1", "h2", "0000-FFFF"), ("h2", "dp2", ":"),
        ("dp2", "h3", "0000-FFFF"), ("h3", "dp3", ":"),
        ("dp3", "h4", "0000-FFFF"), ("h4", "dp4", ":"),
        ("dp4", "h5", "0000-FFFF"), ("h5", "dp5", ":"),
        ("dp5", "h6", "0000-FFFF"), ("h6", "dp6", ":"),
        ("dp6", "h7", "0000-FFFF"), ("h7", "dp7", ":"),
        ("dp7", "h8", "0000-FFFF"), ("h8", "qf", "Fin")
    ]
    
    for estado in estados:
        G.add_node(estado)
    for origen, destino, etiqueta in transiciones:
        G.add_edge(origen, destino, label=etiqueta)

    return G

def dibujar_afn(tipo):
    G = construir_afn_ipv4() if tipo == "IPv4" else construir_afn_ipv6()
    
    pos = nx.spring_layout(G)
    etiquetas = nx.get_edge_attributes(G, 'label')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    plt.title(f"Autómata Finito No Determinista para {tipo}")
    plt.show()

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Validador de Direcciones IP y AFN")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Ingrese una dirección IP:")
etiqueta.pack(pady=5)

entrada_ip = tk.Entry(ventana, width=30)
entrada_ip.pack(pady=5)

boton_validar = tk.Button(ventana, text="Validar IP", command=validar_ip)
boton_validar.pack(pady=5)

boton_ipv4 = tk.Button(ventana, text="Mostrar AFN IPv4", command=lambda: dibujar_afn("IPv4"))
boton_ipv4.pack(pady=5)

boton_ipv6 = tk.Button(ventana, text="Mostrar AFN IPv6", command=lambda: dibujar_afn("IPv6"))
boton_ipv6.pack(pady=5)

ventana.mainloop()
