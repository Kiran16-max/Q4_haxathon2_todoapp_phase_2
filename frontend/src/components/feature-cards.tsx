// frontend/src/components/feature-cards.tsx
import React from 'react';

interface FeatureCardProps {
  icon: React.ReactNode;
  title: string;
  description: string;
}

const FeatureCard: React.FC<FeatureCardProps> = ({ icon, title, description }) => {
  return (
    <div className="bg-white p-8 rounded-xl shadow-lg transform transition-transform duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center">
        {icon}
      </div>
      <h3 className="mt-6 text-xl font-bold text-gray-900">{title}</h3>
      <p className="mt-4 text-gray-600">
        {description}
      </p>
    </div>
  );
};

const FeatureCards: React.FC = () => {
  return (
    <section className="mt-16">
      <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        <FeatureCard 
          icon={
            <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
            </svg>
          }
          title="Smart Task Management"
          description="Organize your tasks with due dates, categories, and priority levels."
        />
        <FeatureCard 
          icon={
            <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.87-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
            </svg>
          }
          title="AI-Powered Assistant"
          description="Interact with our AI chatbot using natural language to manage tasks effortlessly."
        />
        <FeatureCard 
          icon={
            <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
          }
          title="Secure & Private"
          description="Your data is encrypted and securely stored with industry-standard security measures."
        />
      </div>
    </section>
  );
};

export default FeatureCards;