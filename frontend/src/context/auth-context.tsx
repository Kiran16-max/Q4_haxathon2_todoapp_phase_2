// frontend/src/context/auth-context.tsx
import React, { createContext, useContext, ReactNode } from 'react';
import { User } from '../lib/auth';
import { useAuthFlow } from '../hooks/use-auth-flow';

interface LoginResult {
  success: boolean;
  user?: User;
  error?: string;
}

interface RegisterResult {
  success: boolean;
  user?: User;
  error?: string;
}

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  error: string | null;
  isAuthenticated: boolean;
  signupAndLogin: (signupData: { name: string; email: string; password: string }) => Promise<{ success: boolean; user?: User; error?: string }>;
  login: (email: string, password: string) => Promise<{ success: boolean; user?: User; error?: string }>;
  logout: () => void;
  clearError: () => void;
  register: (name: string, email: string, password: string) => Promise<RegisterResult>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const authFlow = useAuthFlow();

  const register = async (name: string, email: string, password: string) => {
    return authFlow.signupAndLogin({ name, email, password });
  };

  const value: AuthContextType = {
    ...authFlow,
    user: authFlow.user,
    login: authFlow.login,
    register,
    logout: authFlow.logout,
    isAuthenticated: authFlow.isAuthenticated,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};