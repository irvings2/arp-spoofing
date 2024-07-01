from scapy.all import sr1, ARP, conf
import os

def obtener_mac_legitima(ip):
    respuesta = sr1(ARP(pdst=ip), timeout=2, verbose=False)
    if respuesta:
        return respuesta.hwsrc
    else:
        return None

def obtener_tabla_arp():
    if os.name == 'nt':
        output = os.popen('arp -a').read()
        return output
    else:
        output = os.popen('arp').read()
        return output

def analizar_tabla_arp(tabla, ip_objetivo, mac_legitima):
    if mac_legitima in tabla:
        print("La dirección MAC del router coincide con la dirección legítima.")
    else:
        print("¡Alerta! La dirección MAC del router ha sido modificada.")
        print(f"Dirección MAC esperada: {mac_legitima}")
        print("Tabla ARP actual:")
        print(tabla)

def main():
    ip_router = input("Dirección IP Puerta de enlace (Router): ")

    mac_legitima = obtener_mac_legitima(ip_router)
    if not mac_legitima:
        print("No se pudo obtener la dirección MAC del router.")
        return

    print(f"Dirección MAC legítima del router: {mac_legitima}")

    tabla_arp = obtener_tabla_arp()

    analizar_tabla_arp(tabla_arp, ip_router, mac_legitima)

if __name__ == "__main__":
    main()