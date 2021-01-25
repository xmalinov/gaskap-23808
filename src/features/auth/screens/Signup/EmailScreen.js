import React, {Component} from 'react';
import {View, Text, Image} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import {Input, Button} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';
import {connect} from 'react-redux';
import * as authActions from '../../../../store/auth/constants';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../../../constants/message';

class EmailScreen extends Component {
  state = {
    email: '',
  };

  handleNext = () => {
    if (this.props.email && this.props.userType != '') {
      this.props.navigation.navigate(ScreenConstants.addName);
    } else {
      SimpleToast.show(authMessage.noEmail);
    }
  };

  handleEmailChange = value => {
    this.props.addEmail({email: value});
  };

  render() {
    return (
      <View style={styles.wrapper}>
        <View style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.titleText}>Enter Email</Text>
            <Input
              autoCapitalize='none'
              autoCorrect={false}
              value={this.props.email}
              onChangeText={this.handleEmailChange}
              placeholder="Email"
              secureTextEntry={false}
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
    email: state.authReducer.email
  };
};
const mapDispToProps = dispatch => ({
  addEmail: obj => dispatch({type: authActions.SET_EMAIL, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(EmailScreen);
