import { api } from './client'
import type { Task, TaskCreate, TaskUpdate } from '../types'

export async function getHealth(): Promise<{ status: string; service: string }> {
  const { data } = await api.get('/health')
  return data
}

export async function listTasks(rootOnly = false, skip = 0, limit = 100): Promise<Task[]> {
  const { data } = await api.get('/tasks', { params: { root_only: rootOnly, skip, limit } })
  return data
}

export async function getTask(id: number): Promise<Task> {
  const { data } = await api.get(`/tasks/${id}`)
  return data
}

export async function getTaskWithSubtasks(id: number): Promise<Task> {
  const { data } = await api.get(`/tasks/${id}/with-subtasks`)
  return data
}

export async function createTask(payload: TaskCreate): Promise<Task> {
  const { data } = await api.post('/tasks', payload)
  return data
}

export async function updateTask(id: number, payload: TaskUpdate): Promise<Task> {
  const { data } = await api.put(`/tasks/${id}`, payload)
  return data
}

export async function deleteTask(id: number): Promise<void> {
  await api.delete(`/tasks/${id}`)
}
