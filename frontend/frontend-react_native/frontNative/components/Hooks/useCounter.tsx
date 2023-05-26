import { useState } from "react";

export const useCounter = () => {
  /*UseState for data*/

  const [valor, setValor] = useState(0);

  /*Function to customHook*/
  const acum = (numero: number) => {
    setValor(valor + numero);
  };
  /*Return data and function*/
  return {
    valor,
    acum,
  };
};
