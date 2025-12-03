import { useState } from 'react'
import type { Task, TaskCreate } from '../types'
import { useTaskStore } from '../store/tasks'

type Props = {
  task: Task
  depth?: number
}

export default function TaskTree({ task, depth = 0 }: Props) {
  const [expanded, setExpanded] = useState(true)
  const addTask = useTaskStore(s => s.addTask)
  const removeTask = useTaskStore(s => s.removeTask)

  const handleAddSubtask = async () => {
    const title = prompt('Subtask title:')
    if (!title) return
    const payload: TaskCreate = { title, parent_id: task.id }
    await addTask(payload)
    // Note: caller page should refresh task tree after creation
    alert('Subtask created. Refresh to see updates.')
  }

  const handleDelete = async () => {
    if (confirm('Delete this task and all its subtasks?')) {
      await removeTask(task.id)
      alert('Task deleted. Refresh to see updates.')
    }
  }

  const hasChildren = !!task.subtasks && task.subtasks.length > 0

  return (
    <div style={{ marginLeft: depth * 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
        {hasChildren && (
          <button onClick={() => setExpanded(e => !e)} aria-label="toggle">
            {expanded ? '▾' : '▸'}
          </button>
        )}
        <span style={{ fontWeight: 600 }}>{task.title}</span>
        {task.description && <span style={{ color: '#666' }}>— {task.description}</span>}
        <button onClick={handleAddSubtask}>+ Subtask</button>
        <button onClick={handleDelete} style={{ color: 'crimson' }}>Delete</button>
      </div>
      {expanded && hasChildren && (
        <div style={{ marginTop: 4 }}>
          {task.subtasks!.map(st => (
            <TaskTree key={st.id} task={st} depth={depth + 1} />
          ))}
        </div>
      )}
    </div>
  )}
