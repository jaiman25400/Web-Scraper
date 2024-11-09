import React from "react";
import { useSelector } from "react-redux";
import { useEffect } from "react";

const McqPage = () => {
  const mcqData = useSelector((state) => state.mcq.questions);
  useEffect (() => {
    console.log("MCQqq :",mcqData)
  },[])
  return <div>MCQData </div>;
};

export default McqPage;
