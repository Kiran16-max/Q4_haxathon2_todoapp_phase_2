// frontend/src/hooks/use-auth-flow.ts
import { useState, useEffect } from 'react';
import { User } from '../lib/auth';
import { 
  registerUser, 
  loginUser, 
  storeToken, 
  removeToken,
  getToken 
} from '../lib/auth-utils';

interface AuthFlowState {
  user: User | null;
  isLoading: boolean;
  error: string | null;
  isAuthenticated: boolean;
}

interface SignupData {
  name: string;
  email: string;
  password: string;
}

export const useAuthFlow = () => {
  const [state, setState] = useState<AuthFlowState>({
    user: null,
    isLoading: false,
    error: null,
    isAuthenticated: false,
  });

  // Check authentication status on mount
  useEffect(() => {
    const token = getToken();
    if (token) {
      // In a real implementation, you would validate the token or fetch user details
      // For now, we'll just set the authenticated state based on token presence
      setState(prev => ({
        ...prev,
        isAuthenticated: true,
      }));
    }
  }, []);

  const signupAndLogin = async (signupData: SignupData) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));

    try {
      // Attempt to register the user
      let authResult;
      try {
        authResult = await registerUser({
          name: signupData.name,
          email: signupData.email,
          password: signupData.password,
        });
      } catch (registerError) {
        // If registration fails because user already exists, try to log in
        if (registerError instanceof Error) {
          if (registerError.message.includes('already registered')) {
            // User already exists, proceed to login
            authResult = await loginUser({
              email: signupData.email,
              password: signupData.password,
            });
          } else {
            // Some other registration error
            throw registerError;
          }
        } else {
          // Unexpected error type
          throw new Error('Registration failed due to an unexpected error');
        }
      }

      // Store the token
      storeToken(authResult.access_token);

      // Update state with user info
      setState({
        user: authResult.user,
        isLoading: false,
        error: null,
        isAuthenticated: true,
      });

      return { success: true, user: authResult.user };
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred';
      
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));

      return { success: false, error: errorMessage };
    }
  };

  const login = async (email: string, password: string) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));

    try {
      const authResult = await loginUser({
        email,
        password,
      });

      // Store the token
      storeToken(authResult.access_token);

      // Update state with user info
      setState({
        user: authResult.user,
        isLoading: false,
        error: null,
        isAuthenticated: true,
      });

      return { success: true, user: authResult.user };
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred';
      
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));

      return { success: false, error: errorMessage };
    }
  };

  const logout = () => {
    removeToken();
    setState({
      user: null,
      isLoading: false,
      error: null,
      isAuthenticated: false,
    });
  };

  const clearError = () => {
    setState(prev => ({ ...prev, error: null }));
  };

  return {
    ...state,
    signupAndLogin,
    login,
    logout,
    clearError,
  };
};