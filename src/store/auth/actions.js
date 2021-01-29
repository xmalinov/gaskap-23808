import * as types from "./constants"

//Example get balance actions
export const setEmail = email => ({
  type: types.SET_EMAIL,
  payload: email,
});

export const login = params => ({
  type: types.LOGIN,
  payload: params,
});

export const loginSucceeded = response => ({
  type: types.LOGIN_SUCCEEDED,
  payload: response,
});

export const loginFailed = error => ({
  type: types.LOGIN_FAILED,
  error,
});

export const signup = params => ({
  type: types.SIGNUP,
  payload: params,
});

export const signupSucceeded = response => ({
  type: types.SIGNUP_SUCCEEDED,
  payload: response,
});

export const signupFailed = error => ({
  type: types.SIGNUP_FAILED,
  error,
});


export const setSchool = school => ({
  type: types.SET_SCHOOL,
  payload: school,
});

export const setCode = code => ({
  type: types.SET_CODE,
  payload: code,
});

export const setUserType = user => ({
  type: types.SET_USER_TYPE,
  payload: user,
});

export const setName = name => ({
  type: types.SET_NAME,
  payload: name,
});

export const setParentName = parentName => ({
  type: types.SET_PARENT_NAME,
  payload: parentName,
});

export const setPassword = password => ({
  type: types.SET_PASSWORD,
  payload: password,
});

export const deactivateAccount = params => ({
  type: types.DEACTIVATE_ACCOUNT,
  payload: params,
});

export const deactivateAccountSucceeded = response => ({
  type: types.DEACTIVATE_ACCOUNT_SUCCEEDED,
  payload: response,
});

export const deactivateAccountFailed = error => ({
  type: types.DEACTIVATE_ACCOUNT_FAILED,
  payload: error,
});


export const logout = params => ({
  type: types.LOG_OUT,
  payload: params,
});

export const logoutSucceeded = response => ({
  type: types.LOG_OUT_SUCCEEDED,
  payload: response,
});

export const logoutFailed = error => ({
  type: types.LOG_OUT_FAILED,
  payload: error,
});

export const forgetPassword = params => ({
  type: types.FORGET_PASSWORD,
  payload: params,
});

export const forgetPasswordSucceeded = response => ({
  type: types.FORGET_PASSWORD_SUCCEEDED,
  payload: response,
});

export const forgetPasswordFailed = error => ({
  type: types.FORGET_PASSWORD_FAILED,
  payload: error,
});
