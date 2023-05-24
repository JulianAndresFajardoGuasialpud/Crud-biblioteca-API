import React from "react";
import { useState, useEffect } from "react";

/* Function useState(Permite guardar estados de nuestros componentes)*/
/* Function useEfect hook (Permite hacer efectos secundarios en componentes funcionales)*/

export default function CounterHook(_props) {
  //useState for the loop the counter sumar
  const [counter, setCounter] = useState(0);
  //useState for changes dinamically
  const [semaforo, setSemaforo] = useState(false);


  //Function for the effect
  useEffect(() => {
    console.log(semaforo);
  }, [semaforo]);

  //Function for counter and colors
  const countNum = () => {
    setCounter(counter + 1);
    setSemaforo(!semaforo);
  };

  return (
    <>
      <div>
        {/*         <h3>Numero actual del contador: {counter}</h3>
        <button
          type="submit"
          onClick={() => {
            setCounter(counter + 1);
          }}
        >
          sumar counter
        </button> */}

        <h3>Numero actual del contador: {counter}</h3>
        <p>El color del semaforo es el: {semaforo ? "red" : "green"}</p>
        <button type="submit" onClick={countNum}>
          sumar counter
        </button>
      </div>
    </>
  );
}
