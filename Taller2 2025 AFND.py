from graphviz import Digraph

def generar_automata_ipv4_ipv6():
    dot = Digraph(format='png')
    
     #  Configurar orientación horizontal
    dot.attr(rankdir='LR')  # Hace que el autómata sea de izquierda a derecha

    # Estados del autómata
    estados = [
        "q0", "ipv4_1", "punto1", "ipv4_2", "punto2", "ipv4_3", "punto3", "ipv4_4", "fin_ipv4",
        "ipv6_1", "dos_puntos1", "ipv6_2", "dos_puntos2", "ipv6_3", "dos_puntos3", "ipv6_4",
        "dos_puntos4", "ipv6_5", "dos_puntos5", "ipv6_6", "dos_puntos6", "ipv6_7", "dos_puntos7", 
        "ipv6_8", "fin_ipv6"
    ]
    
    estados_aceptacion = ["fin_ipv4", "fin_ipv6"]

    # Agregar nodos al grafo
    dot.node("q0", shape="circle", label="Inicio")
    
    for estado in estados:
        if estado in estados_aceptacion:
            dot.node(estado, shape="doublecircle")  # Estados de aceptación
        else:
            dot.node(estado, shape="circle")

    # Transiciones para IPv4 (Formato: X.X.X.X)
    dot.edge("q0", "ipv4_1", label="000-255")
    dot.edge("ipv4_1", "punto1", label=".")
    dot.edge("punto1", "ipv4_2", label="000-255")
    dot.edge("ipv4_2", "punto2", label=".")
    dot.edge("punto2", "ipv4_3", label="000-255")
    dot.edge("ipv4_3", "punto3", label=".")
    dot.edge("punto3", "ipv4_4", label="000-255")
    dot.edge("ipv4_4", "fin_ipv4", label="Fin IPv4")

    # Transiciones para IPv6 (Formato: XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX)
    dot.edge("q0", "ipv6_1", label="0000-FFFF")
    dot.edge("ipv6_1", "dos_puntos1", label=":")
    dot.edge("dos_puntos1", "ipv6_2", label="0000-FFFF")
    dot.edge("ipv6_2", "dos_puntos2", label=":")
    dot.edge("dos_puntos2", "ipv6_3", label="0000-FFFF")
    dot.edge("ipv6_3", "dos_puntos3", label=":")
    dot.edge("dos_puntos3", "ipv6_4", label="0000-FFFF")
    dot.edge("ipv6_4", "dos_puntos4", label=":")
    dot.edge("dos_puntos4", "ipv6_5", label="0000-FFFF")
    dot.edge("ipv6_5", "dos_puntos5", label=":")
    dot.edge("dos_puntos5", "ipv6_6", label="0000-FFFF")
    dot.edge("ipv6_6", "dos_puntos6", label=":")
    dot.edge("dos_puntos6", "ipv6_7", label="0000-FFFF")
    dot.edge("ipv6_7", "dos_puntos7", label=":")
    dot.edge("dos_puntos7", "ipv6_8", label="0000-FFFF")
    dot.edge("ipv6_8", "fin_ipv6", label="Fin IPv6")

    # Guardar y renderizar
    dot.render("automata_ipv4_ipv6", view=True)

# Generar la imagen del autómata
generar_automata_ipv4_ipv6()
