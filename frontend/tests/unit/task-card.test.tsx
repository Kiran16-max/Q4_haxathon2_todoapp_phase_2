// frontend/tests/unit/task-card.test.tsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import TaskCard from '../../src/components/task-card';

describe('TaskCard Component', () => {
  const defaultProps = {
    id: '1',
    title: 'Test Task',
    description: 'Test Description',
    completed: false,
    createdAt: '2023-01-01T00:00:00Z',
    updatedAt: '2023-01-01T00:00:00Z',
    onToggle: jest.fn(),
    onDelete: jest.fn(),
    onEdit: jest.fn(),
  };

  it('renders task title and description', () => {
    render(<TaskCard {...defaultProps} />);
    
    expect(screen.getByText('Test Task')).toBeInTheDocument();
    expect(screen.getByText('Test Description')).toBeInTheDocument();
  });

  it('displays correct status badge', () => {
    render(<TaskCard {...defaultProps} />);
    
    expect(screen.getByText('Pending')).toBeInTheDocument();
    
    render(<TaskCard {...defaultProps} completed={true} />);
    expect(screen.getByText('Completed')).toBeInTheDocument();
  });

  it('calls onToggle when toggle button is clicked', () => {
    const onToggleMock = jest.fn();
    render(<TaskCard {...defaultProps} onToggle={onToggleMock} />);
    
    const toggleButton = screen.getByText('Mark Complete');
    fireEvent.click(toggleButton);
    
    expect(onToggleMock).toHaveBeenCalledWith('1');
  });

  it('calls onDelete when delete button is clicked', () => {
    const onDeleteMock = jest.fn();
    render(<TaskCard {...defaultProps} onDelete={onDeleteMock} />);
    
    const deleteButton = screen.getByText('Delete');
    fireEvent.click(deleteButton);
    
    expect(onDeleteMock).toHaveBeenCalledWith('1');
  });

  it('calls onEdit when edit button is clicked', () => {
    const onEditMock = jest.fn();
    render(<TaskCard {...defaultProps} onEdit={onEditMock} />);
    
    const editButton = screen.getByText('Edit');
    fireEvent.click(editButton);
    
    expect(onEditMock).toHaveBeenCalledWith('1');
  });
});