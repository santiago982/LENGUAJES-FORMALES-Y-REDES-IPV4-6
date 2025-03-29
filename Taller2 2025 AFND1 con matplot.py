import re
import networkx as nx
import matplotlib.pyplot as plt

def es_ipv4(direccion):
    patron_ipv4 = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.'
                              r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.'
                              r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.'
                              r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return bool(patron_ipv4.match(direccion))

def es_ipv6(direccion):
    patron_ipv6 = re.compile(r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$')
    return bool(patron_ipv6.match(direccion))

def reconocer_direccion(direccion):
    if es_ipv4(direccion):
        return "La dirección es IPv4"
    elif es_ipv6(direccion):
        return "La dirección es IPv6"
    else:
        return "La dirección no es válida"

def dibujar_afn_ipv4():
    G = nx.DiGraph()
    estados = ["Inicio", "Bloque 1", "Punto 1", "Bloque 2", "Punto 2", "Bloque 3", "Punto 3", "Bloque 4", "Aceptación"]
    transiciones = [("Inicio", "Bloque 1", "0-255"),
                    ("Bloque 1", "Punto 1", "."),
                    ("Punto 1", "Bloque 2", "0-255"),
                    ("Bloque 2", "Punto 2", "."),
                    ("Punto 2", "Bloque 3", "0-255"),
                    ("Bloque 3", "Punto 3", "."),
                    ("Punto 3", "Bloque 4", "0-255"),
                    ("Bloque 4", "Aceptación", "Fin")]
    
    for estado in estados:
        G.add_node(estado)
    
    for origen, destino, etiqueta in transiciones:
        G.add_edge(origen, destino, label=etiqueta)
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Autómata Finito No Determinista para IPv4")
    plt.show()

def dibujar_afn_ipv6():
    G = nx.DiGraph()
    estados = ["Inicio", "Segmento 1", "DosPuntos 1", "Segmento 2", "DosPuntos 2", "Segmento 3", "DosPuntos 3", 
               "Segmento 4", "DosPuntos 4", "Segmento 5", "DosPuntos 5", "Segmento 6", "DosPuntos 6", 
               "Segmento 7", "DosPuntos 7", "Segmento 8", "Aceptación"]
    transiciones = [("Inicio", "Segmento 1", "0000-FFFF"),
                    ("Segmento 1", "DosPuntos 1", ":"),
                    ("DosPuntos 1", "Segmento 2", "0000-FFFF"),
                    ("Segmento 2", "DosPuntos 2", ":"),
                    ("DosPuntos 2", "Segmento 3", "0000-FFFF"),
                    ("Segmento 3", "DosPuntos 3", ":"),
                    ("DosPuntos 3", "Segmento 4", "0000-FFFF"),
                    ("Segmento 4", "DosPuntos 4", ":"),
                    ("DosPuntos 4", "Segmento 5", "0000-FFFF"),
                    ("Segmento 5", "DosPuntos 5", ":"),
                    ("DosPuntos 5", "Segmento 6", "0000-FFFF"),
                    ("Segmento 6", "DosPuntos 6", ":"),
                    ("DosPuntos 6", "Segmento 7", "0000-FFFF"),
                    ("Segmento 7", "DosPuntos 7", ":"),
                    ("DosPuntos 7", "Segmento 8", "0000-FFFF"),
                    ("Segmento 8", "Aceptación", "Fin")]
    
    for estado in estados:
        G.add_node(estado)
    
    for origen, destino, etiqueta in transiciones:
        G.add_edge(origen, destino, label=etiqueta)
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Autómata Finito No Determinista para IPv6")
    plt.show()

# Ejemplos
print(reconocer_direccion("192.168.1.1"))  # IPv4 válida
print(reconocer_direccion("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # IPv6 válida
print(reconocer_direccion("999.999.999.999"))  # No válida

# Dibujar AFN para IPv4 e IPv6
dibujar_afn_ipv4()
dibujar_afn_ipv6()
