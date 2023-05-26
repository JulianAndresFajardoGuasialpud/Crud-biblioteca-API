import React from 'react'
import { View, Text } from "react-native";

/*Function void arguments*/
const sumar = () =>{
  let a = 12;
  let b = 5;

  return a + b;
}
/*Function with arguments or parameters*/
const sumParameter = (c: number, d: number) => {
  return c + d;
}

export const Funciones = () => {
  return (
    <View>
      <Text>Resultado de suma sin parametros mediante funciones: {sumar()}</Text>
      <Text>Resultado de suma de funcion con parametros: {sumParameter(15, 5)}</Text>
    </View>
  )
}
