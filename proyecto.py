import os
import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# Verificar si Firebase ya está inicializado para evitar errores
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate("moviescreds.json")  # Asegúrate de que el archivo existe
        firebase_admin.initialize_app(cred, {"projectId": "movies-94cb0"})  # Reemplázalo con tu ID de proyecto
    except Exception as e:
        st.error(f"Error al inicializar Firebase: {e}")

