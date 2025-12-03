export interface Task {
  id: number
  title: string
  description?: string | null
  parent_id?: number | null
  created_at: string
  updated_at: string
  subtasks?: Task[]
}

export interface TaskCreate {
  title: string
  description?: string | null
  parent_id?: number | null
}

export interface TaskUpdate {
  title?: string
  description?: string | null
  parent_id?: number | null
}
