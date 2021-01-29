import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon, SearchBar} from 'react-native-elements';
import * as chatActions from './../../store/chat/constants'

import {styles} from './styles';
import {SafeAreaView} from 'react-native';

const userLists = [
  {
    title: 'User 1',
    message: 'This is the recent Message ',
  },
  {
    title: 'User 2',
    message: 'This is the recent Message ',
  },
  {
    title: 'User 3',
    message: 'This is the recent Message ',
  },
  {
    title: 'User 4',
    message: 'This is the recent Message ',
  },
  {
    title: 'User 5',
    message: 'This is the recent Message ',
  },
  {
    title: 'User 6',
    message: 'This is the recent Message ',
  },
];

class ChatScreen extends Component {
  state = {
    selectedIndex: 0,
    searchTerm: '',
    isSearchActive: false,
  };

  updateSearchTerm = search => {
    this.setState({searchTerm: search});
  };

  handleListItemClick = item => {
    console.log(item.title);
  };

  getList = list => {
    return list.map((item, index) => {
      return (
        <ListItem
          key={index}
          bottomDivider
        // onPress={() => props.handleItemClick(item)}
        >
          <Avatar
            rounded
            icon={{name: 'user', type: 'font-awesome-5', color: 'black'}}
            containerStyle={styles.itemIcon}
          />
          <ListItem.Content>
            <ListItem.Title style={styles.listTitle}>
              {item.title}
            </ListItem.Title>
            <ListItem.Subtitle style={styles.subtitle}>
              {item.message}
            </ListItem.Subtitle>
          </ListItem.Content>
          <ListItem.Chevron />
        </ListItem>
      );
    });
  };

  render() {
    return (
      <SafeAreaView style={styles.wrapper}>
        <View style={styles.headerContainer}>
          <SearchBar
            round
            placeholder="Search"
            onChangeText={this.updateSearch}
            value={this.state.searchTerm}
            showCancel={true}
            showLoading={this.state.isSearchActive}
            lightTheme={true}
            containerStyle={styles.searchContainer}
            inputContainerStyle={styles.searchInput}
          />
        </View>
        <ScrollView>{this.getList(userLists)}</ScrollView>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = state => {
  return {
    users: state.chatReducer.users,
  };
};
const mapDispToProps = dispatch => ({
  getAllUsers: obj => dispatch({type: chatActions.GET_USERS, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(ChatScreen);
