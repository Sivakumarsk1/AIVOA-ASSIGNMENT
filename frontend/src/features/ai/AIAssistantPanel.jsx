import React from 'react';
import FileUpload from './FileUpload';
import ExtractionProgress from './ExtractionProgress';
import ChatInterface from './ChatInterface';
import './AIAssistantPanel.css';

const AIAssistantPanel = () => {
  return (
    <div className="ai-panel">
      <div className="ai-panel-header">
        <h2>AI Complaint Intake Assistant</h2>
        <span className="beta-badge">BETA</span>
      </div>
      
      <div className="ai-panel-card">
        <FileUpload />
        <ExtractionProgress />
        <ChatInterface />
      </div>
    </div>
  );
};

export default AIAssistantPanel;
