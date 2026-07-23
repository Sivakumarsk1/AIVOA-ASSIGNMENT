import React from 'react';
import './StatusBadge.css';

const StatusBadge = ({ status = 'Pending Triage' }) => {
  return (
    <div className="status-badge">
      {status}
    </div>
  );
};

export default StatusBadge;
