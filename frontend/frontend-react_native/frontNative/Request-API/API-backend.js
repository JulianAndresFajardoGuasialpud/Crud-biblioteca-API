import axios from "axios";

const request = axios.create({
  data: {},
  baseURL: "http://127.0.0.1:8000",
});

export default request;
