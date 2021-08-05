Los nombres utilizados en la topologías son consistentes con los usados en el pdf explicando el lab
# Instrucciones generales:

  1. Se recomienda reemplazar el controlador a probar en la carpeta pox/pox/forwarding/l2_learning.py, también puede intentar simplemente poner los archivos en la carpeta pox/pox/forwarding.
  2. Ejecutar pox con comando "./pox.py openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.l2_learning" o, si dejó los archivos en la carpeta, cambie "forwarding.l2_learning" por "forwarding.archivo_controlador", siendo "archivo_controlador" el que usted desee ejecutar.
  3. Ejecutar la topologia    "sudo mn --custom redes.py --topo RED --controller remote", donde RED corresponde a red1 o bien a red2.
  4. Esperar que la ventana de pox anuncie que los puertos se han actualizado (30s app.).

# Para la red 1:

  1. El archivo l2_learning-P1a.py es una copia del controlador original. Esto permite, con los párametros antes dados, realizar un pingall exitoso sin algún otro menester.
  2. El archivo l2_learning-P1b.py es una modificación del contolador original. Este actualiza las tablas de flujo para seguir el sentido horario especificado, en la ventana de pox se muestra información del route seguido por cada paquete por protocolo ICMP.
  3. El análisis en wireshark de eliminar una conexión, se adjunta en el informe.

# Para la red 2:

  1. Abrir los servicios http en los host 5 y 6 con el comando "h_i python -m SimpleHTTPServer 80 &" donde "i" corresponde a 5 y 6. Si tiene problemas intente con "hi python3 -m http.server 80 &", donde "i" corresponde a 5 y 6.
  2. Para hacer un request a alguno de los servidores debe usar el comando "hi wget -O - hj", siendo "i" el numero de host 1, 2, 3 o 4 y "j" el numero de host/servidor 5 o 6

