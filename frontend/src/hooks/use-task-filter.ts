// frontend/src/hooks/use-task-filter.ts
import { useState, useMemo } from 'react';

export type TaskStatus = 'all' | 'pending' | 'completed';

export interface Task {
  id: string;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

const useTaskFilter = (tasks: Task[]) => {
  const [statusFilter, setStatusFilter] = useState<TaskStatus>('all');

  const filteredTasks = useMemo(() => {
    switch (statusFilter) {
      case 'completed':
        return tasks.filter(task => task.completed);
      case 'pending':
        return tasks.filter(task => !task.completed);
      default:
        return tasks;
    }
  }, [tasks, statusFilter]);

  const filterCounts = useMemo(() => {
    const all = tasks.length;
    const completed = tasks.filter(task => task.completed).length;
    const pending = all - completed;

    return { all, completed, pending };
  }, [tasks]);

  return {
    filteredTasks,
    statusFilter,
    setStatusFilter,
    filterCounts
  };
};

export default useTaskFilter;