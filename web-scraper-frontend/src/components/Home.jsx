import React, { useState } from "react";
import "../styles/Home.CSS"; // Import CSS file for styling (create this in the styles folder)
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setQuestions } from "../redux/mcqSlice";

const Home = () => {
  const [url, setUrl] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false); // New loading state
  const dispatch = useDispatch();

  // Handler for submit button
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true); // Disable the button during submission
    setLoading(true); // Show loading spinner


    try {
      const res = await axios.post("http://127.0.0.1:5000//api/submit-url", {
        url,
      });
      console.log("Response : ", res.data);
      toast.success("URL submitted successfully!");
      dispatch(setQuestions(res.data));
      navigate("/mcq"); // Redirect to MCQ page

    } catch (error) {
      console.log("Error :", error);
      toast.error("Failed to submit URL. Please try again.");
    } finally {
      setIsSubmitting(false); // Re-enable the button after completion
      setUrl(""); // Clear the input field
      setLoading(false); // Hide loading spinner

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
        {loading && <div className="loading-spinner">Processing...</div>} 

        <ToastContainer position="top-right" autoClose={3000} />
      </form>
    </div>
  );
};

export default Home;
