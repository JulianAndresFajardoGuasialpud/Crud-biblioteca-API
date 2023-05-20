import React from "react";
import { useState } from "react";

export default function CounterHook(props) {
  //State for the loop the counter
  const [ counter, setCounter ] = useState([0]);

  return (
    <>
      <div>
        <h3>Numero actual del contador: {counter}</h3>
        <button type="submit" onClick={()=> setCounter(counter)}>sumar counter</button>
      </div>
    </>
  );
}
