import React, {Component} from 'react';
import {View, Text} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import {Input, CheckBox} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';
import * as authActions from '../../../../store/auth/constants';
import SimpleToast from 'react-native-simple-toast';
import {connect} from 'react-redux';
import {authMessage} from '../../../../constants/message';

class PasswordScreen extends Component {
  state = {
    password: '',
    checked: false,
  };

  handleRegister = () => {
    const {userName, email, password, userType, code} = this.props;
    console.log(email, '-------');

    const registerParams = {
      name: userName,
      email: email.toLowerCase(),
      password,
      code,
      user_type: userType.toLowerCase(),
      phone_number: '+6144444444'
    }

    if (password) {
      this.props.register(registerParams);
    } else {
      SimpleToast.show(authMessage.noPassword);
    }
  };

  handleSignin = () => {
    this.props.navigation.reset({
      index: 0,
      routes: [{name: ScreenConstants.login}],
    });
  };

  handlePasswordChange = value => {
    this.props.addPassword({password: value});
  };

  componentDidUpdate() {
    // if (this.props.signupError != '') {
    //   SimpleToast.show(this.props.signupError);
    // }
    if (this.props.registrationSuccess) {
      setTimeout(() => {
        this.props.navigation.navigate(ScreenConstants.login);
      }, 500);
    }
  }

  componentDidUpdate() {
    // if (this.props.signupError != '') {
    //   SimpleToast.show(this.props.signupError);
    // }
    if (this.props.registrationSuccess) {
      setTimeout(() => {
        this.props.navigation.navigate(ScreenConstants.login);
      }, 500);
    }
  }

  render() {
    return (
      <View style={styles.wrapper}>
        <View style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.confirmationTitle}>Create a Password</Text>
            <Text style={styles.itemConfirmationCode}>
              Gaskap can remember your password so you won't have to
            </Text>
            <Input
              autoCapitalize='none'
              autoCorrect={false}
              onChangeText={this.handlePasswordChange}
              placeholder="Password"
              secureTextEntry={true}
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
            {/* <CheckBox
              containerStyle={styles.checkBackground}
              title="Save Password"
              checked={this.state.checked}
              onPress={() => {
                this.setState({checked: !this.state.checked});
              }}
            /> */}

            <GradientButton
              title="Register"
              onPress={this.handleRegister}
              isLoading={this.props.isRegisteringUser}
            />
            <Text style={styles.infoTitle}>
              {`Once you register we will send a link on your email (${ this.props.email }) for verification.`}
            </Text>
          </View>
        </View>
        <AuthFooter
          secondaryText={'Sign In.'}
          handleSignin={this.handleSignin}
        />
      </View>
    );
  }
}

const mapStateToProps = state => {
  return {
    email: state.authReducer.email,
    password: state.authReducer.password,
    userType: state.authReducer.userType,
    userName: state.authReducer.userName,
    code: state.authReducer.code,
    isRegisteringUser: state.authReducer.isRegisteringUser,
    signupError: state.authReducer.signupError,
    registrationSuccess: state.authReducer.registrationSuccess
  };
};
const mapDispToProps = dispatch => ({
  addPassword: obj => dispatch({type: authActions.SET_PASSWORD, obj}),
  register: obj => dispatch({type: authActions.SIGNUP, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(PasswordScreen);
