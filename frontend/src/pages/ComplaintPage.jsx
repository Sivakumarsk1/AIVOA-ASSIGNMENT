import React from 'react';
import ComplaintForm from '../features/complaints/ComplaintForm';
import AIAssistantPanel from '../features/ai/AIAssistantPanel';
import './ComplaintPage.css';

const ComplaintPage = () => {
  return (
    <div className="page-container">
      <div className="left-panel">
        <ComplaintForm />
      </div>
      <div className="right-panel">
        <AIAssistantPanel />
      </div>
    </div>
  );
};

export default ComplaintPage;
