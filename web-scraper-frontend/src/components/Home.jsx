import React, { useState } from "react";
import "../styles/Home.CSS"; // Import CSS file for styling (create this in the styles folder)
import axios from "axios";

const Home = () => {
  const [url, setUrl] = useState("");

  // Handler for submit button
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:5000//api/submit-url",{
        url
      })
      console.log("Response : ",res.data)
    } catch (error) {
      console.log("Error :",error)
    }
  };

  return (
    <div className="home-outer-block container-fluid">
        <form onSubmit={handleSubmit} className="url-form ">
          <input
            type="url"
            placeholder="Enter a website URL..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="url-input"
            required
          />
          <button type="submit" className="btn btn-secondary  btn-lg btn-block">
            Submit
          </button>
        </form>
    </div>
  );
};

export default Home;
