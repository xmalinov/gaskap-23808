import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';
import ScreenConstants from '../../../../constants/screenConstants';

const classLisItems = [
  {
    class: 'Geometry 101',
    taughtBy: 'Mrs. Wrenfield',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'World History',
    taughtBy: 'Mr Goodwyn',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'Cooking Making',
    taughtBy: 'Mrs. Smith Cookies',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'Underwater Basket Weaving',
    taughtBy: 'Uncle Ben',
    location: 'Room',
    iconName: 'user',
  },
];

class Class extends Component {
  state = {};

  getList = itemList => {
    console.log(itemList);

    return itemList.map((item, index) => {
      return (
        <ListItem
          key={index}
          bottomDivider
          onPress={() => this.handleItemClick(item)}
          containerStyle={{paddingHorizontal: 0}}
        >
          <Avatar
            rounded
            icon={{name: item.iconName, type: 'font-awesome-5', color: 'black'}}
            containerStyle={styles.itemIcon}
          />
          <ListItem.Content>
            <ListItem.Title style={styles.listTitle}>
              {`Class: ${ item.class }`}
            </ListItem.Title>
            <ListItem.Subtitle style={styles.subtitle}>
              {`Taught By: ${ item.taughtBy }`}
            </ListItem.Subtitle>
            <ListItem.Subtitle style={styles.subtitle}>
              {`Location: ${ item.location }`}
            </ListItem.Subtitle>
          </ListItem.Content>
        </ListItem>
      );
    });
  };

  handleItemClick = item => {
    this.props.navigation.navigate(ScreenConstants.classDetail, {
      item: item,
    });
  };

  render() {
    return (
      <View style={styles.wrapper}>
        <View style={styles.container}>
          <View style={styles.chatContainer}>
            <Text style={styles.chatTitle}>
              Chat with Administrator to Request a Change
          </Text>
            <Icon
              raised
              name="comment-dots"
              type="font-awesome-5"
              // color='#f50'
              onPress={() => console.log('hello')}
            />
          </View>
          <Text style={styles.header}>Mike Stroke</Text>
          <View>{this.getList(classLisItems)}</View>
        </View>
      </View>
    );
  }
}

const mapStateToProps = state => {
  return {};
};
const mapDispToProps = dispatch => ({});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Class);
