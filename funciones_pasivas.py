import dns.resolver
import whois
import shodan
import ssl
import socket
import requests

SHODAN_API_KEY = "..." #Ingresar tu shodan ApiKey

def dns_lookup(domain):
    print("- Consultando registros DNS...")
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    dns_results = {}

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            data = []
            for rdata in answers:
                data.append(str(rdata))
            dns_results[rtype] = data
        except Exception as e:
            dns_results[rtype] = f"Error: {str(e)}"

    return dns_results


def whois_lookup(domain):
    print("- Consultando WHOIS...")
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers,
            "emails": w.emails
        }
    except Exception as e:
        return {"error": str(e)}
    

def shodan_lookup(domain):
    print("- Consultando Shodan...")
    try:
        ip = dns.resolver.resolve(domain, "A")[0].to_text()
        api = shodan.Shodan(SHODAN_API_KEY)
        host = api.host(ip)
        return {
            "ip": ip,
            "organization": host.get("org"),
            "os": host.get("os"),
            "ports": host.get("ports"),
            "data": host.get("data")
        }
    except Exception as e:
        return {"error": str(e)}
    

def get_tls_info(domain):
    print("- Obteniendo información TLS...")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return {
                    "subject": cert.get("subject"),
                    "issuer": cert.get("issuer"),
                    "valid_from": cert.get("notBefore"),
                    "valid_to": cert.get("notAfter"),
                    "serial_number": cert.get("serialNumber")
                }
    except Exception as e:
        return {"error": str(e)}
    

def enumerate_subdomains(domain):
    print("- Enumerando subdominios desde crt.sh...")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    if sub.endswith(domain):
                        subdomains.add(sub.strip())
        return sorted(subdomains)
    except Exception as e:

        return {"error": str(e)}
