import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {Avatar, ListItem, Icon, SearchBar} from 'react-native-elements';

import {styles} from './styles';

const RandomNews = props => {
  const {itemList} = props;

  return (
    <View>
      <Text>This is a random list view </Text>
    </View>
  );
};

export default RandomNews;
