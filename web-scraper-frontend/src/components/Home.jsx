import React, { useState } from "react";
import "../styles/Home.CSS"; // Import CSS file for styling (create this in the styles folder)
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const Home = () => {
  const [url, setUrl] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Handler for submit button
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true); // Disable the button during submission

    try {
      const res = await axios.post("http://127.0.0.1:5000//api/submit-url", {
        url,
      });
      console.log("Response : ", res.data);
      toast.success("URL submitted successfully!");
    } catch (error) {
      console.log("Error :", error);
      toast.error("Failed to submit URL. Please try again.");
    } finally {
      setIsSubmitting(false); // Re-enable the button after completion
      setUrl(""); // Clear the input field
    }
  };

  return (
    <div className="home-outer-block  ">
      <form onSubmit={handleSubmit} className="url-form ">
        <input
          type="url"
          placeholder="Enter a website URL..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="url-input"
          required
        />

        <button
          type="submit"
          className="btn btn-success  btn-md btn-block"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Submitting..." : "Submit"}
        </button>
        {/* Toast Container for notifications */}
        <ToastContainer position="top-right" autoClose={3000} />
      </form>
    </div>
  );
};

export default Home;
