import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {Avatar, ListItem, Icon, SearchBar} from 'react-native-elements';
import ScreenConstants from '../../../../constants/screenConstants';

import {styles} from './styles';

const ListEvents = props => {
  const {itemList} = props;

  const getList = list => {
    return list.map((item, index) => {
      return (
        <ListItem
          key={index}
          bottomDivider
          onPress={() => props.handleItemClick(item)}
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
              {item.description}
            </ListItem.Subtitle>
            <ListItem.Subtitle style={styles.subtitle}>
              {item.location}
            </ListItem.Subtitle>
          </ListItem.Content>
          <ListItem.Chevron />
        </ListItem>
      );
    });
  };

  return <View>{getList(itemList)}</View>;
};

export default ListEvents;
