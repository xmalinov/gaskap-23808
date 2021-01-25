import axios from 'axios';
import { appConfig } from '../config/app';
import { request_methods } from '../constants/generalConstants';
import { general_message } from '../constants/message';
import NetInfo from '@react-native-community/netinfo';
import GaskAxiosInstance from '../services/axiosInstance';

const APP_PLATFORM = 'Mobile';

export const request = axios.create({
  headers: {
    app_platform: APP_PLATFORM,
    app_version: 1,
  },
});

export const isConnectedToNetwork = () => {
  return new Promise((resolve, reject) => {
    NetInfo.isConnected
      .fetch()
      .then(isConnected => {
        resolve(isConnected);
      })
      .catch(error => reject(error));
  });
};

export function setupHttpConfig() {
  request.defaults.baseURL = appConfig.emailAuthAPIEndPoint;
  request.defaults.timeout = appConfig.defaultTimeout;
  axios.defaults.headers['Content-Type'] = 'application/json';
  // todo add auth token from store

  // you can add more default values for http requests here
}

export const requestToServer = info => {
  const axiosInstance = GaskAxiosInstance;

  switch (info.method) {
    case request_methods.post:
      return axiosInstance.post(info.url, info.params);
    case request_methods.get:
      return axiosInstance.get(info.url, { params: info.params });
    // return axiosInstance.get(info.url);
    case request_methods.patch:
      return axiosInstance.patch(info.url, info.params);
    case request_methods.put:
      return axiosInstance.put(info.url, { params: info.params });
    default:
      return Promise.reject(Error(general_message.method_not_found));
  }
};
