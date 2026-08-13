import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Soporte Técnico", page_icon="💻")

st.title("💻 Soporte Técnico en la Nube")
st.write("Por favor, completa el siguiente formulario para reportar un problema.")

with st.form("reporte_form"):
    nombre = st.text_input("Nombre")
    email_usuario = st.text_input("Correo electrónico")
    tipo_problema = st.selectbox("Tipo de problema", ["Hardware", "Software", "Red", "Otro"])
    prioridad = st.selectbox("Prioridad", ["Baja", "Media", "Alta"])
    descripcion = st.text_area("Descripción del problema")
    
    enviar = st.form_submit_button("Enviar Reporte")

if enviar:
    if not nombre or not email_usuario or not descripcion:
        st.error("Por favor completa todos los campos.")
    else:
        try:
            # Lee las credenciales de forma segura desde Streamlit Secrets
            email_admin = st.secrets["EMAIL_ADMIN"]
            password = st.secrets["EMAIL_PASSWORD"]
            
            msg = EmailMessage()
            msg.set_content(f"Nuevo reporte de: {nombre}\nEmail: {email_usuario}\nTipo: {tipo_problema}\nPrioridad: {prioridad}\n\nDescripción:\n{descripcion}")
            msg["Subject"] = f"Reporte de Soporte: {tipo_problema}"
            msg["From"] = email_usuario
            msg["To"] = email_admin
            
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_admin, password)
                smtp.send_message(msg)
                
            st.success("¡Reporte enviado correctamente!")
        except Exception as e:
            st.error(f"Error al enviar: {e}")
