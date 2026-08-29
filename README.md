# EjSonar — Ejemplo práctico de SonarQube / SonarCloud

Mini aplicación Python que se analiza automáticamente con **SonarCloud** en cada
`push` y en cada `pull_request`, demostrando un flujo de aseguramiento de la
calidad: pruebas + cobertura + análisis estático + Quality Gate.

## Estructura del repositorio

```
EjSonar/
├── app.py                        # Punto de entrada (CLI)
├── src/
│   ├── calculadora.py            # Operaciones aritméticas
│   └── texto.py                  # Utilidades de texto
├── tests/
│   ├── test_app.py
│   ├── test_calculadora.py
│   └── test_texto.py
├── requirements.txt              # pytest + pytest-cov
├── pytest.ini                    # Config de pruebas y cobertura
├── sonar-project.properties      # Identifica el proyecto ante SonarCloud
└── .github/workflows/sonarcloud.yml
```

## Ejecutar en local

```bash
pip install -r requirements.txt
pytest
```

`pytest` genera `coverage.xml` (formato Cobertura), que es el reporte que
SonarCloud importa para mostrar el porcentaje de cobertura.

Probar la app:

```bash
python app.py "6 * 7"
python app.py --texto "Anita lava la tina"
```

## Puesta en marcha de SonarCloud

1. **Crear el proyecto en SonarCloud**
   - Entrar a <https://sonarcloud.io> con la cuenta de GitHub.
   - *Analyze new project* → seleccionar este repositorio.
   - Elegir **GitHub Actions** como método de análisis.
   - Anotar la `Organization Key` y la `Project Key`.

2. **Guardar el token como secreto del repositorio**
   - SonarCloud muestra un `SONAR_TOKEN` al configurar el proyecto.
   - En GitHub: *Settings → Secrets and variables → Actions → New repository secret*
   - Nombre: `SONAR_TOKEN` — Valor: el token generado.

3. **Ajustar `sonar-project.properties`**
   - Reemplazar `sonar.organization` y `sonar.projectKey` por los valores reales.

4. **Desactivar "Automatic Analysis"** en SonarCloud
   (*Project → Administration → Analysis Method*) para que el análisis lo haga
   el workflow de GitHub Actions y no entre en conflicto.

## Qué hace el workflow (`.github/workflows/sonarcloud.yml`)

| Paso | Acción |
|------|--------|
| Checkout | Clona el repo con `fetch-depth: 0` (SonarCloud necesita el historial para el *new code*). |
| Setup Python | Prepara Python 3.12. |
| Instalar dependencias | `pip install -r requirements.txt`. |
| Pruebas + cobertura | `pytest --cov=src --cov=app --cov-report=xml` → `coverage.xml`. |
| SonarCloud Scan | La acción lee `sonar-project.properties`, envía código y cobertura usando `SONAR_TOKEN`. |

> El nombre actual de la acción es `SonarSource/sonarqube-scan-action`; se
> mantiene `sonarcloud-github-action@master` por compatibilidad con material previo.

## Qué revisa SonarCloud en este proyecto

- **Bugs / Code Smells**: p. ej. usar `eval()` para evaluar la expresión
  aritmética sería marcado; por eso `app.py` la parsea manualmente.
- **Cobertura de nuevo código**: el Quality Gate por defecto exige ≥ 80 %.
- **Código duplicado**: bloques repetidos entre módulos.
- **Security Hotspots**: entradas sin validar, secretos en el código, etc.
- **Complejidad ciclomática** y funciones demasiado largas.

## Quality Gate

Si el análisis no cumple las condiciones (cobertura insuficiente, bugs nuevos,
hotspots sin revisar…), el check de SonarCloud aparece en **rojo** sobre el
pull request y puede bloquear el *merge* si se marca como requerido en
*Branch protection rules*.
