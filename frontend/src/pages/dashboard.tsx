// frontend/src/pages/dashboard.tsx
import React, { useState, useEffect } from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router';
import { useAuth } from '../context/auth-context';
import { authenticatedRequest, createTask, updateTask, toggleTaskCompletion, deleteTask } from '../lib/auth-utils';
import Button from '../components/ui/button';
import TaskFormModal from '../components/task-form-modal';

interface Task {
  id: string;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

const DashboardPage: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const router = useRouter();
  const { isAuthenticated, logout } = useAuth();

  useEffect(() => {
    // Check if user is authenticated
    if (!isAuthenticated) {
      router.push('/login');
      return;
    }

    // Fetch tasks from API
    const fetchTasks = async () => {
      try {
        const response = await authenticatedRequest('http://localhost:8000/api/tasks');

        if (response.ok) {
          const data = await response.json();
          setTasks(data);
        } else if (response.status === 401) {
          // Token expired, redirect to login
          logout();
          router.push('/login');
        } else {
          console.error('Failed to fetch tasks');
        }
      } catch (error) {
        console.error('Error fetching tasks:', error);
        if (error instanceof Error && error.message.includes('Network error')) {
          // Handle network error specifically
          alert('Network error: Unable to connect to the server. Please ensure the backend is running.');
        }
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [router, isAuthenticated, logout, showModal]); // Added showModal to dependency array to refresh tasks after modal closes

  const handleAddTask = () => {
    setEditingTask(null);
    setShowModal(true);
  };

  const handleEditTask = (task: Task) => {
    setEditingTask(task);
    setShowModal(true);
  };

  const handleTaskSubmit = async (taskData: { title: string; description: string; completed: boolean }) => {
    try {
      if (editingTask) {
        // Update existing task
        const updatedTask = await updateTask(editingTask.id, taskData);
        setTasks(tasks.map(t => t.id === updatedTask.id ? updatedTask : t));
        setShowModal(false);
      } else {
        // Create new task
        const newTask = await createTask(taskData);
        setTasks([...tasks, newTask]);
        setShowModal(false);
      }
    } catch (error) {
      console.error('Error submitting task:', error);
      if (error instanceof Error && error.message.includes('Authentication token expired')) {
        // Token expired, redirect to login
        logout();
        router.push('/login');
      } else {
        alert('Error submitting task');
      }
    }
  };

  const handleToggleTask = async (taskId: string) => {
    try {
      const result = await toggleTaskCompletion(taskId);
      setTasks(tasks.map(task =>
        task.id === taskId ? { ...task, completed: result.completed } : task
      ));
    } catch (error) {
      console.error('Error toggling task:', error);
      if (error instanceof Error && error.message.includes('Authentication token expired')) {
        // Token expired, redirect to login
        logout();
        router.push('/login');
      } else if (error instanceof Error && error.message.includes('Network error')) {
        // Handle network error specifically for toggle - don't show alert to avoid disrupting UX
        console.warn('Network error during task toggle, keeping UI state as is');
      } else {
        alert('Error toggling task');
      }
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await deleteTask(taskId);
        setTasks(tasks.filter(task => task.id !== taskId));
      } catch (error) {
        console.error('Error deleting task:', error);
        if (error instanceof Error && error.message.includes('Authentication token expired')) {
          // Token expired, redirect to login
          logout();
          router.push('/login');
        } else {
          alert('Error deleting task');
        }
      }
    }
  };

  const handleLogout = () => {
    logout();
    router.push('/');
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Head>
        <title>Todo Dashboard | Full-Stack Todo App</title>
        <meta name="description" content="Manage your tasks with our AI-powered todo app" />
      </Head>

      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">Todo Dashboard</h1>
          <div className="flex items-center space-x-4">
            <span className="text-gray-600">Welcome back!</span>
            <Button onClick={handleLogout} variant="outline">Logout</Button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-xl font-semibold text-gray-800">Your Tasks</h2>
          <Button onClick={handleAddTask}>Add New Task</Button>
        </div>

        {tasks.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500">You have no tasks yet. Add one to get started!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {tasks.map((task) => (
              <div
                key={task.id}
                className={`bg-white rounded-lg shadow-md p-6 border-l-4 ${
                  task.completed ? 'border-green-500' : 'border-yellow-500'
                }`}
              >
                <div className="flex justify-between items-start">
                  <h3 className={`text-lg font-medium ${
                    task.completed ? 'line-through text-gray-500' : 'text-gray-900'
                  }`}>
                    {task.title}
                  </h3>
                  <span className={`px-2 py-1 text-xs rounded-full ${
                    task.completed
                      ? 'bg-green-100 text-green-800'
                      : 'bg-yellow-100 text-yellow-800'
                  }`}>
                    {task.completed ? 'Completed' : 'Pending'}
                  </span>
                </div>
                <p className="mt-2 text-gray-600">{task.description}</p>
                <div className="mt-4 flex justify-between items-center">
                  <span className="text-xs text-gray-500">
                    Created: {new Date(task.created_at).toLocaleDateString()}
                  </span>
                  <div className="flex space-x-2">
                    <Button
                      variant="outline"
                      className="text-sm"
                      onClick={() => handleEditTask(task)}
                    >
                      Edit
                    </Button>
                    <Button
                      variant={task.completed ? "outline" : "primary"}
                      className="text-sm"
                      onClick={() => handleToggleTask(task.id)}
                    >
                      {task.completed ? 'Mark Incomplete' : 'Mark Complete'}
                    </Button>
                    <Button
                      variant="outline"
                      className="text-sm text-red-600 hover:text-red-800"
                      onClick={() => handleDeleteTask(task.id)}
                    >
                      Delete
                    </Button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Task Form Modal */}
        <TaskFormModal
          isOpen={showModal}
          onClose={() => setShowModal(false)}
          onSubmit={handleTaskSubmit}
          initialData={editingTask || undefined}
        />
      </main>
    </div>
  );
};

export default DashboardPage;