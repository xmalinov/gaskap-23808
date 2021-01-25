import {first} from 'lodash';

export const request_methods = {
  post: 'POST',
  get: 'GET',
  put: 'PUT',
  patch: 'PATCH',
};

export const end_points = {
  login: '/api/v1/auth/login/',
  signup: '/api/v1/auth/registration/',
  allSchools: '/api/v1/schools/',
  profile: '/api/v1/auth/user/',
  changePassword: '/api/v1/auth/password/change/',
  changeEmail: '/api/v1/auth/user/',
  changePhone: '/api/v1/auth/user/',
  updateProfile: '/api/v1/users/profile/me/',
  updateUser: '/api/v1/auth/user/',
  deactivateAccount: '/api/v1/auth/logout/',
  logout: '/api/v1/auth/logout/',
  sendConfirmationEmail: '/auth/email-confirmation/send/',
};

export const userTypes = {
  teacher: 'Teacher',
  parent: 'Parent',
  student: 'Student',
};

export const keys = {
  accessToken: 'access_token',
  date_format: 'yyyy-MM-dd',
};

export const settingItems = {
  changePassword: 'Change Password',
  changeEmail: 'Change Email',
  changePhone: 'Change Phone #',
  deactivateAccount: 'Deactivate Account',
  logout: 'Log out',
};

export const profileItems = {
  studentId: 'Student ID',
  schoolId: 'School ID#',
  grade: 'Grade',
  age: 'Date of Birth',
  city: 'City',
  state: 'State',
  classAssigned: 'Classes Assigned',
};

export const grades = {
  kindergarten: 'kindergarten',
  first: 'first',
  second: 'second',
  third: 'third',
  fourth: 'fourth',
  fifth: 'fifth',
  sixth: 'sixth',
  seventh: 'seventh',
  eight: 'eight',
  freshman: 'freshman',
  sophomore: 'sophomore',
  junior: 'junior',
  senior: 'senior',
};
