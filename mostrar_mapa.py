import matplotlib.pyplot as plt

def mostrar_mapa(gdf):
  
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(10, 8))

    # Graficar la geometría
    gdf.plot(ax=ax, edgecolor="black", linewidth=0.8)

    # Agregar título
    ax.set_title("Mapa del GeoDataFrame", fontsize=14)

    # Quitar ejes
    ax.set_axis_off()

    # Mostrar mapa
    plt.show()
