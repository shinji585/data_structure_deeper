# Árbol Binario de Búsqueda (Binary Search Tree)

Este proyecto implementa un **Árbol Binario de Búsqueda (BST)** en Python usando genéricos y tipado estático. Está compuesto por tres archivos principales.

---

## Estructura del proyecto

```
tree/
├── __init__.py
├── tree_node.py
└── binary_tree_search.py
```

---

## Archivos

### 1. `tree/__init__.py`

Archivo vacío que convierte el directorio `tree/` en un paquete de Python. Permite importar los módulos del árbol con rutas como `from tree.tree_node import Node`.

---

### 2. `tree/tree_node.py`

Define el bloque fundamental de la estructura: el **nodo**.

```python
class Node[T]:
    def __init__(self, data: T):
        self.data: T = data
        self.left_child: Optional[Node[T]] = None
        self.right_child: Optional[Node[T]] = None
```

**Detalles de implementación:**

- Usa **genéricos** (`Node[T]`) para que el nodo pueda almacenar cualquier tipo de dato comparable.
- Cada nodo guarda un valor (`data`) y dos referencias opcionales: `left_child` (hijo izquierdo) y `right_child` (hijo derecho), ambos inicializados en `None`.
- Usa `from __future__ import annotations` para permitir anotaciones de tipo forward (referenciar `Node[T]` dentro de la misma clase).

---

### 3. `tree/binary_tree_search.py`

Contiene la clase principal `BinaryTreeSearch[T]`, que implementa todas las operaciones del árbol. También define el protocolo `Comparable` para garantizar que los tipos usados soporten comparaciones.

#### Protocolo `Comparable`

```python
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
```

Garantiza en tiempo de análisis estático que el tipo `T` soporte los operadores `<` y `>`, necesarios para navegar el árbol.

---

#### Clase `BinaryTreeSearch[T]`

El árbol se inicializa con `root = None` (árbol vacío).

---

##### `insert(data: T) -> None`
Inserta un nuevo nodo en la posición correcta del árbol:
- Si el árbol está vacío, el nodo se convierte en la raíz.
- De lo contrario, recorre el árbol comparando valores: si el dato es menor, va a la izquierda; si es mayor o igual, va a la derecha.
- Se detiene cuando encuentra un espacio vacío (`None`) y coloca allí el nuevo nodo.
- Usa `while current is not None:` como condición explícita del loop, lo que hace el flujo más seguro y legible. `current` se declara como `Optional[Node[T]]` para reflejar correctamente que puede ser `None` durante el recorrido.

---

##### `search(data: T) -> bool`
Busca un valor en el árbol:
- Recorre el árbol desde la raíz comparando el valor buscado con el nodo actual.
- Si lo encuentra, retorna `True`; si llega a un `None`, retorna `False`.

---

##### `find_min() -> Node[T]`
Retorna el nodo con el valor mínimo:
- Navega siempre hacia la izquierda hasta llegar al nodo más a la izquierda del árbol.

##### `find_max() -> Node[T]`
Retorna el nodo con el valor máximo:
- Navega siempre hacia la derecha hasta llegar al nodo más a la derecha.

---

##### `remove(data: T) -> bool`
Elimina un nodo del árbol manejando tres casos:

| Caso | Descripción |
|------|-------------|
| **0 hijos** (hoja) | Se elimina directamente desconectándolo del padre. |
| **1 hijo** | El hijo del nodo eliminado toma su lugar. |
| **2 hijos** | Se busca el nodo más a la izquierda del subárbol derecho (*sucesor en orden*), se copia su valor al nodo a eliminar, y se elimina ese sucesor. |

---

##### Recorridos del árbol

Estos métodos recorren el árbol de distintas formas usando **generadores recursivos** (`yield` / `yield from`):

| Método | Orden de visita | Uso típico |
|--------|----------------|------------|
| `preorder()` | Raíz → Izquierda → Derecha | Copiar o serializar el árbol |
| `inorder()` | Izquierda → Raíz → Derecha | Obtener valores en orden ascendente |
| `postorder()` | Izquierda → Derecha → Raíz | Eliminar o liberar el árbol |

---

##### `__get_parent_and_node__(data: T) -> tuple`
Método auxiliar privado que retorna una tupla `(padre, nodo)` dado un valor. Es usado internamente por `remove()` para localizar el nodo y su padre antes de eliminarlo.

---

## Propiedades del BST

- **Búsqueda, inserción y eliminación:** O(log n) en promedio, O(n) en el peor caso (árbol degenerado).
- **Recorrido inorder:** produce los valores en orden ascendente.
- **Tipado genérico:** compatible con cualquier tipo que implemente `<` y `>`.