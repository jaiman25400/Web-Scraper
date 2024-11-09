import { configureStore } from "@reduxjs/toolkit";
import mcqReducer from "./mcqSlice";  // Import the mcqReducer from the slice file

const store = configureStore({
  reducer: {
    mcq: mcqReducer,  // Setting up mcq state using the mcqReducer
  },
});

export default store;
