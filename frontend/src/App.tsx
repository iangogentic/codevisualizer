/**
 * Main App Component with Routing
 * 
 * PRD Reference: PRD.md p.52-53
 * TASK: TASK-406
 */

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Visualization from './pages/Visualization';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analysis/:analysisId" element={<Visualization />} />
      </Routes>
    </Router>
  );
}

export default App;
