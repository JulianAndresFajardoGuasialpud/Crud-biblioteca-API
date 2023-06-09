import React from "react";

export default function Welcome(props: any) {
  console.log(props);
  const {message, name} = props;
  return(
    <>
        <div>
            <p>Hola, {name}</p>
            <br />
            <b>{message}</b>
            <br />
        </div>
    </>
  )
}
