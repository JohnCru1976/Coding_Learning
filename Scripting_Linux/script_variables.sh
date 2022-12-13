#! /bin/sh
echo "Mal definida":
echo "(orden no encontrada)":
# Mal definida por existir espacios
# antes y después del =
VAR = 1
echo "Variables bien definidas:"
VAR=1
VAR1=2
var=3
# Muestra: Variables: 1 2 3
echo "Variables: $VAR $VAR1 $var"
# Muestra: Variable VAR: 1
echo "Variable VAR: $VAR"
# Muestra: Variable VAR1: 2
echo "Variable VAR1: $VAR1"
# Muestra: VAR seguida de 1: 11
echo "VAR seguida de 1: ${VAR}1"
# Muestra: Comillas dobles: 1
echo "Comillas dobles: $VAR"
# Muestra: Comillas simples: $VAR
echo 'Comillas simples: $VAR'
# Muestra: Valor 1-1
echo "Valor: $VAR-1"