import axios from "axios";

export default axios.create({
    baseURL: 'https://con-backend-1:8000/api'
});