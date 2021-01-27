import {profileListItems} from '../../constants/generalConstants';
import * as types from './constants';

const initialState = {
  schools: [],
  users: ['Teacher', 'Parent', 'Student'],
  profile: {},
  profileItems: [],
  isLoadingProfile: false,
  profileError: '',
  isChangingPassword: false,
  isChangingEmail: false,
  isChangingPhone: false,
  isDeactivatingAccount: false,
  isLoggingOut: false,
  isMakingNetworkRequest: false,
  settingsError: '',
  profileUpdateFailed: false,
  userUpdateFailed: true,
  updatingProfilePhoto: false,
  profilePhotoFailed: false,
};

const getSchoolsSuccess = (state, action) => {
  return {
    ...state,
    schools: action.data ? action.data.results : [],
  };
};

const getProfileStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isLoadingProfile: true,
    profileError: '',
  };
};

const getProfileSuccess = (state, action) => {
  console.log('success', action, profileListItems[action.payload.user_type]);
  return {
    ...state,
    profile: action.payload,
    isLoadingProfile: false,
    profileItems: profileListItems[action.payload.user_type],
    profileError: '',
  };
};

const getProfileFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    profileError: 'Unable to fetch user details',
    isLoadingProfile: false,
  };
};

const changePasswordStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    settingsError: '',
  };
};

const changePasswordSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: '',
  };
};

const changePasswordFailed = (state, action) => {
  console.log(action, 'failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: action.payload,
  };
};

const changeEmailStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    settingsError: '',
  };
};

const changeEmailSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: '',
  };
};

const changeEmailFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: 'Unable to Change password',
  };
};

const changePhoneStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    settingsError: '',
  };
};

const changePhoneSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: '',
  };
};

const changePhoneFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    settingsError: 'Unable to Change phone number',
  };
};

const updateProfileStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    profileError: '',
  };
};

const updateProfileSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    profile: {
      ...state.profile,
      profile: action.payload,
    },
    profileError: '',
  };
};

const updateProfileFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    profileError: 'Unable to update profile',
  };
};

const updateUserStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    profileError: '',
    userUpdateFailed: false,
  };
};

const updateUserSuccess = (state, action) => {
  console.log('success', action);
  return {
    ...state,
    isMakingNetworkRequest: false,
    profileError: '',
    profile: action.payload,
    userUpdateFailed: false,
  };
};

const updateUserFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    profileError: 'Unable to update user',
    userUpdateFailed: true,
  };
};

const updateProfilePhotoStarted = (state, action) => {
  console.log('started');
  return {
    ...state,
    isMakingNetworkRequest: true,
    profileError: '',
    updateProfilePhotoFailed: false,
  };
};

const updateProfilePhotoSuccess = (state, action) => {
  console.log('success', action.payload);
  return {
    ...state,
    isMakingNetworkRequest: false,
    profileError: '',
    profile: {
      ...state.profile,
      profile: action.payload,
    },
    updateProfilePhotoFailed: false,
  };
};

const updateProfilePhotoFailed = (state, action) => {
  console.log('failed');
  return {
    ...state,
    isMakingNetworkRequest: false,
    profileError: 'Unable to upload profile photo',
    updateProfilePhotoFailed: true,
  };
};

const handlers = {
  [types.GET_SCHOOLS_SUCCEEDED]: getSchoolsSuccess,
  [types.GET_PROFILE]: getProfileStarted,
  [types.GET_PROFILE_SUCCEEDED]: getProfileSuccess,
  [types.GET_PROFILE_FAILED]: getProfileFailed,

  [types.UPDATE_PASSWORD]: changePasswordStarted,
  [types.UPDATE_PASSWORD_SUCCEEDED]: changePasswordSuccess,
  [types.UPDATE_PASSWORD_FAILED]: changePasswordFailed,

  [types.UPDATE_EMAIL]: changeEmailStarted,
  [types.UPDATE_EMAIL_SUCCEEDED]: changeEmailSuccess,
  [types.UPDATE_EMAIL_FAILED]: changeEmailFailed,

  [types.UPDATE_PHONE]: changePhoneStarted,
  [types.UPDATE_PHONE_SUCCEEDED]: changePhoneSuccess,
  [types.UPDATE_PHONE_FAILED]: changePhoneFailed,

  [types.UPDATE_PROFILE]: updateProfileStarted,
  [types.UPDATE_PROFILE_SUCCEEDED]: updateProfileSuccess,
  [types.UPDATE_PROFILE_FAILED]: updateProfileFailed,

  [types.UPDATE_USER]: updateUserStarted,
  [types.UPDATE_USER_SUCCEEDED]: updateUserSuccess,
  [types.UPDATE_USER_FAILED]: updateUserFailed,

  [types.UPDATE_PROFILE_PHOTO]: updateProfilePhotoStarted,
  [types.UPDATE_PROFILE_PHOTO_SUCCEEDED]: updateProfilePhotoSuccess,
  [types.UPDATE_PROFILE_PHOTO_FAILED]: updateProfilePhotoFailed,
};

export default function authReducer(state = initialState, action) {
  const handler = handlers[action.type];

  if (typeof handler === 'undefined') {
    return state;
  }

  return handler(state, action);
}
