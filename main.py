import argparse
import json
from funciones_activas import scan_ports, send_packets
from funciones_pasivas import dns_lookup, whois_lookup, shodan_lookup, enumerate_subdomains, get_tls_info
from datetime import datetime

AUTHORIZED = False  # Cambiar a True solo si se tiene permiso para ejecutar técnicas activas

print(f"Inicio: {datetime.now()}")

def run_passive(domain):
    print(f"\nEjecutando análisis pasivo sobre: {domain}")

    results = {

        "dns": dns_lookup(domain),
        "whois": whois_lookup(domain),
        "shodan": shodan_lookup(domain),
        "tls": get_tls_info(domain),
        "subdominios": enumerate_subdomains(domain)

    }

    with open("reporte_pasivo.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Reporte guardado en reporte_pasivo.json")


def run_active(domain):
    if not AUTHORIZED:
        print("\nBloque activo deshabilitado, se requiere autorización.")
        return
    print(f"\nEjecutando técnicas activas sobre: {domain}")

    results = {

        "port_scan": scan_ports(domain),
        "packet_test": send_packets(domain)

    }

    with open("reporte_activo.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Reporte activo guardado en reporte_activo.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="Dominio objetivo")
    parser.add_argument("--run-active", action="store_true", help="Ejecutar bloque activo (requiere autorización)")
    args = parser.parse_args()

    run_passive(args.domain)
    if args.run_active:
        print("\nADVERTENCIA: estás por ejecutar el bloque activo.")
        print("Asegúrate de tener autorización para escanear el dominio.")
        run_active(args.domain)