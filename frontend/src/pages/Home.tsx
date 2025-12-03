import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getHealth } from '../api/tasks'

export default function Home() {
  const [health, setHealth] = useState<string>('Checking...')

  useEffect(() => {
    getHealth()
      .then((h) => setHealth(`${h.status} (${h.service})`))
      .catch(() => setHealth('Unavailable'))
  }, [])

  return (
    <div>
      <p>Backend health: {health}</p>
      <p>Empieza por ver tus tareas:</p>
      <ul>
        <li><Link to="/tasks">Task List</Link></li>
      </ul>
    </div>
  )
}
