import React from "react"
import Home from "./components/Home"
import Navbar from "./components/Navbar"
import "./styles/App.css"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {

  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <Routes>
        <Route path="/" element={<Home />} /> 
        </Routes>
      </div>
    </Router>
  )
}

export default App
