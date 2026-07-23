import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const aiApi = createApi({
  reducerPath: 'aiApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8000/api' }),
  endpoints: (builder) => ({
    extractFromFile: builder.mutation({
      query: (formData) => ({
        url: '/ai/extract',
        method: 'POST',
        body: formData,
      }),
    }),
    extractFromText: builder.mutation({
      query: (text) => ({
        url: '/ai/extract-text',
        method: 'POST',
        body: { text },
      }),
    }),
    chatWithAI: builder.mutation({
      query: (message) => ({
        url: '/ai/chat',
        method: 'POST',
        body: { message },
      }),
    }),
  }),
});

export const {
  useExtractFromFileMutation,
  useExtractFromTextMutation,
  useChatWithAIMutation,
} = aiApi;
