# Instrucciones generales:
  1. Reemplazar el controlador a probar en la carpeta pox/pox/forwarding/l2_learning.py
  2. Ejecutar pox con comando "./pox.py openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.l2_learning"
  3. Ejecutar la topologia    "sudo mn --custom redes.py --topo RED --controller remote", donde RED corresponde o bien a red1 o bien a red2.
  4. Esperar que la ventana de pox anuncie que los puertos se han actualizado (30s app.)

# Para la red 1:

  1. El archivo l2_learning-P1a.py es una copia del controlador original. Esto permite, con los párametros antes dados, realizar un pingall exitoso sin algún otro menester.
  2. El archivo l2_learning-P1b.py es una modificación del contolador original. Este actualiza las tablas de flujo para seguir el sentido horario especificado, en la ventana de pox se muestra información del rute seguido por cada paquete por protocolo ICMP.
  3. El análisis en wireshark de eliminar una conexión, se adjunta en el informe.

# Para la red 2:

  1. Abrir los servicios http en los host 5 y 6 con el comando "h_i python -m SimpleHTTPServer 80 &" donde "i" corresponde a 5, y 6. 
