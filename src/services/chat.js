import {end_points, request_methods} from '../constants/generalConstants';
import {requestToServer} from '../utils/http';

const getAllUsers = action => {
  const url = end_points.allUsers;
  const info = {
    url,
    method: request_methods.get,
    params: {school: action.schoolId},
  };

  return requestToServer(info);
};

export const chatApiService = {
  getAllUsers,
};
