import "./App.css";
import API from "./API";
import { useEffect} from "react";
/* import Books from "./components/Books"; */
import Welcome from "./components/welcome.tsx";
import CounterHook from "./components/counter.tsx";

/* import { BrowserRouter as Router, Routes, Link, Route } from "react-router-dom"; */
/* import Contact from "./pages/contact"; */

function App() {
  /* Function useState(Permite guardar estados de nuestros componentes)*/
  /* Function useEfect hook (Permite hacer efectos secundarios en componentes funcionales)*/

  //Function for data API states
/*   const [books, setBooks] = useState(null); */

  //Function for data API of axios
  useEffect(() => {
    const fetchData = async () => {
 
      const data = await API.getData();
      return data;
    };
    fetchData();
  }, []);

  return (
    <>  
      <h1>Props, components</h1>
        <Welcome message="Hola desde la pagina" name="julian" />
        <br />
        <h2>components with hooks</h2>
        <CounterHook />
    </>
  );
}

export default App;
