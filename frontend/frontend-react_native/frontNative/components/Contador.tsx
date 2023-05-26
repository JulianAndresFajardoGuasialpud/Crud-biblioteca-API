import React, { useState } from "react";
import { View, Text, Button } from "react-native";

export const Contador = () => {
  const [valor, setValor] = useState(0);

  const acum = (numero: number) => {
    setValor(valor + numero);
  };

  return (
    <>
      <View>
        <Text style={{ marginTop: 20, marginBottom: 10 }}>
          Contador con hook of useState: {valor}
        </Text>
        <Button title="incrementar" color={"#f194ff"} onPress={() => acum(1)} />
        <Text style={{ alignSelf: "center" }}>OR</Text>
        <Button
          title="decrementar"
          color={"#DE1504"}
          onPress={() => acum(-1)}
        />
      </View>
    </>
  );
};
