import {end_points, request_methods} from '../constants/generalConstants';
import {requestToServer} from '../utils/http';

const getAllSchools = () => {
  const url = end_points.allSchools;
  const info = {
    url,
    method: request_methods.get,
    params: {},
  };

  return requestToServer(info);
};

export const schoolApiService = {
  getAllSchools,
};
