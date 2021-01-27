import React, {Component} from 'react';

import {View, Dimensions, Text, Button} from 'react-native';

import Video from 'react-native-video';
import styles from './styles';
import generalUtils from './../../utils/gneralUtils';

export default class VideoPlayer extends Component {
  constructor(props) {
    super(props);
    this.onLayout = this.onLayout.bind(this);

    this.state = {
      orientationWidth: 0,
      orientationHeight: 0,
    };
  }

  componentDidMount() {
    this.resizeVideoPlayer();
  }

  render() {
    return (
      <View onLayout={this.onLayout} style={styles.container}>
        {/* <Text>Here's some pre-Text</Text> */}
        <Video
          ref={p => {
            this.videoPlayer = p;
          }}
          source={{uri: this.props.videoUrl}}
          style={{
            width: this.state.orientationWidth,
            height: this.state.orientationHeight,
          }}
          controls={true}
        />
        {/* <Button title="full screen" onPress={this.onPress.bind(this)} /> */}
      </View>
    );
  }

  onPress() {
    if (this.videoPlayer != null) {
      this.videoPlayer.presentFullscreenPlayer();
    }
  }

  resizeVideoPlayer() {
    // Always in 16 /9 aspect ratio
    let {width, height} = Dimensions.get('window');

    if (generalUtils.isPortrait()) {
      this.setState({
        orientationWidth: width * 0.8,
        orientationHeight: width * 0.8 * 0.56,
      });
    } else {
      this.setState({
        orientationHeight: height * 0.8,
        orientationWidth: height * 0.8 * 1.77,
      });
    }
  }

  onLayout(e) {
    console.log('on layout called');
    this.resizeVideoPlayer();
  }
}
