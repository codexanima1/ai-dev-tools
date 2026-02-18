#!/bin/bash

# AI Developer Tools - Script de Configuración

echo "=========================================="
echo "AI Developer Tools - Setup"
echo "=========================================="

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado."
    exit 1
fi

echo "✅ Python encontrado"

# Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "✅ Setup completado!"
echo "=========================================="
echo ""
echo "Para activar el entorno virtual:"
echo "  source venv/bin/activate"
echo ""
echo "Para ejecutar los scripts:"
echo "  python scripts/ai_prompt_generator.py"
echo "  python scripts/github_stats.py"
echo ""
echo "¡Listo para contribuir!"
