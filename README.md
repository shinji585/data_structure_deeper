# Data Structures Deeper 🚀

Un repositorio educativo para entender y profundizar en las **estructuras de datos fundamentales** y avanzadas. Este proyecto implementa estructuras de datos desde cero con explicaciones detalladas, tests comprensivos y documentación clara.

---

## 📚 Objetivo del Proyecto

Este repositorio tiene como objetivo:

1. **Comprender** cómo funcionan las estructuras de datos internamente
2. **Implementar** estructuras de datos desde cero sin librerías externas
3. **Documentar** cada implementación con ejemplos y diagramas
4. **Probar** cada estructura con tests exhaustivos
5. **Comparar** rendimiento y características de diferentes estructuras
6. **Evolucionar** desde estructuras simples hasta complejas

---

## 📂 Estructura del Proyecto

```
data_structure_deeper/
├── tests/                         # Test suite organized by structure
│   ├── __init__.py
│   ├── test_singly_linked_list.py         # Tests for SinglyLinkedList
│   └── test_doubly_linked_list.py         # Tests for DoublyLinkedList
│
├── linkendlist/                    # Listas Enlazadas
│   ├── node.py                    # Nodo para lista simple
│   ├── node2.py                   # Nodo para lista doblemente enlazada
│   ├── singlylinkedlist.py        # Implementación de lista simple
│   ├── doublylinkedlist.py        # Implementación de lista doblemente enlazada
│   └── README.md                  # Documentación detallada
│
├── main.py                        # Main entry point
├── requirements.txt               # Dependencias del proyecto
├── pyproject.toml                 # Configuración del proyecto
├── README.md                      # Este archivo
└── understanding_datastructure.txt# Notas de aprendizaje
```

---

## 🗺️ Roadmap - Estructuras Planeadas

1. **Listas Enlazadas** ✅ (Completado - Todas las operaciones implementadas)
   - Lista Enlazada Simple (Singly Linked List) ✅
     - ✅ Insertar al inicio/final
     - ✅ Insertar antes/después de referencia
     - ✅ Eliminar al inicio/final
     - ✅ Eliminar antes/después de referencia
     - ✅ Eliminar por valor
     - ✅ Búsqueda secuencial (search/find)
     - ✅ Iteración forward
   - Lista Doblemente Enlazada (Doubly Linked List) ✅
     - ✅ Todas las operaciones anteriores
     - ✅ Iteración backward (iterate_backward)
     - ✅ Eliminación final O(1)
   - Lista Circular 🔄 (Pendiente)

2. **Pilas y Colas** 🔄 (Próximo)
   - Stack (Pila)
   - Queue (Cola)
   - Deque (Cola Doble)
   - Priority Queue

3. **Árboles** 🌳 (Planeado)
   - Árbol Binario (Binary Tree)
   - Árbol de Búsqueda Binaria (Binary Search Tree)
   - Árbol AVL
   - Árbol Rojo-Negro
   - Árbol B
   - Heap

4. **Grafos** 🔗 (Planeado)
   - Grafo No Dirigido
   - Grafo Dirigido
   - Representación por Lista de Adyacencia
   - Representación por Matriz de Adyacencia
   - BFS (Breadth-First Search)
   - DFS (Depth-First Search)
   - Dijkstra
   - Floyd-Warshall

5. **Tablas Hash** 🔐 (Planeado)
   - Hash Table
   - Resolución de Colisiones (Chaining, Open Addressing)

6. **Estructuras Avanzadas** 🎯 (Planeado)
   - Trie
   - Segment Tree
   - Fenwick Tree
   - Union-Find

---

## 🚀 Inicio Rápido

### Requisitos

- Python 3.9+
- pytest

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/shinji585/data_structure_deeper.git
cd data_structure_deeper

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar tests de una estructura específica
pytest tests/test_singly_linked_list.py -v
pytest tests/test_doubly_linked_list.py -v

# Ejecutar con cobertura
pytest tests/ --cov=linkendlist
```

---

## 📖 Documentación de Estructuras

### 🔗 Listas Enlazadas

Ver la [documentación completa de Listas Enlazadas](linkendlist/README.md)

**Incluye:**
- Explicación de conceptos
- Estructura de nodos
- Métodos detallados paso a paso
- Complejidad de tiempo
- Ejemplos de uso
- Comparación entre implementaciones

**Estructuras incluidas:**
- `SinglyLinkedList`: Lista enlazada simple
- `DoublyLinkedList`: Lista doblemente enlazada

---

## 🧪 Tests

El proyecto utiliza **pytest** para testing comprehensivo. Los tests están organizados en la carpeta `tests/`:

```
tests/
├── test_singly_linked_list.py      # 21 tests para SinglyLinkedList
└── test_doubly_linked_list.py      # 27 tests para DoublyLinkedList
```

**Cada archivo de test incluye:**
- Inserciones en diferentes posiciones
- Eliminaciones en diferentes posiciones
- Casos límite (lista vacía, un elemento)
- Mantenimiento de referencias
- Integridad del tamaño

### CI/CD con GitHub Actions

Este proyecto utiliza **GitHub Actions** para ejecutar tests automáticamente:

- **Trigger**: Cada push a `main` o `develop`, y en Pull Requests
- **Matriz de versiones Python**: 3.9, 3.10, 3.11, 3.12
- **Tests**: Se ejecutan desde la carpeta `tests/`
- **Reporte**: Se genera un reporte HTML de los tests

Ver configuración en [.github/workflows/test.yml](.github/workflows/test.yml)

---

## 💡 Concepto de Aprendizaje

Cada estructura de datos se implementa siguiendo este patrón:

1. **Teoría**: Explicar qué es y cómo funciona
2. **Estructura**: Mostrar la estructura interna
3. **Métodos**: Implementar operaciones comunes
4. **Análisis**: Explicar complejidad de tiempo/espacio
5. **Tests**: Validar todas las funcionalidades
6. **Documentación**: Proporcionar ejemplos claros

---

## 📊 Complejidad de Operaciones

### Listas Enlazadas

| Estructura | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Singly Linked List | O(n) | O(n) | O(1)* | O(n)* |
| Doubly Linked List | O(n) | O(n) | O(1)* | O(1)* |

*Si tienes la referencia al nodo

---

## 🎯 Uso Práctico

### Crear una Lista Enlazada Simple

```python
from linkendlist.singlylinkedlist import SinglyLinkedList

# Crear lista
sll = SinglyLinkedList[int]()

# Insertar elementos
sll.insert_at_beginning(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_before(15, 20)

# Eliminar elementos
sll.remove(15)
sll.remove_at_beginning()
```

### Ejecutar Tests Específicos

```python
# Importar y ejecutar
from tests.test_singly_linked_list import TestSinglyLinkedList
from tests.test_doubly_linked_list import TestDoublyLinkedList

# O simplemente
pytest tests/test_singly_linked_list.py -v
pytest tests/test_doubly_linked_list.py -v
```

---

## 🔧 Tecnologías Utilizadas

- **Lenguaje**: Python 3.9+
- **Testing**: pytest
- **Type Hints**: Generic[T] para type-safety
- **CI/CD**: GitHub Actions
- **Versionado**: Git

---

## 📝 Notas de Aprendizaje

Ver [understanding_datastructure.txt](understanding_datastructure.txt) para notas detalladas sobre el aprendizaje de estructuras de datos.

---

## 🤝 Contribuciones

Este es un proyecto educativo personal. Las mejoras, correcciones y nuevas estructuras son bienvenidas.

---

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.

---

## 📞 Contacto

Para preguntas o sugerencias sobre las implementaciones, puedes:
- Abrir un Issue
- Crear un Pull Request
- Contactar al autor

---

## ✨ Características Destacadas

- ✅ Implementaciones desde cero sin librerías externas
- ✅ Type hints completos para mejor experiencia de IDE
- ✅ Tests exhaustivos con cobertura
- ✅ Documentación clara y detallada
- ✅ Exemplos de uso práctico
- ✅ Análisis de complejidad para cada operación
- ✅ CI/CD automático con GitHub Actions
- ✅ Estructura escalable para agregar nuevas estructuras

---

**Última actualización**: Abril 2026

Mantente aprendiendo 🎓
