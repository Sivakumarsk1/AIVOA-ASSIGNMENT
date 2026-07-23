import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const complaintApi = createApi({
  reducerPath: 'complaintApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8000/api' }),
  endpoints: (builder) => ({
    getComplaints: builder.query({
      query: () => '/complaints',
    }),
    getComplaint: builder.query({
      query: (id) => `/complaints/${id}`,
    }),
    createComplaint: builder.mutation({
      query: (complaint) => ({
        url: '/complaints',
        method: 'POST',
        body: complaint,
      }),
    }),
    updateComplaint: builder.mutation({
      query: ({ id, ...patch }) => ({
        url: `/complaints/${id}`,
        method: 'PUT',
        body: patch,
      }),
    }),
    deleteComplaint: builder.mutation({
      query: (id) => ({
        url: `/complaints/${id}`,
        method: 'DELETE',
      }),
    }),
  }),
});

export const {
  useGetComplaintsQuery,
  useGetComplaintQuery,
  useCreateComplaintMutation,
  useUpdateComplaintMutation,
  useDeleteComplaintMutation,
} = complaintApi;
