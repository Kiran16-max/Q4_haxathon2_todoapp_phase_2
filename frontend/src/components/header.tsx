// frontend/src/components/header.tsx
import React from 'react';
import Link from 'next/link';
import Button from './ui/button';

const Header: React.FC = () => {
  return (
    <header className="absolute inset-x-0 top-0 z-10 flex items-center justify-between px-4 sm:px-6 lg:px-8 py-6">
      <div className="flex items-center">
        <Link href="/">
          <h1 className="text-2xl font-bold text-purple-700">TaskBot</h1>
        </Link>
      </div>
      <nav className="hidden md:flex space-x-10">
        <a href="#features" className="text-gray-700 hover:text-purple-600">Features</a>
        <a href="#how-it-works" className="text-gray-700 hover:text-purple-600">How It Works</a>
        <a href="#pricing" className="text-gray-700 hover:text-purple-600">Pricing</a>
      </nav>
      <div className="flex items-center space-x-4">
        <Link href="/login">
          <Button variant="outline">Log in</Button>
        </Link>
        <Link href="/signup">
          <Button>Sign up</Button>
        </Link>
      </div>
    </header>
  );
};

export default Header;