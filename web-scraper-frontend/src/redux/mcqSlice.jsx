import { createSlice } from "@reduxjs/toolkit";

const mcqSlice = createSlice({
  name: "mcq",
  initialState: {
    questions: [],
  },
  reducers: {
    setQuestions: (state, action) => {
      state.questions = action.payload;  // Updating the questions in the state
    },
  },
});

export const { setQuestions } = mcqSlice.actions;  // Export the setQuestions action
export default mcqSlice.reducer;  // Export the reducer to be used in the store
