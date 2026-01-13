// frontend/src/hooks/use-error-handler.ts
import { useState, useCallback } from 'react';

interface ErrorState {
  message: string;
  type: 'error' | 'warning' | 'info' | 'success';
  visible: boolean;
}

const useErrorHandler = () => {
  const [error, setError] = useState<ErrorState>({ 
    message: '', 
    type: 'error', 
    visible: false 
  });

  const showError = useCallback((message: string, type: ErrorState['type'] = 'error') => {
    setError({ message, type, visible: true });
    
    // Auto-hide error after 5 seconds
    setTimeout(() => {
      setError(prev => ({ ...prev, visible: false }));
    }, 5000);
  }, []);

  const hideError = useCallback(() => {
    setError(prev => ({ ...prev, visible: false }));
  }, []);

  return {
    error,
    showError,
    hideError
  };
};

export default useErrorHandler;