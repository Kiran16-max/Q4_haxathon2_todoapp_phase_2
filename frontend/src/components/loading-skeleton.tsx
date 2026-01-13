// frontend/src/components/loading-skeleton.tsx
import React from 'react';

interface LoadingSkeletonProps {
  type?: 'card' | 'text' | 'avatar' | 'button';
  width?: string;
  height?: string;
  className?: string;
}

const LoadingSkeleton: React.FC<LoadingSkeletonProps> = ({ 
  type = 'card', 
  width, 
  height, 
  className = '' 
}) => {
  let classes = 'animate-pulse bg-gray-200 rounded-md ';
  
  switch (type) {
    case 'card':
      classes += 'h-24 ';
      break;
    case 'text':
      classes += 'h-4 ';
      break;
    case 'avatar':
      classes += 'rounded-full h-10 w-10 ';
      break;
    case 'button':
      classes += 'h-10 rounded-md ';
      break;
    default:
      classes += 'h-24 ';
  }
  
  if (width) classes += `w-${width} `;
  if (height) classes += `h-${height} `;
  
  return <div className={`${classes} ${className}`} />;
};

export default LoadingSkeleton;