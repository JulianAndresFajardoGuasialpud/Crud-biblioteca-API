import "./App.css";
import API from "./API";
import { useEffect } from "react";
import Welcome from "./components/welcome.tsx";
import CounterHook from "./components/counter.tsx";

function App() {
  /* Function hook to get axios (los hook son funciones en las que podremos guardas estados de nuestros componentes)*/
  useEffect(() => {
    const fetchData = async () => {
      try {
        const datos = await API.getData();
        console.log("Datos obtenidos:", datos);
      } catch (errors) {
        console.error("Error al obtener los datos:", errors);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <h1>Props, components</h1>
      <Welcome message="Hola desde la pagina" name="julian" />
      <br/>
      <h2>components with hooks</h2>
      <CounterHook/>
    </>
  );
}

export default App;
