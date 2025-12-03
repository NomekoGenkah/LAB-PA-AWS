import './App.css'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import TaskList from './pages/TaskList'
import TaskDetail from './pages/TaskDetail'

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: '1rem', maxWidth: 960, margin: '0 auto' }}>
        <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1>Hierarchical To-Do App</h1>
          <nav style={{ display: 'flex', gap: '1rem' }}>
            <Link to="/">Home</Link>
            <Link to="/tasks">Task List</Link>
          </nav>
        </header>
        <main style={{ marginTop: '1rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/tasks" element={<TaskList />} />
            <Route path="/tasks/:id" element={<TaskDetail />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
