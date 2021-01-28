import React, {Component, createRef} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {
  Avatar,
  ListItem,
  Image,
  Icon,
  BottomSheet,
} from 'react-native-elements';
import _ from 'lodash';

import {styles} from './styles';
import * as actions from '../../../../../store/auth/constants';
import * as customActions from '../../../../../store/custom/constants';
import ScreenConstants from '../../../../../constants/screenConstants';
import {
  profileItems,
  userTypes,
} from '../../../../../constants/generalConstants';
import SimpleToast from 'react-native-simple-toast';
import {authMessage} from '../../../../../constants/message';
import Dialog from 'react-native-dialog';
import {Loader} from '../../../../../components/Loader';
import {launchCamera, launchImageLibrary} from 'react-native-image-picker';
import {ActivityIndicator} from 'react-native';

class Profile extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showUserDialog: false,
      name: '',
      isSheetVisible: false,
    };

    this.list = [
      {
        title: 'Take Photo',
        onPress: () =>
          launchCamera(
            {
              mediaType: 'photo',
              includeBase64: false,
              maxHeight: 200,
              maxWidth: 200,
            },
            response => {
              console.log(response);
              const formdata = new FormData();
              formdata.append('profile_picture', {
                uri: response.uri,
                name: response.fileName,
                type: 'image/jpeg',
              });
              console.log(response);
              // setResponse(response);
              this.setState({isSheetVisible: false});
              this.props.uploadPhoto(formdata);
            },
          ),
      },
      {
        title: 'Choose From Library',
        onPress: () => {
          // this.setState({isSheetVisible: false},()=>{

          // });

          launchImageLibrary(
            {
              mediaType: 'photo',
              includeBase64: false,
              maxHeight: 200,
              maxWidth: 200,
            },
            response => {
              const formdata = new FormData();
              formdata.append('profile_picture', {
                uri: response.uri,
                name: response.fileName,
                type: 'image/jpeg',
              });
              console.log(response);
              // setResponse(response);
              this.setState({isSheetVisible: false});
              this.props.uploadPhoto(formdata);
            },
          );
        },
      },
      {
        title: 'Cancel',
        containerStyle: {},
        titleStyle: {color: 'red'},
        onPress: () => this.setState({isSheetVisible: false}),
      },
    ];
  }

  getList = itemList => {
    return itemList.map((item, index) => {
      return (
        <ListItem
          key={index}
          bottomDivider
          onPress={() => this.handleItemClick(item)}>
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
        <Dialog.Container visible={this.state.showUserDialog}>
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

  getProfileImage = () => {
    const isProfileEmpty = _.isEmpty(this.props.profile);
    if (!isProfileEmpty && this.props.profile.profile.profile_picture) {
      return (
        <Avatar
          size={'xlarge'}
          rounded
          source={{uri: this.props.profile.profile.profile_picture}}
          onPress={() => {
            this.setState({isSheetVisible: true});
          }}
          renderPlaceholderContent={<ActivityIndicator color="white" />}
          activeOpacity={0.7}
          containerStyle={styles.profilePhoto}
        />
      );
    } else {
      return (
        <Avatar
          size={'xlarge'}
          rounded
          icon={{name: 'user', type: 'font-awesome', color: 'black'}}
          onPress={() => {
            this.setState({isSheetVisible: true});
          }}
          activeOpacity={0.7}
          containerStyle={styles.profilePhoto}
        />
      );
    }
  };

  render() {
    if (this.props.isMakingNetworkRequest || _.isEmpty(this.props.profile)) {
      return <Loader size="large" />;
    }

    return (
      <ScrollView style={styles.wrapper}>
        <View style={styles.container}>
          {this.updateDialog()}
          {this.getProfileImage()}
          <Text
            onPress={() => {
              this.setState({showUserDialog: true});
            }}
            style={styles.userName}>
            {this.props.profile && this.props.profile.name}
          </Text>

          <View style={styles.listWrapper}>
            {this.getList(this.props.profileListItems)}
          </View>
          <BottomSheet
            isVisible={this.state.isSheetVisible}
            containerStyle={{backgroundColor: 'rgba(0.5, 0.25, 0, 0.3)'}}>
            {this.list.map((l, i) => (
              <ListItem
                key={i}
                containerStyle={l.containerStyle}
                onPress={l.onPress}
                bottomDivider>
                <ListItem.Content style={{alignItems: 'center'}}>
                  <ListItem.Title style={l.titleStyle}>
                    {l.title}
                  </ListItem.Title>
                </ListItem.Content>
              </ListItem>
            ))}
          </BottomSheet>
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
    profileListItems: state.customReducer.profileItems,
  };
};
const mapDispToProps = dispatch => ({
  updateName: obj => dispatch({type: customActions.UPDATE_USER, obj}),
  uploadPhoto: obj => dispatch({type: customActions.UPDATE_PROFILE_PHOTO, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Profile);
