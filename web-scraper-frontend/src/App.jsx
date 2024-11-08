import React from "react"
import Home from "./components/Home"
import Navbar from "./components/Navbar"
import "./styles/App.css"
function App() {

  return (
    <>
      <div className="app-container">
        <Navbar />
        <Home />
      </div>
    </>
  )
}

export default App
