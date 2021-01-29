import React, {Component} from 'react';
import {View, Text} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import {Input} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';
import {connect} from 'react-redux';
import * as authActions from '../../../../store/auth/constants';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../../../constants/message';
import {userTypes} from '../../../../constants/generalConstants';
import {KeyboardAvoidingView} from 'react-native';

class NameScreen extends Component {
  state = {
    name: '',
  };

  handleNext = () => {
    if (this.props.userName != '') {
      // this.props.navigation.navigate(ScreenConstants.guardain);
      this.props.navigation.navigate(ScreenConstants.password);
    } else {
      SimpleToast.show(authMessage.noName);
    }
  };

  handleNameChange = value => {
    this.props.addName({name: value});
  };

  handleSignin = () => {
    this.props.navigation.reset({
      index: 0,
      routes: [{name: ScreenConstants.login}],
    });
  };

  render() {
    return (
      <View style={styles.wrapper}>
        <KeyboardAvoidingView style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.confirmationTitle}>Add Your Name</Text>
            <Text style={styles.itemConfirmationCode}>
              Add your name so your others can find you.
            </Text>
            <Input
              autoCapitalize='none'
              autoCorrect={false}
              value={this.props.userName}
              onChangeText={this.handleNameChange}
              placeholder="First and Last Name"
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
  return {
    userName: state.authReducer.name,
    userType: state.authReducer.userType
  };
};
const mapDispToProps = dispatch => ({
  addName: obj => dispatch({type: authActions.SET_NAME, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(NameScreen);
