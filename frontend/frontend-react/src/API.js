import axios from "axios";

const API = {
    
    getData: async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/get/');
            return console.log("Datos obtenidos:", response.data);
        } catch (errors) {
            if (errors.get_404) {
                errors.get_404 = axios.get('http://127.0.0.1:8000/')
                console.error('Error al obtener los datos:', errors.get_404);
            }
            throw errors;
        }
    }
};

export default API;