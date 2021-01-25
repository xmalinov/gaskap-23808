import * as types from './constants'

/* Example get balance actions
export const getBalance = id => ({
  type: types.GET_BALANCE, id
})

export const getBalanceSucceeded = response => ({
  type: types.GET_BALANCE_SUCCEEDED, response
})

export const getBalanceFailed = error => ({
  type: types.GET_BALANCE_FAILED, error
})
 */

//Example get balance actions

export const getSchools = params => ({
  type: types.GET_SCHOOLS,
  params,
});

export const getSchoolsSucceeded = response => ({
  type: types.GET_SCHOOLS_SUCCEEDED,
  data: response.data,
});

export const getSchoolsFailed = error => ({
  type: types.GET_SCHOOLS_FAILED,
  error,
});

export const getProfile = params => ({
  type: types.GET_PROFILE,
  params,
});

export const getProfileSucceeded = response => ({
  type: types.GET_PROFILE_SUCCEEDED,
  payload: response,
});

export const getProfileFailed = error => ({
  type: types.GET_PROFILE_FAILED,
  error,
});

export const changePassword = params => ({
  type: types.UPDATE_PASSWORD,
  payload: params,
});

export const changePasswordSucceeded = response => ({
  type: types.UPDATE_PASSWORD_SUCCEEDED,
  payload: response,
});

export const changePasswordFailed = error => ({
  type: types.UPDATE_PASSWORD_FAILED,
  payload: error,
});


export const changeEmail = params => ({
  type: types.UPDATE_EMAIL,
  payload: params,
});

export const changeEmailSucceeded = response => ({
  type: types.UPDATE_EMAIL_SUCCEEDED,
  payload: response,
});

export const changeEmailFailed = error => ({
  type: types.UPDATE_EMAIL_FAILED,
  payload: error,
});


export const changePhone = params => ({
  type: types.UPDATE_PROFILE,
  payload: params,
});

export const changePhoneSucceeded = response => ({
  type: types.UPDATE_PROFILE_SUCCEEDED,
  payload: response,
});

export const changePhoneFailed = error => ({
  type: types.UPDATE_PHONE_FAILED,
  payload: error,
});

export const updateProfile = params => ({
  type: types.UPDATE_PROFILE,
  payload: params,
});

export const updateProfileSucceeded = response => ({
  type: types.UPDATE_PROFILE_SUCCEEDED,
  payload: response,
});

export const updateProfileFailed = error => ({
  type: types.UPDATE_PROFILE_FAILED,
  payload: error,
});

export const updateUser = params => ({
  type: types.UPDATE_USER,
  payload: params,
});

export const updateUserSucceeded = response => ({
  type: types.UPDATE_USER_SUCCEEDED,
  payload: response,
});

export const updateUserFailed = error => ({
  type: types.UPDATE_USER_FAILED,
  payload: error,
});

export const updateProfilePhoto = params => ({
  type: types.UPDATE_PROFILE_PHOTO,
  payload: params,
});

export const updateProfilePhotoSucceeded = response => ({
  type: types.UPDATE_PROFILE_PHOTO_SUCCEEDED,
  payload: response,
});

export const updateProfilePhotoFailed = error => ({
  type: types.UPDATE_PROFILE_PHOTO_FAILED,
  payload: error,
});
