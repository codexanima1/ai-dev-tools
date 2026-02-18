"""
GitHub Stats - Estadísticas de perfil de GitHub

Este script muestra estadísticas básicas de un perfil de GitHub.
Útil para developers que quieren mostrar su actividad.
"""

import requests
from datetime import datetime, timedelta


def get_user_info(username):
    """Obtiene información básica del usuario."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_user_repos(username, sort="updated", per_page=5):
    """Obtiene los repositorios más recientes."""
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": sort, "per_page": per_page}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return []


def get_contributions(username):
    """Obtiene contribuciónes del último año."""
    # GitHub no tiene API pública para contribuciones
    # Este es un placeholder que retorna info básica
    user_info = get_user_info(username)
    if user_info:
        return {
            "public_repos": user_info.get("public_repos", 0),
            "followers": user_info.get("followers", 0),
            "following": user_info.get("following", 0),
            "created_at": user_info.get("created_at", "")
        }
    return None


def print_profile_stats(username):
    """Imprime las estadísticas del perfil."""
    print("=" * 50)
    print(f"GitHub Stats - @{username}")
    print("=" * 50)
    
    info = get_user_info(username)
    if not info:
        print(f"Usuario {username} no encontrado.")
        return
    
    print(f"\n📊 Estadísticas:")
    print(f"  Repositorios públicos: {info.get('public_repos', 0)}")
    print(f"  Seguidores: {info.get('followers', 0)}")
    print(f"  Siguiendo: {info.get('following', 0)}")
    
    created = info.get('created_at', '')
    if created:
        print(f"  Miembro desde: {created[:10]}")
    
    print(f"\n🔗 Perfil: {info.get('html_url', '')}")
    print(f"  Bio: {info.get('bio', 'Sin bio')}")


def print_recent_repos(username, count=5):
    """Imprime los repositorios más recientes."""
    print(f"\n📦 Últimos {count} repositorios:")
    
    repos = get_user_repos(username, per_page=count)
    for i, repo in enumerate(repos, 1):
        print(f"\n{i}. {repo.get('name', 'N/A')}")
        print(f"   ⭐ {repo.get('stargazers_count', 0)} | 🍴 {repo.get('forks_count', 0)}")
        print(f"   📝 {repo.get('description', 'Sin descripción')}")
        print(f"   🔗 {repo.get('html_url', '')}")


def main():
    """Demo del script."""
    print("=" * 50)
    print("GitHub Profile Stats")
    print("=" * 50)
    
    # Ejemplo con un usuario de prueba
    example_user = "octocat"  # Usuario de ejemplo de GitHub
    
    print(f"\nEjemplo con @{example_user}:")
    print_profile_stats(example_user)
    print_recent_repos(example_user)


if __name__ == "__main__":
    main()
