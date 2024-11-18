// src/components/Navbar.jsx
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar navbar-light  bg-dark">
      <div className="container-fluid" >
      <Link to="/" className="navbar-brand mb-0 " style={{color : "white"}}>Home</Link>
      </div>
    </nav>
  );
};

export default Navbar;
