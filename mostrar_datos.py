def mostrar_datos(gdf, localidad=None):
   
    columnas = ['NOMBRE', 'CODIGO_LOCALIDAD']

    # Verificar columnas
    for col in columnas:
        if col not in gdf.columns:
            raise KeyError(f"La columna '{col}' no está en el GeoDataFrame")

    # Si se especifica localidad, filtrar (los códigos son strings)
    if localidad is not None:
        localidad = str(localidad)  # asegurar string
        gdf_filtrado = gdf[gdf['CODIGO_LOCALIDAD'] == localidad]
        nombre_archivo = f"barrios_localidad_{localidad}.csv"
    else:
        gdf_filtrado = gdf
        nombre_archivo = "barrios_todas_localidades.csv"

    # Guardar CSV
    gdf_filtrado[columnas].to_csv(nombre_archivo, index=False, encoding='utf-8')

    # Mostrar primeras filas
    print(gdf_filtrado[columnas].head())

    print(f"\n Archivo CSV generado: {nombre_archivo}")
