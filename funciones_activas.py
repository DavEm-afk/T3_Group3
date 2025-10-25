import nmap
from scapy.all import IP, ICMP, sr1

def scan_ports(domain):
    print("- Escaneando puertos con Nmap...")
    try:
        scanner = nmap.PortScanner()
        puertos_str = ",".join(str(p) for p in [80, 443])
        scanner.scan(domain, ports=puertos_str, arguments='-Pn -T4')  
        return scanner[domain]
    except Exception as e:
        return {"error": str(e)}
    

def send_packets(domain):
    print("- Enviando paquetes ICMP...")
    try:
        packet = IP(dst=domain)/ICMP()
        response = sr1(packet, timeout=2, verbose=0)
        if response:
            return {
                "status": "Recibido",
                "ttl": response.ttl,
                "src": response.src
            }
        else:
            return {"status": "Sin respuesta"}
    except Exception as e:
        return {"error": str(e)}