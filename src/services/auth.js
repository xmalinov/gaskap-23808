import { end_points, request_methods } from '../constants/generalConstants';
import { requestToServer } from '../utils/http';

const signup = action => {
  const url = end_points.signup;
  const info = {
    url,
    method: request_methods.post,
    params: action.obj,
  };

  return requestToServer(info);
};

const login = action => {
  const params = action.obj;
  const url = end_points.login;
  const info = {
    url,
    method: request_methods.post,
    params: params,
  };

  return requestToServer(info);
};

const deactivateAccount = action => {
  const url = end_points.deactivateAccount;
  const info = {
    url,
    method: request_methods.put,
    params: action.obj,
  };

  return requestToServer(info);
}

const logout = action => {
  const url = end_points.logout;
  const info = {
    url,
    method: request_methods.post,
    params: action.obj,
  };

  return requestToServer(info);
}


export const authApiService = {
  signup,
  login,
  logout,
  deactivateAccount
};
