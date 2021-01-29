import React, {Component} from 'react';
import {
  KeyboardAvoidingView,
  Keyboard,
  View,
  Text,
  SafeAreaView,
} from 'react-native';
import * as authActions from '../../../../store/auth/constants';
import {Input} from 'react-native-elements';
import {connect} from 'react-redux';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';

class ForgetPassword extends Component {
  state = {
    email: '',
  };

  handleReset = () => {
    this.props.forgetPassword({email: this.state.email});
  };

  componentDidUpdate(prevProps, prevState, snapshot) {
    if (prevProps.passwordResetSuccess !== this.props.passwordResetSuccess) {
      this.props.passwordResetSuccess && this.props.navigation.goBack();
    }
  }

  render() {
    return (
      <SafeAreaView style={styles.wrapper}>
        <KeyboardAvoidingView style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.titleText}>Forget your password?</Text>
            <Text style={styles.itemConfirmationCode}>
              Enter your email address you're using for your account below and
              we will send you a password reset link
            </Text>
            <Input
              autoCapitalize="none"
              autoCorrect={false}
              onChangeText={value => {
                this.setState({email: value});
              }}
              placeholder="Enter email address"
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
            <GradientButton
              title="Request Reset Link"
              onPress={this.handleReset}
              isLoading={this.props.isMakingNetworkRequest}
            />
          </View>
        </KeyboardAvoidingView>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = state => {
  return {
    isMakingNetworkRequest: state.authReducer.isMakingNetworkRequest,
    passwordResetSuccess: state.authReducer.passwordResetSuccess,
  };
};

const mapDispToProps = dispatch => ({
  forgetPassword: obj => dispatch({type: authActions.FORGET_PASSWORD, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(ForgetPassword);
