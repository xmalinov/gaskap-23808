import {end_points, request_methods} from '../constants/generalConstants';
import {requestToServer} from '../utils/http';

const getProfile = action => {
  const url = end_points.profile;
  const info = {
    url,
    method: request_methods.get,
    params: {},
  };

  return requestToServer(info);
};

const changePassword = action => {
  const url = end_points.changePassword;
  const info = {
    url,
    method: request_methods.post,
    params: action.obj,
  };

  return requestToServer(info);
};

const changeEmail = action => {
  const url = end_points.changeEmail;
  const info = {
    url,
    method: request_methods.patch,
    params: action.obj,
  };
  console.log(info);
  return requestToServer(info);
};

const changePhone = action => {
  const url = end_points.changePhone;
  const info = {
    url,
    method: request_methods.put,
    params: action.obj,
  };

  return requestToServer(info);
};

const updateProfile = action => {
  const url = end_points.updateProfile;
  const info = {
    url,
    method: request_methods.patch,
    params: action.obj,
  };

  console.log(info);
  return requestToServer(info);
};

const updateUser = action => {
  const url = end_points.updateUser;
  const info = {
    url,
    method: request_methods.patch,
    params: action.obj,
  };

  console.log(info);
  return requestToServer(info);
};

const sendVerificationEmail = () => {
  const url = end_points.sendConfirmationEmail;
  const info = {
    url,
    method: request_methods.post,
  };

  console.log(info);
  return requestToServer(info);
};

export const userApiService = {
  getProfile,
  changePassword,
  changeEmail,
  changePhone,
  updateProfile,
  updateUser,
  sendVerificationEmail,
};
