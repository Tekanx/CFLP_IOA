# Laboratorio 2
Inv. de Operaciones Avanzada

Fecha Entrega Tarea: 24/11/22
Grupos de 3-4 personas
La copia se penalizará con nota 1 para todos los integrantes del (los) grupo(s) involucrado(s)
Si bien es posible encontrar código que realice tareas similares a las que se solicitan en este
Laboratorio, es indispensable que TODO el código que se presente sea de autoría de los integrantes del
grupo.
La implementación de la solución debe cumplir con los siguientes requisitos:

• Pueda ser ejecutado, al menos, en Linux y MS-Windows

• Utilice AMPL/JuMP

• Utilice Gurobi

• Permita resolver instancias del CFLP desde 50x50 hasta 5000x5000 (clientes x localizaciones)

Las instancias de prueba y el detalle del formato de los archivos de entrada de las mismas, se encuentra
en la “OR Library” (http://people.brunel.ac.uk/~mastjjb/jeb/orlib/capinfo.html)
La solución debe constar de un algoritmo heurístico a elección, el cual será el encargado de buscar
buenas combinaciones de centros, y de un algoritmo exacto (AMPL+Gurobi) el cual será el encargado
de encontrar la asignación óptima dado un conjunto de centros abiertos. El algoritmo deberá tener
como criterio de término un número de iteraciones máxima, ingresada por el usuario.
La entrega consiste en un archivo .zip el cual deberá contener todos los archivos necesarios para la
ejecución del programa. Además, se deberá hacer entrega de un informe, el cual deberá contener la
siguiente información:

• Manual de Usuario, explicando como ejecutar el código para una instancia cualquiera (1-2
páginas). 5 pts

• Explicación del problema y el modelo CFLP utilizado (1-2 páginas) 5 pts.

• Explicación del algoritmo implementado, indicando estructuras utilizadas, funciones
principales, etc. (3-4 páginas) 15 pts

• Mostrar, gráficamente, y discutir sobre la convergencia del algoritmo para 4 instancias de la OR
Library. Se solicita considerar, al menos, 2 de las instancias más grandes del problema. (2-3
páginas) 5 pts

• Mostrar y Analizar los resultados del algoritmo para, al menos, una instancia de cada “Problem
Set” de la OR Library. El algoritmo se debe ejecutar, al menos, 10 veces por cada instancia. Se
deben reportar los resultados que ayuden a entender la consistencia del algoritmo. (2-3 páginas)
10 pts

• Reportar, para las instancias capa, capb y capc cómo cambian los resultados (y la eficiencia del
algoritmo) cuando se relaja la restricción de exclusividad de los centros sobre los clientes (i.e.
los clientes ahora pueden ser atendidos por más de un centro). Discutir sobre el por qué de los
cambios en los resultados y performance del algoritmo, si hubiese algún cambio. (2-3 páginas)
10 pts.
• Conclusiones (1 página) 5 pts

El programa debe estar claramente comentado, de tal forma de saber exactamente qué hace cada
parte/función del mismo. Los comentarios en el programa tendrán una puntuación máxima de 5 pts
puntos. Si se utiliza código externo, debe ser bien referenciado. Los programas sin comentarios (o con
muy pocos comentarios en el código) serán penalizados con -5 pts
Este Laboratorio exige el cumplimiento de todas las normas