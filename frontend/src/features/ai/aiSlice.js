import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  extractionProgress: 0,
  extractionStatus: 'idle', // 'idle' | 'extracting' | 'complete' | 'error'
  chatMessages: [
    {
      role: 'ai',
      content: 'Upload a complaint document or paste text above.\nI will automatically extract the details and populate the form for you.',
    }
  ],
  isProcessing: false,
};

const aiSlice = createSlice({
  name: 'ai',
  initialState,
  reducers: {
    setProgress: (state, action) => {
      state.extractionProgress = action.payload;
    },
    setStatus: (state, action) => {
      state.extractionStatus = action.payload;
    },
    addMessage: (state, action) => {
      state.chatMessages.push(action.payload);
    },
    clearMessages: (state) => {
      state.chatMessages = [initialState.chatMessages[0]];
    },
    setProcessing: (state, action) => {
      state.isProcessing = action.payload;
    },
  },
});

export const { setProgress, setStatus, addMessage, clearMessages, setProcessing } = aiSlice.actions;

export const selectAi = (state) => state.ai;

export default aiSlice.reducer;
