// frontend/src/lib/auth.ts
// User interface for the application

export interface User {
  id: string;
  email: string;
  name: string;
}

// This is now a simple interface for the rest of the app
// The actual authentication logic is handled by auth-utils and use-auth-flow