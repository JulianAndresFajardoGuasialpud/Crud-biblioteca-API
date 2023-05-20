import axios from "axios";

const API = {
    
    getData: async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/get/')
            return response.data;
        } catch (errors) {
            console.error('Error al obtener los datos:', errors);
            throw errors;
        }
    }
};

export default API;