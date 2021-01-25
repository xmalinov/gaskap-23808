import React, {Component} from 'react';
import {
  ScrollView,
} from 'react-native';
import {styles} from './styles';

export default class App extends Component {
  static navigationOptions = {
    title: 'Installed blueprints',
  };

  render() {
    return (
      <ScrollView contentContainerStyle={styles.itemsContainer}>
        <></>
      </ScrollView>
    );
  }
}
