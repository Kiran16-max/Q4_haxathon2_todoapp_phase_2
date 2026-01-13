// frontend/src/lib/chatbot-welcome.ts
export const getWelcomeMessage = (): string => {
  return "Hello! I'm your AI task assistant. You can ask me to add, list, update, or complete tasks. How can I help you today?";
};

export const getOnboardingMessages = (): string[] => {
  return [
    "You can ask me things like:",
    "- 'Add a task to buy groceries'",
    "- 'Show my tasks'",
    "- 'Mark task 1 as complete'",
    "- 'Update task 2 with new details'"
  ];
};

export const getErrorMessage = (): string => {
  return "Sorry, I didn't understand that. You can ask me to add, list, update, or complete tasks.";
};