import React, {Component} from 'react';
import {View, Text} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import {Input} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';


import {connect} from 'react-redux';
import * as authActions from '../../../../store/auth/constants';
import {KeyboardAvoidingView} from 'react-native';

class GaurdainScreen extends Component {
  state = {
    name: '',
  };

  handleNext = () => {
    this.props.navigation.navigate(ScreenConstants.password);
  };

  handleSignin = () => {
    this.props.navigation.reset({
      index: 0,
      routes: [{name: ScreenConstants.login}],
    });
  };

  handleNameChange = value => {
    console.log(value);
    this.setState({name: value});
  };

  render() {
    return (
      <View style={styles.wrapper}>
        <KeyboardAvoidingView style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.confirmationTitle}>
              Enter Parent or Guardian Name
            </Text>
            <Text style={styles.itemConfirmationCode}>
              Enter the full name of your parent or legal guardian
            </Text>
            <Input
              autoCapitalize='none'
              autoCorrect={false}
              onChangeText={this.handleNameChange}
              placeholder="First and Last Name"
              secureTextEntry={true}
              inputContainerStyle={styles.itemTextContainer}
              style={styles.itemTextInput}
              errorStyle={styles.errorStyle}
              containerStyle={{paddingHorizontal: 0}}
            />
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

const mapStateToProps = state => {
  return {};
};
const mapDispToProps = dispatch => ({
  addName: obj => dispatch({type: authActions.SET_NAME, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(GaurdainScreen);
