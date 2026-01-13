// frontend/src/components/chat-input.tsx
import React, { useState } from 'react';
import Button from './ui/button';

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSendMessage, isLoading }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    onSendMessage(inputValue);
    setInputValue('');
  };

  return (
    <form onSubmit={handleSubmit} className="border-t border-gray-200 p-4">
      <div className="flex space-x-2">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Ask me to manage your tasks..."
          className="flex-1 border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
          disabled={isLoading}
        />
        <Button type="submit" disabled={isLoading || !inputValue.trim()}>
          Send
        </Button>
      </div>
      <div className="mt-2 text-xs text-gray-500">
        Examples: "Add a task to buy groceries", "Show my tasks", "Mark task 1 as complete"
      </div>
    </form>
  );
};

export default ChatInput;