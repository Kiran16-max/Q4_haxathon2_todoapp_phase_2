import '../styles/globals.css';
import type { AppProps } from 'next/app';
import { AuthProvider } from '../context/auth-context';
import { TaskProvider } from '../context/task-context';
import { ThemeProvider } from '../context/theme-context';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider>
      <AuthProvider>
        <TaskProvider>
          <Component {...pageProps} />
        </TaskProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default MyApp;