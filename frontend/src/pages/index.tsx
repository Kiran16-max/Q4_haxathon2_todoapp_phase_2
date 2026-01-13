// frontend/src/pages/index.tsx
import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import Button from '../components/ui/button';

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-indigo-100">
      <Head>
        <title>AI-Powered Todo App | Manage Tasks Smarter</title>
        <meta name="description" content="A modern todo application with AI chatbot integration" />
      </Head>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="relative pt-10 pb-20 sm:pb-24">
          {/* Header */}
          <header className="absolute inset-x-0 top-0 z-10 flex items-center justify-between px-4 sm:px-6 lg:px-8 py-6">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-purple-700">TaskBot</h1>
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

          {/* Hero Section */}
          <div className="pt-24 text-center sm:pt-32 lg:pt-40">
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
          </div>

          {/* Features Section */}
          <section id="features" className="mt-24">
            <div className="text-center">
              <h2 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">Powerful Features</h2>
              <p className="mt-4 max-w-2xl mx-auto text-xl text-gray-600">
                Everything you need to stay organized and productive
              </p>
            </div>

            <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
              <div className="bg-white p-8 rounded-xl shadow-lg">
                <div className="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center">
                  <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
                  </svg>
                </div>
                <h3 className="mt-6 text-xl font-bold text-gray-900">Smart Task Management</h3>
                <p className="mt-4 text-gray-600">
                  Organize your tasks with due dates, categories, and priority levels.
                </p>
              </div>

              <div className="bg-white p-8 rounded-xl shadow-lg">
                <div className="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center">
                  <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.87-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
                  </svg>
                </div>
                <h3 className="mt-6 text-xl font-bold text-gray-900">AI-Powered Assistant</h3>
                <p className="mt-4 text-gray-600">
                  Interact with our AI chatbot using natural language to manage tasks effortlessly.
                </p>
              </div>

              <div className="bg-white p-8 rounded-xl shadow-lg">
                <div className="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center">
                  <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
                  </svg>
                </div>
                <h3 className="mt-6 text-xl font-bold text-gray-900">Secure & Private</h3>
                <p className="mt-4 text-gray-600">
                  Your data is encrypted and securely stored with industry-standard security measures.
                </p>
              </div>
            </div>
          </section>

          {/* CTA Section */}
          <div className="mt-24 bg-purple-700 rounded-2xl overflow-hidden">
            <div className="relative pt-16 pb-20 px-4 sm:px-6 lg:px-8 lg:pt-24 lg:pb-28">
              <div className="relative mx-auto max-w-7xl">
                <div className="text-center">
                  <h2 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
                    Ready to boost your productivity?
                  </h2>
                  <p className="mt-6 max-w-2xl mx-auto text-xl text-purple-200">
                    Join thousands of users who are already organizing their lives smarter.
                  </p>
                  <div className="mt-10">
                    <Link href="/signup">
                      <Button size="large">Start Free Trial</Button>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;