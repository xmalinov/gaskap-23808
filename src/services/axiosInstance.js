import axios from 'axios';
import { general_message } from '../constants/message';
import { isConnectedToNetwork, request } from '../utils/http';
import { getAccessToken } from '../utils/storageUtils';

// import { handleErrors } from '../errorHandler';

// Add a request interceptor
var GaskAxiosInstance = axios.create();
GaskAxiosInstance.CancelToken = axios.CancelToken;
GaskAxiosInstance.isCancel = axios.isCancel;

GaskAxiosInstance.interceptors.request.use(
  async config => {
    try {
      // const isConnected = await isConnectedToNetwork();
      // console.log(isConnected, '+++++++');
      // if (isConnected) {
      //   TODO: Get accessToken if required
      const accessToken = await getAccessToken();

      // if token is found add it to the header
      if (accessToken) {
        config.headers.Authorization = `Token ${accessToken}`;
      }

      const baseURL = 'https://gaskap-23808.botics.co';

      if (!baseURL) {
        throw general_message.no_base_url;
      } else {
        config.baseURL = baseURL;
      }

      console.log(config);
      return config;
      // } else {
      //   return Promise.reject(Error('No Internet Connection'));
      // }
    } catch (error) {
      Promise.reject(error);
    }
  },
  error => {
    // Do something with request error
    return Promise.reject(error);
  },
);

GaskAxiosInstance.interceptors.response.use(
  response => {
    console.log(response, 'response');
    // Do something with response data
    return response;
  },
  error => {
    console.log(error.response, 'error')
    // Do something with response error
    // TODO: add a new error handler function
    // return promise.reject(handleErrors(error));    
    return Promise.reject(error.response.data);
  },
);

export default GaskAxiosInstance;
