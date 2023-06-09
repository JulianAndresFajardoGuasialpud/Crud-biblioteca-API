import { useEffect, useReducer } from "react";
import { View, Text, Button } from "react-native";

/*Import constants of expo for styles CSS react-native*/
import Constants from "expo-constants";

/*Define rules of types*/
interface AuthState {
  validation: boolean;
  token: string | null;
  username: string;
  password: string;
}

/*Define structure data of the interface*/
const InitialState: AuthState = {
  validation: true,
  token: null,
  username: "",
  password: "",
};

/*Define action to signIn*/
type loginUI = {
  username: string;
  password: string;
};

/*Define actions to execute*/
type AuthAction = { type: "signIn"; payload: loginUI } | { type: "logout" };

/*Define comportament of structures functions */
const authReduce = (state: AuthState, action: AuthAction): AuthState => {
  switch (action.type) {
    case "signIn":
      const {username, password} = action.payload;
      return {
        validation: false,
        token: "asdawdawdwdawd",
        username,
        password
      };

    case "logout":
      return {
        validation: false,
        token: null,
        username: "",
        password: "",
      };
    default:
      return state;
  }
};

export const Login = () => {
  /*Is how useState but reduce the comportament of functions*/
  const [{ validation, token, username }, dispatch] = useReducer(
    authReduce,
    InitialState
  );

  useEffect(() => {
    setTimeout(() => {
      dispatch({ type: "logout" });
    }, 1500);
  }, []);

  /*Function to dispatch loginUI*/
  const loginUI = () => {
    dispatch({
      type: "signIn",
      payload: {
        username: "Julian Fajardo",
        password: "B0dlfisx",
      },
    });
  };

  /*Function to dispatch logoutUI with useEffect and setTimeOut*/
  const logoutUI = () => {
    dispatch({
      type: "logout",
    });
  };

  /*Is to declarate condicional functional components*/
  if (validation) {
    /*Return view of useReducer*/
    return (
      <>
        <View style={{ margin: Constants.statusBarHeight }}>
          <Text
            style={{
              marginTop: 20,
              marginBottom: 15,
              alignSelf: "center",
              backgroundColor: "#4f5bff",
              color: "#fff",
            }}
          >
            Validating....
          </Text>
        </View>
      </>
    );
  }

  /*Return view component login*/
  return (
    <>
      <View>
        <Text style={{ marginTop: 20, marginBottom: 15, alignSelf: "center" }}>
          Login:
        </Text>

        {/*Validation token*/}

        {token ? (
          <>
            <Text style={{ backgroundColor: "#00af0fca", color: "#fff" }}>
              Autenticado como: {username}
            </Text>
            <Text style={{ marginBottom: 10 }}></Text>
            <Button
              title="logout"
              color={"#00af0fca"}
              onPress={logoutUI}
            ></Button>
          </>
        ) : (
          <>
            <Text
              style={{
                backgroundColor: "#bd1a1a",
                color: "#fff",
                textAlign: "center",
              }}
            >
              No autenticado!
            </Text>
            <Text style={{ marginBottom: 10 }}></Text>
            <Button title="signIn" onPress={loginUI}></Button>
          </>
        )}
      </View>
    </>
  );
};
