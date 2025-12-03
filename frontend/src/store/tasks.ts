import { create } from 'zustand'
import type { Task, TaskCreate, TaskUpdate } from '../types'
import { listTasks, getTaskWithSubtasks, createTask, updateTask, deleteTask } from '../api/tasks'

interface TaskState {
  tasks: Task[]
  selectedTask?: Task
  loading: boolean
  error?: string
  loadRootTasks: () => Promise<void>
  loadTaskWithSubtasks: (id: number) => Promise<void>
  addTask: (payload: TaskCreate) => Promise<Task>
  editTask: (id: number, payload: TaskUpdate) => Promise<Task>
  removeTask: (id: number) => Promise<void>
}

export const useTaskStore = create<TaskState>((set, get) => ({
  tasks: [],
  selectedTask: undefined,
  loading: false,
  error: undefined,
  async loadRootTasks() {
    set({ loading: true, error: undefined })
    try {
      const tasks = await listTasks(true)
      set({ tasks })
    } catch (e: any) {
      set({ error: e?.message || 'Failed to load tasks' })
    } finally {
      set({ loading: false })
    }
  },
  async loadTaskWithSubtasks(id: number) {
    set({ loading: true, error: undefined })
    try {
      const task = await getTaskWithSubtasks(id)
      set({ selectedTask: task })
    } catch (e: any) {
      set({ error: e?.message || 'Failed to load task' })
    } finally {
      set({ loading: false })
    }
  },
  async addTask(payload: TaskCreate) {
    const task = await createTask(payload)
    // If creating root task, update list
    if (!payload.parent_id) {
      set({ tasks: [task, ...get().tasks] })
    }
    return task
  },
  async editTask(id: number, payload: TaskUpdate) {
    const task = await updateTask(id, payload)
    // Update in-memory lists if relevant
    set({
      tasks: get().tasks.map(t => (t.id === id ? { ...t, ...task } : t)),
      selectedTask: get().selectedTask && get().selectedTask!.id === id ? { ...get().selectedTask!, ...task } : get().selectedTask,
    })
    return task
  },
  async removeTask(id: number) {
    await deleteTask(id)
    set({
      tasks: get().tasks.filter(t => t.id !== id),
      selectedTask: get().selectedTask && get().selectedTask!.id === id ? undefined : get().selectedTask,
    })
  },
}))
