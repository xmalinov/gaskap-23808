import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';
import Dialog from 'react-native-dialog';

import {styles} from './styles';
import * as actions from '../../../../../store/auth/constants';
import * as customActions from '../../../../../store/custom/constants';
import {settingItems} from '../../../../../constants/generalConstants';
import SimpleToast from 'react-native-simple-toast';
import {Loader} from '../../../../../components/Loader';
import {authMessage, general_message} from '../../../../../constants/message';

class Settings extends Component {
  state = {
    settingListItems: [
      {title: settingItems.changePassword, iconName: 'user', value: 'password'},
      {title: settingItems.changeEmail, iconName: 'user', value: 'email'},
      {title: settingItems.changePhone, iconName: 'user', value: 'phoneNumber'},
      {
        title: settingItems.deactivateAccount,
        iconName: 'user',
        value: 'deactivateAccount',
      },
      {
        title: settingItems.logout,
        iconName: 'user',
        // value: this.props.user.profile.city,
      },
    ],

    showChangePassword: false,
    showChangeEmail: false,
    showChangePhone: false,
    showDeactivateAccount: false,
    showLogout: false,

    oldPassword: '',
    newPassword: '',
    repeatPassword: '',

    email: '',
    phoneNumber: '',
  };

  getList = itemList => {
    return itemList.map((item, index) => {
      return (
        <ListItem
          key={index}
          bottomDivider
          onPress={() => this.handleItemClick(item)}
        >
          <Avatar
            rounded
            icon={{name: item.iconName, type: 'font-awesome-5', color: 'black'}}
            containerStyle={styles.itemIcon}
          />
          <ListItem.Content>
            <ListItem.Title style={styles.listTitle}>
              {item.title}
            </ListItem.Title>
          </ListItem.Content>
          <ListItem.Chevron />
        </ListItem>
      );
    });
  };

  handleItemClick = item => {
    // this.props.navigation.push(ScreenConstants.profileUpdate, {
    //   item: item,
    // });
    switch (item.title) {
      case settingItems.changePassword:
        this.setState({showChangePassword: true});
        break;
      case settingItems.changeEmail:
        this.setState({showChangeEmail: true});
        break;
      case settingItems.changePhone:
        this.setState({showChangePhone: true});
        break;
      case settingItems.deactivateAccount:
        this.setState({showDeactivateAccount: true});
        break;
      case settingItems.logout:
        console.log(item);
        this.setState({showLogout: true});
        break;
    }
  };

  handleConfirmPasswordChange = () => {
    const {oldPassword, newPassword, repeatPassword} = this.state;

    if (newPassword === repeatPassword) {
      const params = {
        old_password: oldPassword,
        new_password1: newPassword,
        new_password2: repeatPassword,
      };

      this.props.changePassword(params);
    } else {
      SimpleToast.show('Password not same');
    }
  };

  handleConfirmEmailChange = () => {
    this.setState({showChangeEmail: false}, () => {
      if (this.state.email === '') {
        SimpleToast.show(authMessage.noEmail);
      } else {
        this.props.updateUser({email: this.state.email});
      }
    });
  };

  handleChangePhone = () => {
    this.setState({showChangePhone: false}, () => {
      if (this.state.phoneNumber === '') {
        SimpleToast.show(general_message.enterPhone);
      } else {
        this.props.updateProfile({phone_number: this.state.phoneNumber});
      }
    });
  };

  handleDeactivateAccount = () => {
    this.setState({showDeactivateAccount: false}, () => {
      // this.props.updateUser({is_active: false});
      this.props.deactivateAccount({is_active: false});
    });
  };

  changePasswordDialog = () => {
    return (
      <View>
        <Dialog.Container visible={this.state.showChangePassword}>
          <Dialog.Title>{settingItems.changePassword}</Dialog.Title>
          <Dialog.Description>
            Enter old and new password below.
          </Dialog.Description>
          <Dialog.Input
            autoCapitalize="none"
            value={this.state.oldPassword}
            secureTextEntry
            onChangeText={value => this.setState({oldPassword: value})}
            placeholder="Old passsword"
          />
          <Dialog.Input
            autoCapitalize="none"
            secureTextEntry
            value={this.state.newPassword}
            onChangeText={value => this.setState({newPassword: value})}
            placeholder="New passsword"
          />
          <Dialog.Input
            autoCapitalize="none"
            secureTextEntry
            value={this.state.repeatPassword}
            onChangeText={value => this.setState({repeatPassword: value})}
            placeholder="Confirm passsword"
          />
          <Dialog.Button
            onPress={() => this.setState({showChangePassword: false})}
            label="Cancel"
          />
          <Dialog.Button
            onPress={this.handleConfirmPasswordChange}
            label="Confirm"
          />
        </Dialog.Container>
      </View>
    );
  };

  changeEmailDialog = () => {
    return (
      <View>
        <Dialog.Container visible={this.state.showChangeEmail}>
          <Dialog.Title>{settingItems.changeEmail}</Dialog.Title>
          <Dialog.Description>
            Check your email for verification.
          </Dialog.Description>
          <Dialog.Input
            autoCapitalize="none"
            onChangeText={value => this.setState({email: value})}
            placeholder={this.props.user.email}
          />
          <Dialog.Button
            onPress={() => this.setState({showChangeEmail: false})}
            label="Cancel"
          />
          <Dialog.Button
            onPress={this.handleConfirmEmailChange}
            label="Confirm"
          />
        </Dialog.Container>
      </View>
    );
  };

  changePhoneDialog = () => {
    return (
      <View>
        <Dialog.Container visible={this.state.showChangePhone}>
          <Dialog.Title>{settingItems.changePhone}</Dialog.Title>
          <Dialog.Description>
            Make sure you enter valid phone number.
          </Dialog.Description>
          <Dialog.Input
            keyboardType="number-pad"
            autoCapitalize="none"
            onChangeText={value => this.setState({phoneNumber: value})}
            placeholder={
              this.props.user.profile.phone_number || 'Input phone number'
            }
          />
          <Dialog.Button
            onPress={() => this.setState({showChangePhone: false})}
            label="Cancel"
          />
          <Dialog.Button onPress={this.handleChangePhone} label="Confirm" />
        </Dialog.Container>
      </View>
    );
  };

  deactivateDialog = () => {
    return (
      <View>
        <Dialog.Container visible={this.state.showDeactivateAccount}>
          <Dialog.Title>{settingItems.deactivateAccount}</Dialog.Title>
          <Dialog.Description>
            Are you sure you want to deactivate account?
          </Dialog.Description>
          <Dialog.Button
            label="No"
            onPress={() => this.setState({showDeactivateAccount: false})}
          />
          <Dialog.Button label="Yes" onPress={this.handleDeactivateAccount} />
        </Dialog.Container>
      </View>
    );
  };

  logoutDialog = () => {
    console.log(this.state.showLogout);
    return (
      <View>
        <Dialog.Container visible={this.state.showLogout}>
          <Dialog.Title>{settingItems.logout}</Dialog.Title>
          <Dialog.Description>Do you really want to logout?</Dialog.Description>
          <Dialog.Button
            label="No"
            onPress={() => this.setState({showLogout: false})}
          />
          <Dialog.Button label="Yes" onPress={() => this.props.logout()} />
        </Dialog.Container>
      </View>
    );
  };

  render() {
    const {isMakingNetworkRequest, isRequesting} = this.props;

    if (isMakingNetworkRequest || isRequesting) {
      return <Loader size="large" />;
    }

    return (
      <ScrollView style={styles.wrapper}>
        <View style={styles.container}>
          <View style={styles.listWrapper}>
            {this.getList(this.state.settingListItems)}
            {this.changePasswordDialog()}
            {this.changeEmailDialog()}
            {this.changePhoneDialog()}
            {this.deactivateDialog()}
            {this.logoutDialog()}
          </View>
        </View>
      </ScrollView>
    );
  }
}

const mapStateToProps = state => {
  return {
    user: state.customReducer.profile,
    settingsError: state.customReducer.settingsError,
    isMakingNetworkRequest: state.customReducer.isMakingNetworkRequest,
    isRequesting: state.authReducer.isMakingNetworkRequest,
    userUpdateFailed: state.customReducer.userUpdateFailed,
    deactivationFailed: state.customReducer.deactivationFailed,
  };
};
const mapDispToProps = dispatch => ({
  updateProfile: obj => dispatch({type: customActions.UPDATE_PROFILE, obj}),
  updateUser: obj => dispatch({type: customActions.UPDATE_USER, obj}),
  deactivateAccount: obj => dispatch({type: actions.DEACTIVATE_ACCOUNT, obj}),
  logout: obj => dispatch({type: actions.LOG_OUT, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Settings);
