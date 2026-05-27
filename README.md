# PanelBox (Box Digital)

Sistema digital de **reservas y gestión de salas Box** en establecimientos de salud.

En el contexto clínico, un **“Box”** es la sala donde se realizan procedimientos o atenciones. PanelBox permite administrar de forma eficiente la disponibilidad y la reserva de estos espacios para:

- Personal **SOME** (admisión/gestión de horas)
- Personal de salud **médico** y **no médico**
- Personal **administrativo** del centro

## Tecnologías

- **Backend:** Django + Django REST Framework
- **Frontend:** React (Vite)
- **Base de datos:** PostgreSQL
- **Infraestructura:** desarrollo local con entorno virtual (plan de migración a Docker)

## Requisitos

- **Python** (recomendado: 3.12+)
- **Node.js** (recomendado: 18+ o 20+)
- **PostgreSQL** (local)

> Nota: el proyecto actualmente tiene configuraciones de BD directamente en `somePro/settings.py`. Para un entorno real se recomienda mover credenciales a variables de entorno.

## Configuración de base de datos (PostgreSQL)

En `somePro/settings.py` se utiliza PostgreSQL. Ajusta los valores según tu entorno:

- `NAME`
- `USER`
- `PASSWORD`
- `HOST`
- `PORT`

## Backend (Django)

### 1) Crear y activar entorno virtual

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 2) Instalar dependencias

Este repositorio aún no incluye un `requirements.txt` en la raíz.

Opciones recomendadas:

1. **Crear un `requirements.txt`** con las dependencias del proyecto (ej: `Django`, `djangorestframework`, `django-cors-headers`, `psycopg2`/`psycopg2-binary`, `djangorestframework-simplejwt`, `ipython`, etc.).
2. Instalar manualmente en el entorno virtual.

Ejemplo (ajustar versiones según corresponda):

```bash
pip install Django djangorestframework django-cors-headers psycopg2-binary djangorestframework-simplejwt ipython
```

### 3) Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4) Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 5) Levantar servidor

```bash
python manage.py runserver
```

Backend local:

- `http://localhost:8000`

## Frontend (React + Vite)

### 1) Instalar dependencias

```bash
cd frontend
npm install
```

### 2) Ejecutar en desarrollo

```bash
npm run dev
```

> Vite normalmente levanta el frontend en `http://localhost:5173` (puede variar si el puerto está ocupado).

## Estado del proyecto

En **desarrollo**.

## Roadmap (tentativo)

- Contenerización con **Docker** (backend + frontend + PostgreSQL)
- Variables de entorno para configuración (DB, secret key, CORS, etc.)
- Documentación de endpoints y flujo de reservas

## Autor

- **Matías Silva**

---

### Notas de seguridad

- No se recomienda mantener `SECRET_KEY` ni credenciales de base de datos hardcodeadas en `settings.py` para ambientes reales.
