import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { Button, Container, Form } from "react-bootstrap";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";

const McqPage = () => {
  const mcqData = useSelector((state) => state.mcq.questions.question_data);
  const [answers, setAnswers] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Log MCQ data on component mount
  useEffect(() => {
    console.log("MCQ data:", mcqData);
  }, [mcqData]);

  // Handle option selection
  const handleOptionChange = (questionId, option) => {
    setAnswers((prevAnswers) => ({
      ...prevAnswers,
      [questionId]: option,
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setLoading(true);
    console.log("User Ans : ",answers)
    try {
      const res = await axios.post("http://127.0.0.1:5000/api/submit-answers", {
        answers,
      });
      console.log("Response:", res.data);
      toast.success("Answers submitted successfully!");
      navigate("/")
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
          <h2 className="text-center">MCQ Questions</h2>
          <Form onSubmit={handleSubmit} style={{ paddingTop : "2%" }}>
            {mcqData.map((mcq) => (
              <div key={mcq.question} className="mb-4" style={{ paddingTop : "1%" }}>
                <div>{mcq.question}</div>
                <Form.Check
                  type="radio"
                  label={mcq.options.A}
                  name={`question-${mcq.question}`}
                  onChange={() => handleOptionChange(mcq.question, mcq.options.A)}
                  checked={answers[mcq.question] === mcq.options.A}
                />
                <Form.Check
                  type="radio"
                  label={mcq.options.B}
                  name={`question-${mcq.question}`}
                  onChange={() => handleOptionChange(mcq.question, mcq.options.B)}
                  checked={answers[mcq.question] === mcq.options.B}
                />
                <Form.Check
                  type="radio"
                  label={mcq.options.C}
                  name={`question-${mcq.question}`}
                  onChange={() => handleOptionChange(mcq.question, mcq.options.C)}
                  checked={answers[mcq.question] === mcq.options.C}
                />
                <Form.Check
                  type="radio"
                  label={mcq.options.D}
                  name={`question-${mcq.question}`}
                  onChange={() => handleOptionChange(mcq.question, mcq.options.D)}
                  checked={answers[mcq.question] === mcq.options.D}
                />
              </div>
            ))}
            <Button type="submit" variant="primary" disabled={isSubmitting}>
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
