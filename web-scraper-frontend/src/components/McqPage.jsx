import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { Button, Container, Form } from "react-bootstrap";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate, useLocation } from "react-router-dom";

const McqPage = () => {
  const mcqData = useSelector((state) => state.mcq.questions.mcq_data);
  const [answers, setAnswers] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const { url } = location.state || {};

  useEffect(() => {
    console.log("MCQ data:", mcqData, url);
  }, [mcqData]);

  const handleOptionChange = (questionId, option) => {
    setAnswers((prevAnswers) => ({
      ...prevAnswers,
      [questionId]: option,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setLoading(true);
    console.log("User Answers:", answers);
    try {
      const res = await axios.post("http://15.222.14.129/:5000/api/submit-answers", {
        answers,
        url,
      });
      console.log("Response:", res.data);
      toast.success("Thank You For Your Response!", {
        onClose: () => navigate("/"),
        autoClose: 1500,
      });
    } catch (error) {
      console.log("Error:", error);
      toast.error("Failed to submit answers. Please try again.");
    } finally {
      setIsSubmitting(false);
      setLoading(false);
    }
  };

  return (
    <Container className="mt-4">
      {mcqData ? (
        <>
          <h2 className="welcome-heading text-center">MCQ Questions</h2>
          <Form
            onSubmit={handleSubmit}
            style={{ paddingTop: "2%", paddingBottom: "3%" }}
          >
            {mcqData.map((mcq) => (
              <div
                key={mcq.question}
                className="mb-4"
                style={{ fontSize: "1rem" }} // Smaller font size for questions
              >
                <div className="fw-bold mb-2">
                  Q) {mcq.question}
                </div>
                <div className="d-flex flex-wrap gap-2">
                  {Object.entries(mcq.options).map(([key, option]) => (
                    <Button
                      key={key}
                      variant={
                        answers[mcq.question] === option
                          ? "primary"
                          : "outline-secondary"
                      }
                      className="btn-sm text-truncate" // Smaller button with truncation for long text
                      style={{
                        minWidth: "150px",
                        fontSize: "0.85rem", // Smaller font for options
                      }}
                      onClick={() => handleOptionChange(mcq.question, option)}
                    >
                      {option}
                    </Button>
                  ))}
                </div>
              </div>
            ))}
            <Button type="submit" variant="success" disabled={isSubmitting}>
              {isSubmitting ? "Submitting..." : "Submit"}
            </Button>
            {loading && <div className="loading-spinner">Processing...</div>}
          </Form>
        </>
      ) : (
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            paddingTop: "30%",
            textAlign: "center",
          }}
        >
          <h2>Hi, Please submit URL on Home Screen to generate MCQ's Here</h2>
        </div>
      )}
      <ToastContainer position="top-right" autoClose={3000} />
    </Container>
  );
};

export default McqPage;
