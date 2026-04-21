#!/bin/bash
# Script para inicializar la base de datos en el primer despliegue

echo "Esperando a que PostgreSQL esté lista..."
sleep 10

echo "Creando usuario administrador..."
python create_admin.py

echo "Iniciando servidor..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000