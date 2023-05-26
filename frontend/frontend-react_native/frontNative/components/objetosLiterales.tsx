import React from 'react';
import { View, Text } from "react-native";

/*Import constants of expo for styles CSS react-native*/
import Constants from 'expo-constants';

/*define Interface (saber como seran los objetos)
    Las interfaces solo sirven para poner reglar de validacion a nuestros objetos
    */
interface Person {
  nombreCompleto: string;
  edad: number;
  direccion: Direccion;
}
interface Direccion {
  pais: string;
  casaNo: number;
}

export const ObjetosLiterales = () => {
  //define const to read validated rules
  const person: Person = {
    nombreCompleto: "julian fajardo",
    edad: 23,
    direccion: {
      pais: "canada",
      casaNo: 1234,
    },
  };

  /*  const direccion: Direccion = {
    pais: "canada",
    casaNo: 123,
  } */

  return (
    <>
      <View style={{margin: Constants.statusBarHeight}}>
        <Text>Introduccion a TS - REACT-NATIVE</Text>
{/*           <Text style={{ margin: 30 }}>Objetos Literales {person.direccion.pais}</Text> */}
      </View>
    </>
  );
};
