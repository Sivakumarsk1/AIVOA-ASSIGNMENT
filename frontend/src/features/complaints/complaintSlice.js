import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  complaintSource: '',
  customerName: '',
  productName: '',
  productStrength: '',
  batchNumber: '',
  manufacturingDate: '',
  expiryDate: '',
  quantityAffected: '',
  complaintType: '',
  complaintDate: '',
  complaintDescription: '',
  initialSeverity: '',
  priority: '',
  status: 'Pending Triage',
};

const complaintSlice = createSlice({
  name: 'complaint',
  initialState,
  reducers: {
    setField: (state, action) => {
      const { field, value } = action.payload;
      if (field in state) {
        state[field] = value;
      }
    },
    setAllFields: (state, action) => {
      return { ...state, ...action.payload };
    },
    resetForm: () => initialState,
    setStatus: (state, action) => {
      state.status = action.payload;
    },
  },
});

export const { setField, setAllFields, resetForm, setStatus } = complaintSlice.actions;

export const selectComplaint = (state) => state.complaint;

export default complaintSlice.reducer;
