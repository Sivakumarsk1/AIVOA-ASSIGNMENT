import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ComplaintPage from './pages/ComplaintPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<ComplaintPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
