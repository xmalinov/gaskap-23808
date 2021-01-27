import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';

import {styles} from './styles';
import ScreenConstants from '../../../../constants/screenConstants';
import DetailCard from '../../../../components/DetailCard';

class Class extends Component {
  state = {};

  handleShare = () => { };

  handleLike = () => { };

  getFooterView = item => {
    return (
      <View style={styles.footerView}>
        <Icon
          raised
          // size={18}
          name="thumbs-up"
          type="font-awesome-5"
          // color='#ffffff'
          onPress={this.handleLike}
        />
        <Icon
          raised
          // size={18}
          name="share-square"
          type="font-awesome-5"
          // color='#ffffff'
          onPress={this.handleShare}
        />
        <View style={{height: '100%', width: '100%'}}>
          <ListItem
            // bottomDivider
            onPress={() => this.handleItemClick(item)}
            containerStyle={{paddingHorizontal: 0, }}
          >
            <ListItem.Content>
              <ListItem.Title style={styles.listTitle}>
                {`Class: ${ item.class }`}
              </ListItem.Title>
              <ListItem.Subtitle style={styles.subtitle}>
                {`Full description of class`}
              </ListItem.Subtitle>
              <ListItem.Subtitle style={styles.subtitle}>
                {`Taught By: ${ item.taughtBy }`}
              </ListItem.Subtitle>
              <ListItem.Subtitle style={styles.subtitle}>
                {`Location: ${ item.location }`}
              </ListItem.Subtitle>
            </ListItem.Content>
          </ListItem>
        </View>
      </View>
    );
  };

  render() {
    const {item} = this.props.route.params;

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
          <ScrollView style={{flex: 1}}>
            <Text style={styles.header}>Mike Stroke</Text>
            <DetailCard item={item} />
            {this.getFooterView(item)}
          </ScrollView>
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
