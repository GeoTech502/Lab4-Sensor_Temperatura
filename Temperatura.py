import pyfirmata
from datetime import datetime

PAUSA = 5 # Número de segundos entre tomas de lectura
           # de temperatura.

placa = pyfirmata.Arduino('COM3')

pyfirmata.util.Iterator(placa).start()

entrada = placa.get_pin('a:0:i')
entrada.enable_reporting()

def volts_to_celsius(v):
    """Convierte un voltaje v obtenido de un sensor
       TMP36 a grados Celsius.
    """
    return 100 * (v - 0.5)

def celsius_to_fahrenheit(c):
    """Convierte c grados Celsius a grados Ffahrenheit.
    """
    return 1.8 * c + 32

try:
    while True:
        d = datetime.now()
        v = entrada.read()
        if v != None:
            v *= 5 # Convertir el valor devuelto por
                   # read() a voltios.

            c = volts_to_celsius(v)
            f = celsius_to_fahrenheit(c)
            print('{}, {:.3f} V, {:.2f} °C, {:.2f} °F'
                  .format(d, v, c, f))
            placa.pass_time(PAUSA)

except KeyboardInterrupt:
    # Terminar programa cuando se presione Ctrl-C.
    pass

finally:
    placa.exit()