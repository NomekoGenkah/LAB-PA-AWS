import { useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useTaskStore } from '../store/tasks'
import TaskTree from '../components/TaskTree'

export default function TaskDetail() {
  const { id } = useParams()
  const taskId = Number(id)
  const { selectedTask, loading, error, loadTaskWithSubtasks } = useTaskStore()

  useEffect(() => {
    if (!Number.isNaN(taskId)) {
      loadTaskWithSubtasks(taskId)
    }
  }, [taskId, loadTaskWithSubtasks])

  if (Number.isNaN(taskId)) return <p>Invalid task id</p>

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <h2>Task Detail</h2>
        <Link to="/tasks">Back to list</Link>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'crimson' }}>{error}</p>}
      {!loading && selectedTask && (
        <TaskTree task={selectedTask} />
      )}
    </div>
  )
}
