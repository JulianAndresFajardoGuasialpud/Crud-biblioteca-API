import React from "react";
import { View, Text } from "react-native";

export default function TiposBasicos() {
  //define constant variables
  const nombre: string = "Julian Fajardo";
  const edad: number = 23;
  const stateActive: boolean = false;

  //define array of string
  const fruts: string[] = ["apple", "pera", "banano", "uvas"];

  return (
    <View>
      <Text style={{ margin: 20 }}>Tipos basicos con typescript</Text>
      <Text style={{ margin: 30 }}>
        {nombre}, {edad}, {stateActive ? "activo: " : "no activo: "}{" "}
        {fruts.join(" ")}
      </Text>
    </View>
  );
}
