import {
  put,
  call,
  all,
  spawn,
  takeEvery,
  takeLatest,
  throttle,
} from 'redux-saga/effects';
import {customApiService} from './services';
import * as types from './constants';
import * as actions from './actions';
import {authApiService} from '../../services/auth';
import {storeAccessToken} from '../../utils/storageUtils';
import SimpleToast from 'react-native-simple-toast';
import generalUtils from '../../utils/gneralUtils';

/* Example worker saga and watcher setup

// Worker
function* getBalanceWorker(action) {
  try {
    const result = yield call(customApiService.getBalance, action)
    yield put(actions.getBalanceSucceeded(result))
  } catch (err) {
    yield put(actions.getBalanceFailed(err))
  }
}
*/
function* loginWorker(action) {
  // yield put(actions.loginSucceeded({}));
  try {
    const result = yield call(authApiService.login, action);

    yield call(storeAccessToken, result.data.key);
    yield put(actions.loginSucceeded(result));
  } catch (err) {
    const errorMessage = generalUtils.parseErrorMessage(err);
    const message = Array.isArray(errorMessage)
      ? errorMessage[0]
      : errorMessage;
    SimpleToast.show(message);
    yield put(actions.loginFailed(err));
  }
}

function* setSchoolWorker(action) {
  yield put(actions.setSchool(action.obj.selectedSchool));
}

function* setUserTypeWorker(action) {
  if (action.obj) {
    yield put(actions.setUserType(action.obj.selectedUserType));
  }
}

function* setEmailWorker(action) {
  if (action.obj) {
    yield put(actions.setEmail(action.obj.email));
  }
}

function* setParentWorker(action) {
  yield put(actions.setParentName(action.obj.parentName));
}

function* setPasswordWorker(action) {
  if (action.obj) {
    yield put(actions.setPassword(action.obj.password));
  }
}

function* setCodeWorker(action) {
  if (action.obj) {
    yield put(actions.setCode(action.obj.code));
  }
}

function* setUserNameWorker(action) {
  if (action.obj) {
    yield put(actions.setName(action.obj.name));
  }
}

function* signupWorker(action) {
  try {
    const result = yield call(authApiService.signup, action);
    yield put(actions.signupSucceeded(result));
  } catch (err) {
    console.log(err);
    yield put(actions.signupFailed(err));
  }
}

function* signupWatcher() {
  yield takeEvery(types.SIGNUP, signupWorker);
}

function* loginWatcher() {
  yield takeEvery(types.LOGIN, loginWorker);
}

function* setSchoolWatcher() {
  yield takeEvery(types.SET_SCHOOL, setSchoolWorker);
}

function* setUserTypeWatcher() {
  yield takeEvery(types.SET_USER_TYPE, setUserTypeWorker);
}

function* setEmailWatcher() {
  // yield throttle(500, types.SET_EMAIL, setEmailWorker);
  yield takeLatest(types.SET_EMAIL, setEmailWorker);
}

function* setCodeWatcher() {
  yield takeLatest(types.SET_CODE, setCodeWorker);
}

function* setPasswordWatcher() {
  yield throttle(500, types.SET_PASSWORD, setPasswordWorker);
}

function* setParentWatcher() {
  yield throttle(500, types.SET_PARENT_NAME, setParentWorker);
}

function* setUserNameWatcher() {
  yield takeLatest(types.SET_NAME, setUserNameWorker);
}

function* deactivateAccountWorker(action) {
  try {
    // const result = yield call(authApiService.deactivateAccount, action);
    // console.log(result.data);
    yield put(actions.logout(action));
    // yield put(actions.deactivateAccountSucceeded(result.data));
    yield put(actions.deactivateAccountSucceeded({}));
  } catch (err) {
    yield put(actions.deactivateAccountFailed(err));
  }
}

function* deactivateAccountWatcher() {
  yield takeEvery(types.DEACTIVATE_ACCOUNT, deactivateAccountWorker);
}

function* logoutWorker(action) {
  try {
    const result = yield call(authApiService.logout, action);
    console.log(result);
    yield call(storeAccessToken, '');
    yield put(actions.logoutSucceeded(result.data));
  } catch (err) {
    yield put(actions.logoutFailed(err));
  }
}

function* logoutWatcher() {
  yield takeEvery(types.LOG_OUT, logoutWorker);
}

// Read more information about root sagas in the documentation
// https://redux-saga.js.org/docs/advanced/RootSaga.html
export default function* authRootSaga() {
  const sagas = [
    // Example watcher
    // getBalanceWatcher
    loginWatcher,
    setSchoolWatcher,
    setUserTypeWatcher,
    setEmailWatcher,
    setPasswordWatcher,
    setParentWatcher,
    setCodeWatcher,
    setUserNameWatcher,
    signupWatcher,
    deactivateAccountWatcher,
    logoutWatcher,
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
