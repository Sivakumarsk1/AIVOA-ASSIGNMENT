import React from 'react';
import { useAppSelector } from '../../app/hooks';
import { selectAi } from './aiSlice';
import './ExtractionProgress.css';

const ExtractionProgress = () => {
  const { extractionProgress, extractionStatus } = useAppSelector(selectAi);

  if (extractionStatus !== 'extracting') return null;

  return (
    <div className="extraction-progress-container">
      <h4 className="section-label">EXTRACTION PROGRESS</h4>
      <div className="progress-bar-bg">
        <div 
          className="progress-bar-fill" 
          style={{ width: `${extractionProgress}%` }}
        >
          <span className="progress-text">{extractionProgress}%</span>
        </div>
      </div>
      <p className="status-text">Analyzing document content and extracting key details...</p>
      <p className="sub-status-text">Please wait, this may take a few moments.</p>
    </div>
  );
};

export default ExtractionProgress;
