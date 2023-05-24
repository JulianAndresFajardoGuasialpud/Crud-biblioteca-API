import React from "react";
import { View, Text } from "react-native";

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
  
  return (
    <>
      <View>
        <Text style={{ margin: 30 }}>Objetos Literales</Text>
      </View>
    </>
  );
};
