import React, { useState } from "react";
import { View, Text, Button } from "react-native";
import { useCounter } from "./Hooks/useCounter";

export const CustomHooks = () => {
  /*CustomHook for useCounter*/
  const { valor, acum } = useCounter();

  return (
    <>
      <View>
        <Text style={{ marginTop: 20, marginBottom: 10 }}>
          Custom hook: {valor}
        </Text>
        <Button title="incrementar" color={"#2500f5"} onPress={() => acum(1)} />
        <Text style={{ alignSelf: "center" }}>OR</Text>
        <Button
          title="decrementar"
          color={"#008b07"}
          onPress={() => acum(-1)}
        />
      </View>
    </>
  );
};
