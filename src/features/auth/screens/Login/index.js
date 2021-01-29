import React, {Component} from 'react';
import {
  KeyboardAvoidingView,
  Keyboard,
  View,
  Image,
  Text,
  SafeAreaView,
} from 'react-native';
import {Input, Button, CheckBox} from 'react-native-elements';
import GradientButton from '../../../../components/GradientButton';
import {images} from '../../../../constants/images';
import ScreenConstants from '../../../../constants/screenConstants';
import {connect} from 'react-redux';

import {styles} from './styles';
import * as authActions from '../../../../store/auth/constants';
import * as customActions from '../../../../store/custom/constants';
import SimpleToast from 'react-native-simple-toast';
import AuthFooter from '../../../../components/AuthFooter';
import {authMessage} from '../../../../constants/message';

class Login extends Component {
  state = {
    email: '',
    password: '',
    checked: false,
  };

  componentDidMount = async () => {
    // try {
    //   this.props.getSchools();
    // } catch (error) {
    //   SimpleToast.show(error.message);
    // }
  };

  componentDidUpdate() {
    // if (this.props.loginSuccess) {
    //   setTimeout(() => {
    //     this.props.navigation.navigate(ScreenConstants.home, {
    //       screen: ScreenConstants.home,
    //     });
    //   }, 500);
    // }
  }

  handleEmailChange = value => {
    this.setState({email: value});
  };

  handlePasswordChange = value => {
    this.setState({password: value});
  };

  handleSignup = () => {
    this.props.navigation.navigate(ScreenConstants.signUp);
  };

  handleLogin = () => {
    if (this.state.email === '') {
      SimpleToast.show(authMessage.noEmail);
    } else if (this.state.password === '') {
      SimpleToast.show(authMessage.noPassword);
    } else {
      this.props.login({
        email: this.state.email,
        password: this.state.password,
      });
    }
    // this.props.navigation.navigate(ScreenConstants.home);
    // this.props.navigation.navigate(ScreenConstants.home, {
    //   screen: ScreenConstants.home,
    // });
  };

  handleForgetpassword = () => {
    this.props.navigation.navigate(ScreenConstants.forgetPassword);
  };

  render() {
    return (
      <SafeAreaView style={styles.wrapper}>
        <View onTouchStart={() => Keyboard.dismiss()} style={styles.container}>
          <KeyboardAvoidingView style={styles.itemsContainer}>
            <Image source={images.slogan} style={styles.itemSlogan} />
            <Input
              autoCapitalize="none"
              autoCorrect={false}
              onChangeText={this.handleEmailChange}
              placeholder="Email"
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
            <Input
              autoCapitalize="none"
              autoCorrect={false}
              onChangeText={this.handlePasswordChange}
              placeholder="Password"
              secureTextEntry={true}
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
            <CheckBox
              containerStyle={styles.checkBackground}
              title="Save Password"
              checked={this.state.checked}
              onPress={() => {
                this.setState({checked: !this.state.checked});
              }}
            />
            <View style={styles.forgetPasswordContainer}>
              <Button
                title="Forget Password?"
                type="clear"
                titleStyle={styles.forgetPasswordTitle}
                onPress={this.handleForgetpassword}
              />
            </View>
            <GradientButton
              title="Login"
              onPress={this.handleLogin}
              isLoading={this.props.isLoggingIn}
            />
          </KeyboardAvoidingView>
        </View>
        <View style={styles.itemFooterWrappe}>
          <Text style={styles.itemFooterText}>Don't have an account?</Text>
          <Button
            title="Sign Up."
            type="clear"
            titleStyle={styles.itemSignupText}
            onPress={this.handleSignup}
          />
        </View>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = state => {
  return {
    auth: state.authReducer.auth,
    loginSuccess: state.authReducer.loginSuccess,
    loginError: state.authReducer.loginError,
    isLoggingIn: state.authReducer.isLoggingIn,
    loginResult: state.authReducer.loginResult,
  };
};
const mapDispToProps = dispatch => ({
  login: obj => dispatch({type: authActions.LOGIN, obj}),
  getSchools: obj => dispatch({type: customActions.GET_SCHOOLS, obj}),
  forgetPassword: obj => dispatch({type: authActions.GET_SCHOOLS, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Login);
