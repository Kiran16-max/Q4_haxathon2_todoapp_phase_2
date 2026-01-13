// frontend/src/lib/auth-utils.ts
import { User } from './auth';

interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

interface RegisterPayload {
  name: string;
  email: string;
  password: string;
}

interface LoginPayload {
  email: string;
  password: string;
}

/**
 * Registers a new user with the backend
 */
export const registerUser = async (payload: RegisterPayload): Promise<AuthResponse> => {
  try {
    const response = await fetch('http://localhost:8000/api/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `Registration failed: ${response.status} ${response.statusText}`);
    }

    const data: AuthResponse = await response.json();
    return data;
  } catch (error) {
    console.error('Registration error:', error);
    if (error instanceof Error) {
      if (error instanceof TypeError && error.message.includes('fetch')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      throw error;
    }
    throw new Error('Network error during registration');
  }
};

/**
 * Logs in a user with the backend
 */
export const loginUser = async (payload: LoginPayload): Promise<AuthResponse> => {
  try {
    // Convert to form data as expected by backend (OAuth2PasswordRequestForm)
    const formData = new URLSearchParams();
    formData.append('username', payload.email);  // OAuth2 spec uses 'username' field even for email
    formData.append('password', payload.password);

    const response = await fetch('http://localhost:8000/api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `Login failed: ${response.status} ${response.statusText}`);
    }

    const data: AuthResponse = await response.json();
    return data;
  } catch (error) {
    console.error('Login error:', error);
    if (error instanceof Error) {
      if (error instanceof TypeError && error.message.includes('fetch')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      throw error;
    }
    throw new Error('Network error during login');
  }
};

/**
 * Stores the JWT token in localStorage
 */
export const storeToken = (token: string): void => {
  localStorage.setItem('access_token', token);
};

/**
 * Retrieves the JWT token from localStorage
 */
export const getToken = (): string | null => {
  return localStorage.getItem('access_token');
};

/**
 * Removes the JWT token from localStorage
 */
export const removeToken = (): void => {
  localStorage.removeItem('access_token');
};

/**
 * Makes an authenticated API request
 */
export const authenticatedRequest = async (
  url: string,
  options: RequestInit = {}
): Promise<Response> => {
  const token = getToken();

  if (!token) {
    throw new Error('No authentication token available');
  }

  // Ensure the token doesn't already have the "Bearer" prefix to avoid duplication
  const cleanToken = token.startsWith('Bearer ') ? token.substring(7) : token;

  const authenticatedOptions: RequestInit = {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': `Bearer ${cleanToken}`,
      'Content-Type': 'application/json',
    },
  };

  let response;
  try {
    response = await fetch(url, authenticatedOptions);
  } catch (networkError) {
    console.error('Network error during authenticated request:', networkError);
    // Return a mock response with network error status to allow graceful handling by caller
    return new Response(JSON.stringify({ error: 'Network error: Unable to connect to the server. Please check if the backend is running.' }), {
      status: 503,
      statusText: 'Service Unavailable'
    });
  }

  if (response.status === 401) {
    // Token might be expired, remove it
    removeToken();
    // Return the response so the caller can handle the redirect gracefully
    return response;
  }

  return response;
};

/**
 * Creates a new task
 */
export const createTask = async (taskData: { title: string; description: string; completed: boolean }): Promise<any> => {
  try {
    const response = await authenticatedRequest('http://localhost:8000/api/tasks', {
      method: 'POST',
      body: JSON.stringify(taskData),
    });

    if (response.status === 401) {
      // Token expired, the token has already been removed by authenticatedRequest
      // Re-throw to allow caller to handle redirect
      throw new Error('Authentication token expired. Please log in again.');
    }

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail?.message || errorData.detail || `Create task failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();

    // Handle the new response format: { status: "success", task: {...} }
    if (data.status === "success" && data.task) {
      return data.task;
    } else {
      throw new Error(data.message || 'Invalid response format from server');
    }
  } catch (error) {
    console.error('Create task error:', error);
    if (error instanceof Error) {
      if (error.message.includes('Network error')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      if (error.message.includes('Authentication token expired')) {
        // Re-throw authentication errors so callers can handle them
        throw error;
      }
      throw error;
    }
    throw new Error('Network error during task creation');
  }
};

/**
 * Updates an existing task
 */
export const updateTask = async (
  taskId: string,
  taskData: { title?: string; description?: string; completed?: boolean }
): Promise<any> => {
  try {
    const response = await authenticatedRequest(`http://localhost:8000/api/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });

    if (response.status === 401) {
      // Token expired, the token has already been removed by authenticatedRequest
      // Re-throw to allow caller to handle redirect
      throw new Error('Authentication token expired. Please log in again.');
    }

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail?.message || errorData.detail || `Update task failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Update task error:', error);
    if (error instanceof Error) {
      if (error.message.includes('Network error')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      if (error.message.includes('Authentication token expired')) {
        // Re-throw authentication errors so callers can handle them
        throw error;
      }
      throw error;
    }
    throw new Error('Network error during task update');
  }
};

/**
 * Toggles the completion status of a task
 */
export const toggleTaskCompletion = async (taskId: string): Promise<any> => {
  try {
    const response = await authenticatedRequest(`http://localhost:8000/api/tasks/${taskId}/complete`, {
      method: 'PATCH',
    });

    if (response.status === 401) {
      // Token expired, the token has already been removed by authenticatedRequest
      // Re-throw to allow caller to handle redirect
      throw new Error('Authentication token expired. Please log in again.');
    }

    if (response.status === 503) {
      // Network error occurred, parse the error message
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || 'Network error: Unable to connect to the server. Please check if the backend is running.');
    }

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail?.message || errorData.detail || `Toggle task completion failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Toggle task completion error:', error);
    if (error instanceof Error) {
      if (error.message.includes('Network error')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      if (error.message.includes('Authentication token expired')) {
        // Re-throw authentication errors so callers can handle them
        throw error;
      }
      throw error;
    }
    throw new Error('Network error during task completion toggle');
  }
};

/**
 * Deletes a task
 */
export const deleteTask = async (taskId: string): Promise<any> => {
  try {
    const response = await authenticatedRequest(`http://localhost:8000/api/tasks/${taskId}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.status === 401) {
      // Token expired, the token has already been removed by authenticatedRequest
      // Re-throw to allow caller to handle redirect
      throw new Error('Authentication token expired. Please log in again.');
    }

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail?.message || errorData.detail || `Delete task failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Delete task error:', error);
    if (error instanceof Error) {
      if (error.message.includes('Network error')) {
        throw new Error('Network error: Unable to connect to the server. Please check if the backend is running.');
      }
      if (error.message.includes('Authentication token expired')) {
        // Re-throw authentication errors so callers can handle them
        throw error;
      }
      throw error;
    }
    throw new Error('Network error during task deletion');
  }
};