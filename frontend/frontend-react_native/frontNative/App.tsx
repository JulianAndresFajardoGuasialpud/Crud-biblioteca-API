import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

/*Import component tipos basicos*/
/* import TiposBasicos from './components/tiposBasicos';
 */

/*import component objetos literales*/
import { ObjetosLiterales } from "./components/objetosLiterales";

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Introduccion a TS - REACT-NATIVE</Text>

      <StatusBar style="auto" />
      {/*       <TiposBasicos/> */}
      <ObjetosLiterales />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
