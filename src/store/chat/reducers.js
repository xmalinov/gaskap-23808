import * as types from './constants';

const initialState = {
  users: [],
  loadingUsers: false,
  error: '',
};

const getUsersStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    loadingUsers: true,
    error: '',
  };
};

const getUsersSuccess = (state, action) => {
  return {
    ...state,
    profile: action.payload,
    loadingUsers: false,
    users: action.payload,
    error: '',
  };
};

const getUsersFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    error: 'Unable to get users',
    loadingUsers: false,
  };
};

const handlers = {
  [types.GET_USERS]: getUsersStarted,
  [types.GET_USERS_SUCCEEDED]: getUsersSuccess,
  [types.GET_USERS_FAILED]: getUsersFailed,
};

export default function chatReducer(state = initialState, action) {
  const handler = handlers[action.type];

  if (typeof handler === 'undefined') {
    return state;
  }

  return handler(state, action);
}
