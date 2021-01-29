import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import * as customActions from './../../../store/custom/constants'
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';

class HomeScreen extends Component {
  state = {};

  componentDidMount() {
    this.props.getProfile();
  }

  render() {
    return (
      <View style={styles.wrapper}>
        <View
          style={[
            styles.container,
            {alignItems: 'center', justifyContent: 'center'},
          ]}>
          <Text>Home screen</Text>
        </View>
      </View>
    );
  }
}

const mapStateToProps = state => {
  return {
    user: state.customReducer.profile,
  };
};
const mapDispToProps = dispatch => ({
  getProfile: obj => dispatch({type: customActions.GET_PROFILE, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(HomeScreen);
