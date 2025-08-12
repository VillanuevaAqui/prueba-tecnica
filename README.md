# Microservicio Django REST - Productos

Microservicio que expone una API RESTful para la gestión de productos (CRUD), construido con Django 4.2+, Django REST Framework y SQLite.

---

## Características

- CRUD completo para el modelo Producto: crear, listar, obtener, actualizar y eliminar.
- Documentación automática con Swagger (drf-spectacular).
- Pruebas automáticas básicas para endpoints.
- Configurado para ejecución local y con Docker.

---

## Requisitos

- Python 3.11+
- Docker y docker-compose (opcional para contenedor)
- Git (opcional para clonar)

---

## Instalación

### local

Clonar el repositorio y configura el entorno virtual:

```bash
git clone <url-del-repositorio>
cd <nombre-repo>
python -m venv venv 
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate.bat   # Windows (CMD)
.\venv\Scripts\Activate.ps1 # Windows (PowerShell)
pip install -r requirements.txt
```
Ejecutar migraciones
```
python manage.py migrate
```

Iniciar servidor 
```
python manage.py runserver
```

### docker
Clonar repositorio
```
git clone <url-del-repositorio>
cd <nombre-repo>
```

Crear el contenedor y ejecutar el servicio (migraciones y servidor)

```
docker-compose up --build
```

## Pruebas automaticas
### Local

En la directorio raiz escribe este comando

```
python manage.py test
```
Salida Esperada 
```
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.039s

OK
Destroying test database for alias 'default'...
```

### Docker

En el directorio raiz ejecuta este comando

```
docker-compose run --rm web python manage.py test
```
Salida Esperada

```
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.016s

OK
Destroying test database for alias 'default'...
```
## Documentacion automatica de Endpoints 

Una vez iniciado el servicio puede consultar la documentación de los endpoints desde este URL 

http://localhost:8000/api/docs/