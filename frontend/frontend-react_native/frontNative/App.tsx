import { View } from "react-native";

/*import components*/
import { ObjetosLiterales } from "./components/objetosLiterales";
import { Funciones } from "./components/funciones";
import { Contador } from "./components/Contador";
import { CustomHooks } from "./components/CustomHooks";
import TiposBasicos from "./components/tiposBasicos";
import { Login } from "./components/Login";

export default function App() {
  return (
    <View>
      {/*    
      <TiposBasicos/>
      <Funciones/>
      <Contador/>
      <CustomHooks/>
       */}
      <ObjetosLiterales />
      <Login />
    </View>
  );
}
