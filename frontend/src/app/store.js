import { configureStore } from '@reduxjs/toolkit';
import complaintReducer from '../features/complaints/complaintSlice';
import aiReducer from '../features/ai/aiSlice';
import { complaintApi } from '../features/complaints/complaintApi';
import { aiApi } from '../features/ai/aiApi';

export const store = configureStore({
  reducer: {
    complaint: complaintReducer,
    ai: aiReducer,
    [complaintApi.reducerPath]: complaintApi.reducer,
    [aiApi.reducerPath]: aiApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(complaintApi.middleware, aiApi.middleware),
});
