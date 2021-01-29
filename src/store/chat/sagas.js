import {put, call, all, spawn, takeEvery} from 'redux-saga/effects';
import {apiService} from './services';
import * as types from './constants';
import * as actions from './actions';
import {chatApiService} from '../../services/chat';

function* getUsersWorker(action) {
  try {
    const result = yield call(chatApiService.getAllUsers, action);
    yield put(actions.getUsersSucceeded(result));
  } catch (err) {
    yield put(actions.getUsersFailed(err));
  }
}

function* getUsersWatcher() {
  yield takeEvery(types.GET_SCHOOLS, getUsersWorker);
}

export default function* rootSaga() {
  const sagas = [
    // Example watcher
    getUsersWatcher,
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
