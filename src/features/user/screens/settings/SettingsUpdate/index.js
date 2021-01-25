import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';

class ProfileUpdate extends Component {
  state = {};

  render() {
    const {item} = this.props.route.params;

    return (
      <View style={styles.wrapper}>
        <ListItem bottomDivider>
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
          <ListItem.Content>
            <ListItem.Title style={styles.listTitle}>
              {item.value}
            </ListItem.Title>
          </ListItem.Content>
          <Icon
            // raised
            size={16}
            name="edit"
            type="font-awesome-5"
            // color='#f50'
            onPress={() => console.log('hello')}
          />
        </ListItem>
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
)(ProfileUpdate);
