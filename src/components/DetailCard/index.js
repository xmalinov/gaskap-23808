import React from 'react';
import PropTypes from 'prop-types';

import styles from './styles';
import {Avatar, ListItem, Image} from 'react-native-elements';
import {View, ActivityIndicator} from 'react-native';
import VideoPlayer from '../VideoPlayer';

const DetailCard = props => {
  const {item} = props;

  return (
    <View style={styles.container}>
      <ListItem
        bottomDivider
        onPress={() => this.handleItemClick(item)}
        containerStyle={{paddingHorizontal: 0, width: '100%'}}
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
        </ListItem.Content>
      </ListItem>
      {/* <VideoPlayer videoUrl="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" /> */}
      <View style={styles.imageContainer}>
        <Image
          style={styles.profileImage}
          source={{
            uri: 'https://picsum.photos/seed/picsum/400/200',
          }}
          PlaceholderContent={<ActivityIndicator />}
        />
      </View>
    </View>
  );
};

DetailCard.defaultProps = {
  title: '',
  photoUrl: '',
  pictureUrl: '',
  videoUrl: '',
};

DetailCard.prototype = {
  title: PropTypes.string,
  photoUrl: PropTypes.string,
  pictureUrl: PropTypes.string,
  videoUrl: PropTypes.string,
};

export default DetailCard;
