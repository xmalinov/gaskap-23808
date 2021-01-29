import {Dimensions} from 'react-native';
import {general_message} from '../constants/message';

export default function generalUtils() { }

generalUtils.isPortrait = () => {
  const dim = Dimensions.get('screen');
  return dim.height >= dim.width;
};

/**
 * Return a timer for video from< time in seconds
 * ~~ is used as faster substitute for Math.floor() function
 * https://stackoverflow.com/questions/5971645/what-is-the-double-tilde-operator-in-javascript
 * @param time
 * @returns {string}
 */
generalUtils.secondToTime = time => {
  return ~~(time / 60) + ':' + (time % 60 < 10 ? '0' : '') + (time % 60);
};

generalUtils.normalizeSeconds = number => {
  let sec_num = parseInt(number, 10); // don't forget the second param
  let hours = Math.floor(sec_num / 3600);
  let minutes = Math.floor((sec_num - hours * 3600) / 60);
  let seconds = sec_num - hours * 3600 - minutes * 60;

  if (hours < 10) {
    hours = '0' + hours;
  }
  if (minutes < 10) {
    minutes = '0' + minutes;
  }
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  return hours + ':' + minutes + ':' + seconds;
};

generalUtils.parseErrorMessage = err => {
  const errorKey = Object.keys(err)[0];
  const errorMessage = Array.isArray(err) ? err[errorKey][0] : err[errorKey];

  return typeof errorMessage === 'string'
    ? errorMessage
    : general_message.something_wrong;
};

generalUtils.isValidEmail = mail => {
  return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
    mail,
  );
};
