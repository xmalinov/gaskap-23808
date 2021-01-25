import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';
import * as actions from '../../../../../store/auth/constants';
import * as customActions from '../../../../../store/custom/constants';
import ScreenConstants from '../../../../../constants/screenConstants';
import {profileItems} from '../../../../../constants/generalConstants';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../../../../constants/message';
import Dialog from 'react-native-dialog';
import {Loader} from '../../../../../components/Loader';

class Profile extends Component {
  state = {
    profileLisItems: [
      {
        title: profileItems.studentId,
        iconName: 'user',
        isEditable: false,
      },
      {
        title: profileItems.schoolId,
        iconName: 'school',
        isEditable: false,
      },
      {
        title: profileItems.grade,
        iconName: 'user',
        isEditable: true,
      },
      {
        title: profileItems.age,
        iconName: 'user',
        isEditable: true,
      },
      {
        title: profileItems.city,
        iconName: 'home',
        isEditable: true,
      },
      {
        title: profileItems.state,
        iconName: 'home',
        isEditable: true,
      },
      {
        title: profileItems.classAssigned,
        iconName: 'book-open',
        isEditable: false,
      },
    ],
    showUserDialog: false,
    name: '',
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
    this.props.navigation.push(ScreenConstants.profileUpdate, {
      item: item,
    });
  };

  handleUpdateConfirm = () => {
    this.setState({showUserDialog: false}, () => {
      const userName = this.state.name;

      if (userName === '') {
        SimpleToast.show(authMessage.noName);
      } else {
        this.props.updateName({name: userName});
      }
    });
  };

  updateDialog = () => {
    return (
      <View>
        <Dialog.Container
          visible={this.state.showUserDialog || this.props.profileUpdateFailed}
        >
          <Dialog.Title>{'Change User Name'}</Dialog.Title>
          <Dialog.Description>{'Enter new username'}</Dialog.Description>
          <Dialog.Input
            autoCapitalize="none"
            onChangeText={value => this.setState({name: value})}
            placeholder={this.props.profile && `${this.props.profile.name}`}
          />
          <Dialog.Button
            onPress={() => this.setState({showUserDialog: false})}
            label="Cancel"
          />
          <Dialog.Button onPress={this.handleUpdateConfirm} label="Confirm" />
        </Dialog.Container>
      </View>
    );
  };

  render() {
    if (this.props.isMakingNetworkRequest) {
      return <Loader size="large" />;
    }

    return (
      <ScrollView style={styles.wrapper}>
        <View style={styles.container}>
          {this.updateDialog()}
          <Avatar
            size={'xlarge'}
            rounded
            icon={{name: 'user', type: 'font-awesome', color: 'black'}}
            onPress={() => console.log('Works!')}
            activeOpacity={0.7}
            containerStyle={styles.profilePhoto}
          />
          <Text
            onPress={() => {
              this.setState({showUserDialog: true});
            }}
            style={styles.userName}
          >
            {this.props.profile && this.props.profile.name}
          </Text>

          <View style={styles.listWrapper}>
            {this.getList(this.state.profileLisItems)}
          </View>
        </View>
      </ScrollView>
    );
  }
}

const mapStateToProps = state => {
  return {
    profile: state.customReducer.profile,
    isMakingNetworkRequest: state.customReducer.isMakingNetworkRequest,
    profileUpdateFailed: state.customReducer.profileUpdateFailed,
  };
};
const mapDispToProps = dispatch => ({
  updateName: obj => dispatch({type: customActions.UPDATE_USER, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Profile);
