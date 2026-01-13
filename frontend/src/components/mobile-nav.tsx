// frontend/src/components/mobile-nav.tsx
import React, { useState } from 'react';
import Link from 'next/link';
import Button from './ui/button';

const MobileNav: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="md:hidden">
      <button
        onClick={toggleMenu}
        className="text-gray-700 hover:text-purple-600 focus:outline-none"
      >
        <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          {isOpen ? (
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          ) : (
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          )}
        </svg>
      </button>

      {isOpen && (
        <div className="absolute top-16 inset-x-0 bg-white shadow-lg rounded-md py-4 px-4 space-y-3">
          <Link href="#features" className="block text-gray-700 hover:text-purple-600" onClick={toggleMenu}>
            Features
          </Link>
          <Link href="#how-it-works" className="block text-gray-700 hover:text-purple-600" onClick={toggleMenu}>
            How It Works
          </Link>
          <Link href="#pricing" className="block text-gray-700 hover:text-purple-600" onClick={toggleMenu}>
            Pricing
          </Link>
          <div className="pt-4 flex flex-col space-y-3">
            <Link href="/login" className="block" onClick={toggleMenu}>
              <Button variant="outline" className="w-full">Log in</Button>
            </Link>
            <Link href="/signup" className="block" onClick={toggleMenu}>
              <Button className="w-full">Sign up</Button>
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default MobileNav;