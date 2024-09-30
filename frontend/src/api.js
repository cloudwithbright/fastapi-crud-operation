import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Update with your FastAPI URL

export const getItems = async () => {
    const response = await axios.get(`${API_URL}/items`);
    return response.data;
};

export const createItem = async (item) => {
    const response = await axios.post(`${API_URL}/items`, item);
    return response.data;
};

export const updateItem = async (itemId, item) => {
    const response = await axios.put(`${API_URL}/items/${itemId}`, item);
    return response.data;
};

export const deleteItem = async (itemId) => {
    const response = await axios.delete(`${API_URL}/items/${itemId}`);
    return response.data;
};

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await axios.post(`${API_URL}/uploadfile/`, formData);
    return response.data;
};
