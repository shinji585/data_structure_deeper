# Listas Enlazadas - Documentación

Esta carpeta contiene dos implementaciones de listas enlazadas: **Singly Linked List** (Lista Enlazada Simple) y **Doubly Linked List** (Lista Doblemente Enlazada).

---

## 📋 Tabla de Contenidos

1. [Conceptos Básicos](#conceptos-básicos)
2. [Estructura de Nodos](#estructura-de-nodos)
3. [Lista Enlazada Simple](#lista-enlazada-simple)
4. [Lista Doblemente Enlazada](#lista-doblemente-enlazada)
5. [Comparación](#comparación)
6. [Complejidad de Tiempo](#complejidad-de-tiempo)

---

## 🔍 Conceptos Básicos

### ¿Qué es una Lista Enlazada?

Una lista enlazada es una estructura de datos donde los elementos (llamados **nodos**) se conectan entre sí mediante referencias o punteros. A diferencia de un array, los nodos no ocupan memoria contigua.

**Ventajas:**
- Inserción y eliminación O(1) si tienes el nodo
- Tamaño dinámico
- Sin desperdicio de memoria

**Desventajas:**
- Acceso aleatorio O(n)
- Requiere más memoria (referencias adicionales)

---

## 🧩 Estructura de Nodos

### Node (node.py) - Para Lista Simple

```python
class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data           # Valor almacenado
        self.next: Optional[Node[T]] = None  # Referencia al siguiente nodo
```

**Componentes:**
- `data`: Almacena el valor del nodo
- `next`: Puntero al siguiente nodo (None si es el último)

---

### Node (node2.py) - Para Lista Doblemente Enlazada

```python
class Node(Generic[T]):
    def __init__(
        self, 
        data: Optional[T] = None, 
        prev: Optional[Node] = None, 
        next: Optional[Node] = None
    ) -> None:
        self.prev: Optional[Node] = prev      # Referencia al nodo anterior
        self.next: Optional[Node] = next      # Referencia al siguiente nodo
        self.data = data                      # Valor almacenado
```

**Componentes:**
- `data`: Almacena el valor del nodo
- `prev`: Puntero al nodo anterior (None si es el primero)
- `next`: Puntero al siguiente nodo (None si es el último)

---

## 📌 Lista Enlazada Simple

### Descripción

Una lista enlazada simple donde cada nodo solo conoce al siguiente nodo. Solo puedes traversar en una dirección (adelante).

### Estructura Interna

```
head → [data₁|next]→ [data₂|next]→ [data₃|next]→ None ← tail
```

- `__head`: Apunta al primer nodo
- `__tail`: Apunta al último nodo
- `__size`: Contador de elementos

### Métodos Principales

#### 1. `insert_at_beginning(data: T)`

Inserta un elemento al inicio de la lista.

**Casos:**
- **Lista vacía**: head y tail apuntan al nuevo nodo
- **Lista no vacía**: Nuevo nodo apunta a head, luego head apunta al nuevo

```python
sll = SinglyLinkedList()
sll.insert_at_beginning(10)  # [10]
sll.insert_at_beginning(5)   # [5] → [10]
```

**Complejidad:** O(1)

---

#### 2. `insert_at_end(data: T)`

Inserta un elemento al final de la lista.

**Casos:**
- **Lista vacía**: head y tail apuntan al nuevo nodo
- **Lista no vacía**: tail.next apunta al nuevo, luego tail apunta al nuevo

```python
sll = SinglyLinkedList()
sll.insert_at_end(5)   # [5]
sll.insert_at_end(10)  # [5] → [10]
sll.insert_at_end(15)  # [5] → [10] → [15]
```

**Complejidad:** O(1)

---

#### 3. `insert_before(data: T, reference: T)`

Inserta un elemento ANTES de un nodo de referencia.

**Lógica:**
1. Si la lista está vacía, retorna
2. Si el reference es head, usa `insert_at_beginning()`
3. Si no, traversa hasta encontrar el nodo con valor `reference`
4. Inserta el nuevo nodo entre el anterior y el reference

```python
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(3)
sll.insert_before(2, 3)  # [1] → [2] → [3]
```

**Complejidad:** O(n)

---

#### 4. `insert_after(data: T, reference: T)`

Inserta un elemento DESPUÉS de un nodo de referencia.

**Lógica:**
1. Traversa hasta encontrar el nodo con valor `reference`
2. Inserta el nuevo nodo entre reference y su siguiente
3. Si reference es tail, actualiza tail

```python
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(3)
sll.insert_after(2, 1)  # [1] → [2] → [3]
```

**Complejidad:** O(n)

---

#### 5. `remove_at_beginning()`

Elimina el primer elemento.

**Casos:**
- **Lista vacía**: No hace nada
- **Un elemento**: head y tail se vuelven None
- **Múltiples**: head apunta al siguiente

```python
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.remove_at_beginning()  # [2] → [3]
```

**Complejidad:** O(1)

---

#### 6. `remove_at_end()`

Elimina el último elemento.

**Casos:**
- **Lista vacía**: No hace nada
- **Un elemento**: head y tail se vuelven None
- **Múltiples**: Traversa para encontrar el penúltimo, actualiza tail

```python
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.remove_at_end()  # [1] → [2]
```

**Complejidad:** O(n)

---

#### 7. `remove(reference: T)`

Elimina el primer nodo que coincida con el valor `reference`.

**Lógica:**
1. Si es head, usa `remove_at_beginning()`
2. Traversa para encontrar el nodo
3. Si es tail, actualiza tail
4. Desconecta el nodo

```python
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.remove(2)  # [1] → [3]
```

**Complejidad:** O(n)

---

## 🔄 Lista Doblemente Enlazada

### Descripción

Una lista enlazada donde cada nodo conoce tanto al nodo anterior como al siguiente. Puedes traversar en ambas direcciones (adelante y atrás).

### Estructura Interna

```
head ← → [prev|data|next] ↔ [prev|data|next] ↔ [prev|data|next] ← tail
```

- `__head`: Apunta al primer nodo
- `__tail`: Apunta al último nodo
- `__size`: Contador de elementos

### Métodos Principales

#### 1. `insert_at_beginning(data: T)`

Inserta un elemento al inicio.

**Casos:**
- **Lista vacía**: head y tail apuntan al nuevo, prev=None, next=None
- **Lista no vacía**: 
  - Nuevo.next = head
  - head.prev = nuevo
  - head = nuevo

```python
dll = DoublyLinkedList()
dll.insert_at_beginning(10)  # ←[10]→
dll.insert_at_beginning(5)   # ←[5]↔[10]→
```

**Complejidad:** O(1)

---

#### 2. `insert_at_end(data: T)`

Inserta un elemento al final.

**Casos:**
- **Lista vacía**: head y tail apuntan al nuevo
- **Lista no vacía**:
  - Nuevo.prev = tail
  - tail.next = nuevo
  - tail = nuevo

```python
dll = DoublyLinkedList()
dll.insert_at_end(5)   # ←[5]→
dll.insert_at_end(10)  # ←[5]↔[10]→
```

**Complejidad:** O(1)

---

#### 3. `insert_before(data: T, reference: T)`

Inserta ANTES del nodo de referencia, manteniendo referencias bidireccionales.

```python
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(3)
dll.insert_before(2, 3)  # ←[1]↔[2]↔[3]→
```

**Complejidad:** O(n)

---

#### 4. `insert_after(data: T, reference: T)`

Inserta DESPUÉS del nodo de referencia, manteniendo referencias bidireccionales.

```python
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(3)
dll.insert_after(2, 1)  # ←[1]↔[2]↔[3]→
```

**Complejidad:** O(n)

---

#### 5. `remove_at_beginning()`

Elimina el primer elemento.

**Casos:**
- **Lista vacía**: No hace nada
- **Un elemento**: head y tail = None
- **Múltiples**: head = head.next, head.prev = None

```python
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.remove_at_beginning()  # ←[2]↔[3]→
```

**Complejidad:** O(1)

---

#### 6. `remove_at_end()`

Elimina el último elemento.

**Casos:**
- **Lista vacía**: No hace nada
- **Un elemento**: head y tail = None
- **Múltiples**: tail = tail.prev, tail.next = None

```python
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.remove_at_end()  # ←[1]↔[2]→
```

**Complejidad:** O(1)

---

#### 7. `remove(reference: T)`

Elimina el nodo con valor `reference`, manteniendo integridad bidireccional.

```python
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.remove(2)  # ←[1]↔[3]→
```

**Complejidad:** O(n)

---

## ⚖️ Comparación

| Operación | Simple | Doblemente |
|-----------|--------|-----------|
| Insertar al inicio | O(1) | O(1) |
| Insertar al final | O(1) | O(1) |
| Insertar en medio | O(n) | O(n) |
| Eliminar inicio | O(1) | O(1) |
| Eliminar final | O(n) | O(1) * |
| Eliminar en medio | O(n) | O(n) |
| Traversal adelante | O(1) por nodo | O(1) por nodo |
| Traversal atrás | ❌ No posible | O(1) por nodo |
| Memoria por nodo | 1 referencia | 2 referencias |

*Si tienes el nodo, en doblemente es O(1)

---

## ⏱️ Complejidad de Tiempo

### Singly Linked List

- **Access**: O(n)
- **Search**: O(n)
- **Insertion**: O(1) si tienes el nodo, O(n) si necesitas buscar
- **Deletion**: O(1) si tienes el nodo, O(n) si necesitas buscar

### Doubly Linked List

- **Access**: O(n)
- **Search**: O(n)
- **Insertion**: O(1) si tienes el nodo, O(n) si necesitas buscar
- **Deletion**: O(1) si tienes el nodo o es final, O(n) si necesitas buscar

---

## 📝 Notas Implementación

Ambas listas utilizan **type hints** con `Generic[T]` para ser type-safe y trabajar con cualquier tipo de dato:

```python
sll: SinglyLinkedList[int] = SinglyLinkedList()
sll.insert_at_end(5)
sll.insert_at_end(10)

dll: DoublyLinkedList[str] = DoublyLinkedList()
dll.insert_at_end("hola")
dll.insert_at_end("mundo")
```

Los métodos privados `__increase__()` y `__decrease__()` mantienen el contador de tamaño sincronizado con las operaciones.

---

## 🧪 Testing

Para ejecutar los tests de ambas implementaciones:

```bash
pytest main.py -v
```

Los tests cubren:
- Inserciones en diferentes posiciones
- Eliminaciones en diferentes posiciones
- Casos límite (lista vacía, un elemento)
- Mantenimiento de referencias
- Integridad del tamaño

---
