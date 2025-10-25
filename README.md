# Proyecto T3 – Reconocimiento pasivo y activo de dominio

Este proyecto realiza un escaneo pasivo y activo sobre un dominio, utilizando herramientas de ciberseguridad con motivos eticos y las prevenciones necesarias.

## Requisitos
Los módulos externos utilizados en este proyecto son:

- `python-nmap`
- `scapy`
- `dnspython`
- `python-whois`
- `shodan`
- `requests`

Instalación de módulos:
`pip install -r requirements.txt`

Otros módulos utilizados:

- `argparse`
- `json`
- `datetime`
- `ssl`
- `socket`

## Ejecución 
Solo análisis pasivo:
`python main.py "dominio.com"`

Analisis pasivo y activo (requiere autorización):
`python main.py "dominio.com" --run-active` 

Ver ayuda de ejecución:
`python main.py --help`

## Advertencia
Este proyecto está diseñado únicamente para fines académicos. 
El análisis activo requiere de la autorización del encargado del dominio a escanear. Ademas de su activación por medio del parámetro'--run-active', se necesita editar directamente los permisos dentro del codigo fuente 'main.py' para habilitar el escaneo activo.

## Documentación adicional
- [Evidencias del análisis](Evidencias/) – incluye reportes, captura de pantalla y ensayo
- [Autorización para escaneo activo](Autorizacion/)

## Créditos
Este proyecto fue desarrollado como parte de la unidad de aprendizaje Programación para Ciberseguridad, correspondiente al periodo académico de agosto-diciembre 2025.
Integrantes del equipo:
- Marcelo Hernández Chávez
- David Emiliano Rangel Tovar


