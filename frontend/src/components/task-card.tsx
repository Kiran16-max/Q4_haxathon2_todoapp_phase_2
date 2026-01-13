// frontend/src/components/task-card.tsx
import React from 'react';
import Button from './ui/button';

interface TaskCardProps {
  id: string;
  title: string;
  description: string;
  completed: boolean;
  createdAt: string;
  updatedAt: string;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
  onEdit: (id: string) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({
  id,
  title,
  description,
  completed,
  onToggle,
  onDelete,
  onEdit
}) => {
  return (
    <div 
      className={`bg-white rounded-lg shadow-md p-6 border-l-4 transition-all duration-300 ease-in-out transform hover:scale-[1.02] ${
        completed ? 'border-green-500 opacity-80' : 'border-yellow-500'
      }`}
    >
      <div className="flex justify-between items-start">
        <div>
          <h3 className={`text-lg font-medium ${
            completed ? 'line-through text-gray-500' : 'text-gray-900'
          }`}>
            {title}
          </h3>
          {description && (
            <p className="mt-2 text-gray-600">{description}</p>
          )}
        </div>
        <span className={`px-2 py-1 text-xs rounded-full ${
          completed 
            ? 'bg-green-100 text-green-800' 
            : 'bg-yellow-100 text-yellow-800'
        }`}>
          {completed ? 'Completed' : 'Pending'}
        </span>
      </div>
      
      <div className="mt-4 flex justify-between items-center">
        <div className="flex space-x-2">
          <Button 
            variant={completed ? "outline" : "primary"} 
            onClick={() => onToggle(id)}
            className="text-sm"
          >
            {completed ? 'Mark Incomplete' : 'Mark Complete'}
          </Button>
          <Button 
            variant="outline" 
            onClick={() => onEdit(id)}
            className="text-sm"
          >
            Edit
          </Button>
        </div>
        <Button 
          variant="outline" 
          onClick={() => onDelete(id)}
          className="text-sm text-red-600 hover:text-red-800"
        >
          Delete
        </Button>
      </div>
    </div>
  );
};

export default TaskCard;