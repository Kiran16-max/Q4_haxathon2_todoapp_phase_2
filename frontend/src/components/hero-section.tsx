// frontend/src/components/hero-section.tsx
import React from 'react';
import Link from 'next/link';
import Button from './ui/button';

const HeroSection: React.FC = () => {
  return (
    <section className="pt-24 text-center sm:pt-32 lg:pt-40">
      <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl md:text-6xl">
        <span className="block">Manage Tasks</span>
        <span className="block text-purple-600 mt-2">Smarter with AI</span>
      </h1>
      <p className="mt-6 max-w-lg mx-auto text-xl text-gray-600">
        Our AI-powered todo app helps you organize your life with intelligent task management and natural language processing.
      </p>
      <div className="mt-10 flex justify-center space-x-4">
        <Link href="/signup">
          <Button size="large">Get Started - It's Free</Button>
        </Link>
        <Button variant="outline" size="large">Watch Demo</Button>
      </div>
    </section>
  );
};

export default HeroSection;