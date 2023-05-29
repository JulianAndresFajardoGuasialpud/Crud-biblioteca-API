import React, { useEffect } from 'react'
import {View, Text} from 'react-native';
import request from '../Request-API/API-backend';

export const Usuarios = () => {
    useEffect(() => {
        request.get("admin/")
        .then(resp =>{
          console.log(resp)
        })
        .catch(console.log)
    }, [])

  return (
    <View>
        <Text>
            Usuarios:
        </Text>
    </View>
  )
}
