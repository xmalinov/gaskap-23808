import {keys} from '../constants/generalConstants';
import AsyncStorage from '@react-native-async-storage/async-storage';

export const storeAccessToken = async token => {
  try {
    await AsyncStorage.setItem(keys.accessToken, token);
  } catch (error) {
    console.log('AsyncStorage error during token store:', error);
  }
}

export const getAccessToken = async () => {
  try {
    const value = await AsyncStorage.getItem(keys.accessToken);

    return value;
  } catch (error) {
    console.log('AsyncStorage error during token store:', error);
  }
}