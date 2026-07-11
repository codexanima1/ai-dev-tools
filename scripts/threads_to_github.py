#!/usr/bin/env python3
"""
threads_to_github.py — Conecta tus posts de Threads con commits en GitHub.
Genera un commit por cada post publicado para mantener el calor en GitHub.
"""

import os
import sys
import random
from datetime import datetime, timedelta

QUOTES = [
    "La IA no reemplaza devs, los potencia.",
    "Código limpio > código inteligente.",
    "Siempre haz git push antes de dormir.",
    "Un buen README vale más que mil issues.",
    "La consistencia vence a la intensidad.",
    "Primero hazlo funcionar, luego hazlo bonito.",
    "Los bugs son solo features no documentadas.",
    "Comenta tu código como si el que lo herede fuera un psicópata.",
    "Menos framework, más lógica.",
    "El mejor código es el que no escribiste.",
    "YAGNI: You Ain't Gonna Need It.",
    "No repitas, abstrae.",
    "Un commit por día mantiene el repo al día.",
    "La IA es tu copiloto, no tu piloto.",
]

def generate_commit():
    """Genera un archivo de log diario y lo commitea."""
    today = datetime.now()
    log_file = "daily_log.md"
    
    # Create or append to daily log
    entry = f"\n## {today.strftime('%Y-%m-%d')}\n\n"
    entry += f"**Status:** Active 🟢\n\n"
    entry += f"**Quote of the day:** {random.choice(QUOTES)}\n\n"
    entry += f"---\n"
    
    with open(log_file, "a") as f:
        f.write(entry)
    
    return log_file, f"Daily commit: {today.strftime('%Y-%m-%d')}"

if __name__ == "__main__":
    log_file, msg = generate_commit()
    print(f"Generated: {log_file}")
    print(f"Message: {msg}")
