import React, {Component} from 'react';
import {View, Text} from 'react-native';

import {styles} from './styles';
import GradientButton from '../../../../components/GradientButton';
import Picker from '../../../../components/Picker';
import ScreenConstants from '../../../../constants/screenConstants';
import AuthFooter from '../../../../components/AuthFooter';
import {connect} from 'react-redux';
import * as authActions from '../../../../store/auth/constants';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../../../constants/message';
import {Input, Button} from 'react-native-elements';
import {userTypes} from '../../../../constants/generalConstants';

const userList = [
  {
    label: userTypes.teacher,
    value: userTypes.teacher,
  },
  {
    label: userTypes.parent,
    value: userTypes.parent,
  },
  {
    label: userTypes.student,
    value: userTypes.student,
  },
];

const placeHolderText = {
  Teacher: 'Enter teacher code',
  Parent: 'Enter student id',
  Student: 'Enter student code',
}

class Signup extends Component {
  state = {
    school: '',
    schools: [],
    selectedValue: 'java'
  };

  handleNext = () => {
    if (this.props.userType != '' && this.props.code != '') {
      this.props.navigation.navigate(ScreenConstants.email);
    } else {
      const message = this.props.userType ? authMessage.noCode : authMessage.noUserType

      SimpleToast.show(message);
    }
  };

  handleSignin = () => {
    this.props.navigation.goBack();
  };

  getFormattedSchool = () => {
    let schools = [];

    if (this.props.schools) {
      schools = this.props.schools.map(item => {
        return {label: item.name, value: item.number};
      });
    }

    return schools;
  };

  componentDidMount() {
    // const formattedSchools = this.getFormattedSchool();

    // this.setState({schools: formattedSchools});
  }

  handleUserTypeSelect = item => {
    this.props.addUserType({selectedUserType: item.value});
  };

  handleCodeChange = value => {
    this.props.addCode({code: value});
  };

  render() {
    const {userType} = this.props;

    return (
      <View style={styles.wrapper}>
        <View style={styles.container}>
          <View style={styles.itemsContainer}>
            <Text style={styles.titleText}>Select User</Text>
            <Picker
              // items={this.props.schools}
              defaultValue={this.props.userType}
              placeHolder="Select user type"
              items={userList}
              onChangeItem={
                item => {
                  this.handleUserTypeSelect(item);
                }
                // this.props.addSchool({selectedSchool: item})
              }
            />
            {
              userType != '' &&
              <Input
                autoCapitalize='none'
                autoCorrect={false}
                value={this.props.code}
                onChangeText={this.handleCodeChange}
                placeholder={placeHolderText[this.props.userType]}
                secureTextEntry={false}
                inputContainerStyle={styles.itemTextContainer}
                style={styles.itemTextInput}
                errorStyle={styles.errorStyle}
                containerStyle={{paddingHorizontal: 0}}
              />
            }

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
    users: state.customReducer.users,
    userType: state.authReducer.userType,
    code: state.authReducer.code,
  };
};
const mapDispToProps = dispatch => ({
  addSchool: obj => dispatch({type: authActions.SET_SCHOOL, obj}),
  addUserType: obj => dispatch({type: authActions.SET_USER_TYPE, obj}),
  addCode: obj => dispatch({type: authActions.SET_CODE, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Signup);
