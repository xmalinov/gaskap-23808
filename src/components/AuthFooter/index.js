import React from 'react';
import PropTypes from 'prop-types';

import styles from './styles';
import {Image, Text, View} from 'react-native';
import {images} from '../../constants/images';
import {Button} from 'react-native-elements';

const AuthFooter = props => {
  return (
    <View style={styles.container}>
      <Image source={images.logo} style={styles.itemLogo} />
      <View style={styles.itemFooterWrapper}>
        <Text style={styles.itemFooterText}>{props.primaryText}</Text>
        <Button
          title={props.secondaryText}
          type={props.buttonType}
          titleStyle={styles.itemSignupText}
          onPress={props.handleSignin}
        />
      </View>
    </View>
  );
};

AuthFooter.defaultProps = {
  buttonType: 'clear',
  primaryText: "Don't have an account?",
  secondaryText: '',
};

AuthFooter.prototype = {
  buttonType: PropTypes.string,
  primaryText: PropTypes.string,
  secondaryText: PropTypes.string,
  handleSignin: PropTypes.func,
};

export default AuthFooter;
