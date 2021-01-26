import {put, call, all, spawn, takeEvery} from 'redux-saga/effects';
import * as types from './constants';
import {schoolApiService} from '../../services/school';
import * as actions from './actions';
import * as authActions from './../auth/actions';
import {userApiService} from '../../services/user';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../constants/message';
import {storeAccessToken} from '../../utils/storageUtils';
import generalUtils from '../../utils/gneralUtils';

function* getSchoolsWorker(action) {
  try {
    const result = yield call(schoolApiService.getAllSchools, action);
    yield put(actions.getSchoolsSucceeded(result));
  } catch (err) {
    yield put(actions.getSchoolsFailed(err));
  }
}

function* getSchoolWatcher() {
  yield takeEvery(types.GET_SCHOOLS, getSchoolsWorker);
}

function* getProfileWorker(action) {
  try {
    const result = yield call(userApiService.getProfile, action);
    console.log(result.data);
    yield put(actions.getProfileSucceeded(result.data));
  } catch (err) {
    yield put(actions.getProfileFailed(err));
  }
}

function* getProfileWatcher() {
  yield takeEvery(types.GET_PROFILE, getProfileWorker);
}

function* changePasswordWorker(action) {
  try {
    const result = yield call(userApiService.changePassword, action);
    SimpleToast.show(authMessage.loginAgain);
    yield put(authActions.logout());
    yield put(actions.changePasswordSucceeded(result.data));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    SimpleToast.show(errorMessage);
    yield put(actions.changePasswordFailed(errorMessage));
  }
}

function* changePasswordWatcher() {
  yield takeEvery(types.UPDATE_PASSWORD, changePasswordWorker);
}

function* changeEmailWorker(action) {
  try {
    const result = yield call(userApiService.updateUser, action);
    //TODO send verification email
    // yield call(userApiService.sendVerificationEmail, action);
    SimpleToast.show(authMessage.loginAgain);
    yield put(authActions.logout());
    yield put(actions.changeEmailSucceeded(result.data));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    SimpleToast.show(errorMessage);
    console.log(errorMessage);
    yield put(actions.changeEmailFailed(errorMessage));
  }
}

function* changeEmailWatcher() {
  yield takeEvery(types.UPDATE_EMAIL, changeEmailWorker);
}

function* changePhoneWorker(action) {
  try {
    const result = yield call(userApiService.changePhone, action);
    console.log(result.data);
    yield put(actions.changePhoneSucceeded(result.data));
  } catch (err) {
    yield put(actions.changePhoneFailed(err));
  }
}

function* changePhoneWatcher() {
  yield takeEvery(types.UPDATE_PHONE, changePhoneWorker);
}

function* updateProfileWorker(action) {
  try {
    const result = yield call(userApiService.updateProfile, action);
    console.log(result.data);
    yield put(actions.updateProfileSucceeded(result.data));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    const message = Array.isArray(errorMessage)
      ? errorMessage[0]
      : errorMessage;
    SimpleToast.show(message, SimpleToast.LONG);
    yield put(actions.updateProfileFailed(message));
  }
}

function* updateProfileWatcher() {
  yield takeEvery(types.UPDATE_PROFILE, updateProfileWorker);
}

function* updateUserWorker(action) {
  try {
    console.log(action);
    const result = yield call(userApiService.updateUser, action);
    console.log(result.data);
    yield put(actions.updateUserSucceeded(result.data));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    const message = Array.isArray(errorMessage)
      ? errorMessage[0]
      : errorMessage;
    SimpleToast.show(message, SimpleToast.LONG);
    yield put(actions.updateUserFailed(message));
  }
}

function* updateUserWatcher() {
  yield takeEvery(types.UPDATE_USER, updateUserWorker);
}

function* updateProfilePhotoWorker(action) {
  try {
    console.log(action);
    const result = yield call(userApiService.updateProfilePhoto, action);
    console.log(result.data);
    yield put(actions.updateProfilePhotoSucceeded(result.data));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    const message = Array.isArray(errorMessage)
      ? errorMessage[0]
      : errorMessage;
    SimpleToast.show(message, SimpleToast.LONG);
    yield put(actions.updateProfilePhotoFailed(message));
  }
}

function* updateProfilePhotoWatcher() {
  yield takeEvery(types.UPDATE_PROFILE_PHOTO, updateProfilePhotoWorker);
}

// Read more information about root sagas in the documentation
// https://redux-saga.js.org/docs/advanced/RootSaga.html
export default function* customRootSaga() {
  const sagas = [
    // Example watcher
    // getBalanceWatcher
    getSchoolWatcher,
    getProfileWatcher,
    changePasswordWatcher,
    changeEmailWatcher,
    changePhoneWatcher,
    updateProfileWatcher,
    updateUserWatcher,
    updateProfilePhotoWatcher,
  ];

  yield all(
    sagas.map(saga =>
      spawn(function* () {
        while (true) {
          try {
            yield call(saga);
            break;
          } catch (e) {
            console.log(e);
          }
        }
      }),
    ),
  );
}
