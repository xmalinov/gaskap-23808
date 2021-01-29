import * as types from './constants';

export const getUsers = params => ({
  type: types.GET_USERS,
  params,
});

export const getUsersSucceeded = response => ({
  type: types.GET_USERS_SUCCEEDED,
  data: response.data,
});

export const getUsersFailed = error => ({
  type: types.GET_USERS_FAILED,
  error,
});

export const getThreads = params => ({
  type: types.GET_THREADS,
  params,
});

export const getThreadsSucceeded = response => ({
  type: types.GET_THREADS_SUCCEEDED,
  data: response.data,
});

export const getThreadsFailed = error => ({
  type: types.GET_THREADS_FAILED,
  error,
});

export const createThreads = params => ({
  type: types.CREATE_THREADS,
  params,
});

export const createThreadsSucceeded = response => ({
  type: types.CREATE_THREADS_SUCCEEDED,
  data: response.data,
});

export const createThreadsFailed = error => ({
  type: types.CREATE_THREADS_FAILED,
  error,
});
