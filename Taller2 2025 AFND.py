from graphviz import Digraph

def generar_automata_ipv4_ipv6():
    dot = Digraph(format='png')
    
    # Definir estados
    estados = ["q0", "h1", "dp1", "h2", "dp2", "h3", "dp3", "h4", "dp4", "h5", "dp5", "h6", "dp6", "h7", "dp7", "h8", "fin"]
    estados_aceptacion = ["fin"]
    
    # Agregar estados al gráfico
    dot.node("q0", shape="circle")  # Estado inicial
    for estado in estados:
        if estado in estados_aceptacion:
            dot.node(estado, shape="doublecircle")  # Estados de aceptación
        else:
            dot.node(estado, shape="circle")
    
    # Definir transiciones IPv4
    dot.edge("q0", "h1", label="000-255")
    dot.edge("h1", "dp1", label=".")
    dot.edge("dp1", "h2", label="000-255")
    dot.edge("h2", "dp2", label=".")
    dot.edge("dp2", "h3", label="000-255")
    dot.edge("h3", "dp3", label=".")
    dot.edge("dp3", "h4", label="000-255")
    dot.edge("h4", "fin", label="Fin IPv4")
    
    # Definir transiciones IPv6
    dot.edge("q0", "h5", label="0000-FFFF")
    dot.edge("h5", "dp4", label=":")
    dot.edge("dp4", "h6", label="0000-FFFF")
    dot.edge("h6", "dp5", label=":")
    dot.edge("dp5", "h7", label="0000-FFFF")
    dot.edge("h7", "dp6", label=":")
    dot.edge("dp6", "h8", label="0000-FFFF")
    dot.edge("h8", "dp7", label=":")
    dot.edge("dp7", "fin", label="Fin IPv6")
    
    # Guardar y renderizar
    dot.render("automata_ipv4_ipv6", view=True)

# Generar la imagen del autómata
generar_automata_ipv4_ipv6()
