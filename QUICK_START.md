# ⚡ Guía Rápida - Data Structure Deeper

## 🎯 Tareas Comunes

### 1️⃣ Ejecutar Todos los Tests

```bash
pytest tests/ -v
```

### 2️⃣ Ejecutar Tests de una Estructura Específica

```bash
# Solo Singly Linked List
pytest tests/test_singly_linked_list.py -v

# Solo Doubly Linked List
pytest tests/test_doubly_linked_list.py -v
```

### 3️⃣ Ver Cobertura de Código (Terminal)

```bash
pytest tests/ --cov=linkendlist --cov-report=term-missing
```

### 4️⃣ Generar Reporte HTML de Cobertura

```bash
pytest tests/ --cov=linkendlist --cov-report=html
```

### 5️⃣ Ver Reporte en el Navegador

```bash
cd htmlcov
python -m http.server 8000
```

Luego abre: `http://localhost:8000`

---

## 📋 Setup Inicial (Solo Primera Vez)

```bash
# Clonar y entrar al proyecto
cd data_structure_deeper

# Crear entorno virtual
python -m venv .venv

# Activar entorno (Linux/Mac)
source .venv/bin/activate

# O en Windows:
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 📊 Estructura del Proyecto

```
data_structure_deeper/
├── linkendlist/              # Implementaciones
│   ├── node.py
│   ├── node2.py
│   ├── singlylinkedlist.py
│   ├── doublylinkedlist.py
│   └── README.md            # Documentación detallada
├── tests/                   # Suite de tests
│   ├── test_singly_linked_list.py
│   └── test_doubly_linked_list.py
├── htmlcov/                 # Reportes de cobertura
│   ├── README.md           # Instrucciones servidor
│   └── index.html          # Reporte interactivo
└── main.py                 # Entry point
```

---

## ✅ Checklist para Mañana

- [ ] Obtén el proyecto
- [ ] Activa `.venv`
- [ ] Ejecuta: `pytest tests/ -v`
- [ ] Genera cobertura: `pytest tests/ --cov=linkendlist --cov-report=html`
- [ ] Inicia servidor: `cd htmlcov && python -m http.server 8000`
- [ ] Abre: `http://localhost:8000`

---

**¡Listo para aprender estructuras de datos!** 🚀
