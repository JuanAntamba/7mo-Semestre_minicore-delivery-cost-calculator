# 📦 Mini Core: Calculadora de Costos Logísticos (MVC)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Sass](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

Proyecto académico (7mo Semestre) desarrollado para demostrar la implementación práctica del patrón de diseño **MVC (Modelo-Vista-Controlador)** a través del framework Django.

La aplicación resuelve un problema logístico concreto: calcular el costo total de envíos realizados por distintos repartidores dentro de un rango de fechas, aplicando tarifas dinámicas según la zona de entrega.

---

## 🚀 Enlaces del Proyecto

- **🌐 Demo en Producción (Render):** https://tu-link.onrender.com
- **🎥 Video Explicativo:** Enlace al video de YouTube/Drive próximamente...

---

## 🧠 Arquitectura Utilizada: Django MVT (Variante de MVC)

Django utiliza una adaptación del patrón MVC conocida como **MVT (Model-View-Template)**. En este Mini Core, las responsabilidades están estrictamente separadas de la siguiente manera:

### 📊 Modelo (Datos)

Tablas relacionales (`Repartidor`, `Zona`, `Envio`) gestionadas mediante el ORM de Django. Se evitó la creación manual de registros mediante el uso de un script de automatización (*Data Seeding*).

### ⚙️ Vista / Controlador (Lógica)

Recibe las fechas ingresadas por el usuario y procesa la lógica matemática directamente en la base de datos utilizando funciones de agregación como:

- `Sum()`
- `Count()`
- `F()`

Esto garantiza eficiencia y un menor consumo de memoria.

### 🎨 Template / Presentación

Interfaz construida con HTML5 semántico y estilos escalables organizados mediante la metodología **BEM (Block Element Modifier)** y compilados con **SCSS**.

---

## ⚙️ Instrucciones para Ejecutar Localmente

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JuanAntamba/7mo-Semestre_minicore-delivery-cost-calculator.git
cd 7mo-Semestre_minicore-delivery-cost-calculator
```

### 2️⃣ Crear y activar el entorno virtual

#### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### En Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Base de Datos y Datos Semilla

El repositorio incluye el archivo `db.sqlite3` listo para usarse con los datos matemáticos exactos del caso de estudio (envíos de mayo de 2025).

Si deseas limpiar y regenerar la base de datos desde cero, ejecuta:

```bash
python manage.py seed_data
```

### 5️⃣ Levantar el servidor

```bash
python manage.py runserver
```

Luego abre en tu navegador:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Cómo Probar la Aplicación

Para validar la lógica matemática implementada en el controlador, ingresa los siguientes valores:

| Campo | Valor |
|---------|---------|
| Fecha Inicio | 01/05/2025 |
| Fecha Fin | 31/05/2025 |

### ✅ Resultado Esperado

| Repartidor | Envíos | Peso Total | Costo |
|------------|---------|------------|---------|
| Andrés | 5 | 32 kg | $48.00 |
| Camila | 3 | 18 kg | $36.00 |
| Luis | 0 | 0 kg | $0.00 (No aplica) |

---

## 🛠️ Tecnologías Utilizadas

- Python
- Django
- SQLite3
- HTML5
- SCSS / Sass
- CSS3
- Render

---

## 👨‍💻 Autor

**Juan Carlos Antamba**  
Estudiante de Ingeniería de Software  
Universidad de Las Américas (UDLA)

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos como parte de las actividades de séptimo semestre de Ingeniería de Software.