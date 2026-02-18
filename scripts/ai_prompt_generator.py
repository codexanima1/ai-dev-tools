"""
AI Prompt Generator - Generador de prompts optimizados para AI

Este script genera prompts optimizados para usar con ChatGPT, Claude, y otros LLMs.
Útil para developers que trabajan con AI.
"""

def generate_code_explanation_prompt(code_snippet, language="python"):
    """
    Genera un prompt para explicar código.
    """
    prompt = f"""
Explica este código en {language} de forma clara y concisa:

```{language}
{code_snippet}
```

Incluye:
1. Qué hace el código
2. Cómo funciona (lógica principal)
3. Posibles mejoras o consideraciones
"""
    return prompt


def generate_refactor_prompt(code_snippet, language="python"):
    """
    Genera un prompt para refactorizar código.
    """
    prompt = f"""
Refactoriza este código {language} para que sea más limpio y mantenible:

```{language}
{code_snippet}
```

Mejoras esperadas:
- Nombres de variables claros
- Estructura modular
- Eliminación de código redundante
- Mejores prácticas de {language}
"""
    return prompt


def generate_debug_prompt(code_snippet, error_message=None):
    """
    Genera un prompt para debugging.
    """
    prompt = f"""
Analiza este código y encuentra el/los bug(s):

```{language}
{code_snippet}
```
"""
    if error_message:
        prompt += f"\nError actual:\n{error_message}"
    
    prompt += """
Explica:
1. Cuál es el problema
2. Por qué ocurre
3. Cómo solucionarlo
4. Cómo evitarlo en el futuro
"""
    return prompt


def generate_documentation_prompt(code_snippet, language="python"):
    """
    Genera un prompt para crear documentación.
    """
    prompt = f"""
Genera documentación para este código:

```{language}
{code_snippet}
```

Incluye:
1. Descripción general
2. Función de cada componente
3. Parámetros y retornos
4. Ejemplos de uso
5. Casos edge
"""
    return prompt


def main():
    """Demo del generador de prompts."""
    print("=" * 50)
    print("AI Prompt Generator - Demo")
    print("=" * 50)
    
    # Ejemplo de uso
    example_code = """
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)
"""
    
    print("\n1. Prompt para explicar código:")
    print(generate_code_explanation_prompt(example_code, "python"))
    
    print("\n2. Prompt para refactorizar:")
    print(generate_refactor_prompt(example_code, "python"))
    
    print("\n3. Prompt para debugging:")
    print(generate_debug_prompt(example_code, "RecursionError: maximum recursion depth exceeded"))


if __name__ == "__main__":
    main()
