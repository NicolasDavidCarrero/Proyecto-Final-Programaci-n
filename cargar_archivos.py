import geopandas as gpd

def cargar_archivo(nombre_archivo):


    gdf = gpd.read_file(nombre_archivo)

    return gdf
