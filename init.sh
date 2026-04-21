#!/bin/bash
# Script para inicializar la base de datos en el primer despliegue

echo "Esperando a que PostgreSQL esté lista..."
sleep 10

echo "Creando usuario administrador..."
python create_admin.py || echo "Admin ya existe o hubo un error"

echo "Iniciando servidor..."
# Railway inyecta la variable PORT automáticamente
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}