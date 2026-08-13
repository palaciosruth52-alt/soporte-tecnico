# Soporte Técnico en la Nube

Una aplicación web desarrollada con **Streamlit** y Python que permite a los usuarios enviar formularios de reporte de problemas técnicos directamente al correo del administrador mediante un servidor SMTP.

##  Características

* **Interfaz intuitiva:** Formulario rápido y fácil de usar para registrar incidencias.
* **Clasificación de reportes:** Selección de tipo de problema (Hardware, Software, Red, Otro) y niveles de prioridad (Baja, Media, Alta).
* **Notificaciones por correo:** Envío automático de notificaciones por email al equipo de soporte utilizando SMTP de Gmail.

##  Tecnologías utilizadas

* [Python](https://www.python.org/) - Lenguaje de programación principal.
* [Streamlit](https://streamlit.io/) - Framework para la creación de la interfaz web.
* `smtplib` y `email` - Librerías nativas de Python para la gestión y envío de correos electrónicos.

##  Requisitos previos

Asegúrate de tener instalado en tu computadora:
* Python 3.8 o superior.
* Una cuenta de correo de Gmail con una **Contraseña de Aplicación** generada (si vas a utilizar la funcionalidad de envío de correos).


##  Instalación y Ejecución local

1. Clona este repositorio o descarga los archivos en tu computadora:
   ```bash
   git clone https://github.com/palaciosruth52-alt/soporte-tecnico.git
   cd soporte-tecnico
