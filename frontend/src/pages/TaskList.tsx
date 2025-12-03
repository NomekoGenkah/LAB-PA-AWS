import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useTaskStore } from '../store/tasks'
import TaskTree from '../components/TaskTree'

export default function TaskList() {
  const { tasks, loading, error, loadRootTasks, addTask } = useTaskStore()

  useEffect(() => {
    loadRootTasks()
  }, [loadRootTasks])

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <h2>Task List</h2>
        <button
          onClick={async () => {
            const title = prompt('Task title:')
            if (!title) return
            await addTask({ title })
            await loadRootTasks()
          }}
        >
          + New Task
        </button>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'crimson' }}>{error}</p>}
      {!loading && tasks.length === 0 && <p>No tasks yet. Create one!</p>}
      <div>
        {tasks.map(t => (
          <div key={t.id} style={{ marginBottom: 8 }}>
            <Link to={`/tasks/${t.id}`}>Open detail</Link>
            <TaskTree task={t} />
          </div>
        ))}
      </div>
    </div>
  )
}
