# Actualizar un paquete concreto
    # pip install --upgrade nombre-del-modulo

# Ejemplo para actualizar TODOS los paquetes en el CMD de Windows
    # pip freeze --local | ForEach-Object { $_ -replace '==.*', '' } | ForEach-Object { pip install --upgrade $_ }

# Listado de paquetes
    # pip list

# Listado de paquetes outdated
    # pip list --outdated 