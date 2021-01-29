import * as types from './constants';

const initialState = {
  user: {},
  auth: true,
  email: '',
  password: '',
  schoolName: '',
  parentName: '',
  userType: '',
  userName: '',
  code: '',

  isLoggingIn: false,
  loginResult: {},
  loginError: '',
  loginSuccess: false,

  isRegisteringUser: false,
  signupResult: {},
  signupError: '',
  registrationSuccess: false,
  deactivationFailed: false,
  isMakingNetworkRequest: false,
  passwordResetSuccess: false,
};

const loginStarted = (state, action) => {
  return {
    ...state,
    isLoggingIn: true,
    loginError: '',
  };
};

const loginSuccess = (state, action) => {
  return {
    ...state,
    auth: true,
    loginResult: action.payload.data,
    user: action.payload.data.user,
    loginError: '',
    isLoggingIn: false,
    loginSuccess: true,
  };
};

const loginFailed = (state, action) => {
  return {
    ...state,
    loginError: 'Login Failed, check if the email is verified.',
    isLoggingIn: false,
  };
};

const signupStarted = (state, action) => {
  return {
    ...state,
    isRegisteringUser: true,
    signupError: '',
  };
};

const signupSuccess = (state, action) => {
  return {
    ...state,
    signupResult: action.data,
    signupError: '',
    isRegisteringUser: false,
    registrationSuccess: true,
  };
};

const signupFailed = (state, action) => {
  console.log(action);

  return {
    ...state,
    // signupError: action.error,
    signupError: 'Registration Failed',
    isRegisteringUser: false,
  };
};

const setParentSuccess = (state, action) => {
  return {
    ...state,
    parent: action.data,
  };
};

const setSchoolSuccess = (state, action) => {
  return {
    ...state,
    schoolName: action.payload,
  };
};

const setUserTypeSuccess = (state, action) => {
  return {
    ...state,
    userType: action.payload,
  };
};

const setEmailSuccess = (state, action) => {
  return {
    ...state,
    email: action.payload,
  };
};

const setCodeSuccess = (state, action) => {
  console.log('code success');
  return {
    ...state,
    code: action.payload,
  };
};

const setNameSuccess = (state, action) => {
  // console.log('name success')
  return {
    ...state,
    userName: action.payload,
  };
};

const setPasswordSuccess = (state, action) => {
  return {
    ...state,
    password: action.payload,
  };
};

const deactiveateAccountStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    loginError: '',
    deactivationFailed: false,
  };
};

const deactiveateAccountSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    loginError: '',
    deactivationFailed: false,
  };
};

const deactiveateAccountFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    loginError: 'Unable to deactivate account',
    deactivationFailed: true,
  };
};

const logoutStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    loginError: '',
  };
};

const logoutSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    loginError: '',
    auth: false,
  };
};

const logoutFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    loginError: 'Unable to logout',
  };
};

const forgetPasswordStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    passwordResetSuccess: false,
    loginError: '',
  };
};

const forgetPasswordSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    passwordResetSuccess: true,
    loginError: '',
    auth: false,
  };
};

const forgetPasswordFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    passwordResetSuccess: false,
    loginError: 'Unable to send a link.',
  };
};

const handlers = {
  [types.SET_EMAIL]: setEmailSuccess,
  [types.SET_USER_TYPE]: setUserTypeSuccess,
  [types.SET_PASSWORD]: setPasswordSuccess,
  [types.SET_SCHOOL]: setSchoolSuccess,
  [types.SET_PARENT_NAME]: setParentSuccess,
  [types.SET_CODE]: setCodeSuccess,
  [types.SET_NAME]: setNameSuccess,

  [types.LOGIN]: loginStarted,
  [types.LOGIN_SUCCEEDED]: loginSuccess,
  [types.LOGIN_FAILED]: loginFailed,

  [types.SIGNUP]: signupStarted,
  [types.SIGNUP_SUCCEEDED]: signupSuccess,
  [types.SIGNUP_FAILED]: signupFailed,

  [types.DEACTIVATE_ACCOUNT]: deactiveateAccountStarted,
  [types.DEACTIVATE_ACCOUNT_SUCCEEDED]: deactiveateAccountSuccess,
  [types.DEACTIVATE_ACCOUNT_FAILED]: deactiveateAccountFailed,

  [types.LOG_OUT]: logoutStarted,
  [types.LOG_OUT_SUCCEEDED]: logoutSuccess,
  [types.LOG_OUT_FAILED]: logoutFailed,

  [types.FORGET_PASSWORD]: forgetPasswordStarted,
  [types.FORGET_PASSWORD_SUCCEEDED]: forgetPasswordSuccess,
  [types.FORGET_PASSWORD_FAILED]: forgetPasswordFailed,
};

export default function authReducer(state = initialState, action) {
  const handler = handlers[action.type];

  if (typeof handler === 'undefined') {
    return state;
  }

  return handler(state, action);
}
