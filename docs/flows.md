# Diagrama de Flujo Básico (Sub-tareas)

1. Usuario crea una tarea raíz (`parent_id = null`).
2. Usuario crea sub-tarea referenciando `parent_id = <id tarea padre>`.
3. Para mostrar jerarquía, el frontend llama `GET /tasks/{id}/with-subtasks`.
4. El backend carga recursivamente sub-tareas y retorna un árbol.
5. El componente `TaskTree` renderiza el árbol con recursión en el cliente.

```text
Task(1)
├─ Task(2)
│  ├─ Task(4)
│  └─ Task(5)
└─ Task(3)
```
