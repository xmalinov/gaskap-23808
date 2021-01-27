import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';
class Profile extends Component {
  state = {};

  render() {
    return (
      <View style={styles.wrapper}>
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
)(Profile);
