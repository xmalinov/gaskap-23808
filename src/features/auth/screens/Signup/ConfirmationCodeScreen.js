import React, {Component} from 'react';
import {View, Text} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import {Input} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';
import {KeyboardAvoidingView} from 'react-native';

export default class ConfirmationCodeScreen extends Component {
  state = {
    confirmationCode: '',
  };

  handleNext = () => {
    this.props.navigation.navigate(ScreenConstants.addName);
  };

  handleSignin = () => {
    this.props.navigation.reset({
      index: 0,
      routes: [{name: ScreenConstants.login}],
    });
  };

  handleEmailChange = value => {
    console.log(value);
    this.setState({confirmationCode: value});
  };

  handleResendCode = () => {
    console.log('send code');
  };

  render() {
    return (
      <View style={styles.wrapper}>
        <KeyboardAvoidingView style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.confirmationTitle}>
              Enter Confirmation Code
            </Text>
            <Text style={styles.itemConfirmationCode}>
              Enter the confirmation code we sent to (email address).
            </Text>
            <Input
              autoCapitalize='none'
              autoCorrect={false}
              onChangeText={this.handleEmailChange}
              placeholder="Confirmation Code"
              secureTextEntry={true}
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
            <GradientButton
              title="Resend Code"
              onPress={this.handleResendCode}
            // isLoading={true}
            />
            <View style={{marginTop: 10}} />
            <GradientButton
              title="Next"
              onPress={this.handleNext}
            // isLoading={true}
            />
          </View>
        </KeyboardAvoidingView>
        <AuthFooter
          secondaryText={'Sign In.'}
          handleSignin={this.handleSignin}
        />
      </View>
    );
  }
}
