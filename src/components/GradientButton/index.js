import React from 'react';

import styles from './styles';
import {TouchableOpacity, Text, ActivityIndicator} from 'react-native';
import LinearGradient from 'react-native-linear-gradient';

const GradientButton = props => {
  const getInnerElement = isLoading => {
    if (isLoading) {
      return <ActivityIndicator size="small" color="white" />;
    }
    return <Text style={styles.text}>{props.title}</Text>;
  };

  return (
    <TouchableOpacity style={styles.button} onPress={props.onPress}>
      <LinearGradient
        colors={['#EB542B', '#EE8031', '#F5C042']}
        style={styles.gradient}
        end={{y: 0.0, x: 1.0}}
        start={{y: 0.0, x: 0.0}}
      >
        {getInnerElement(props.isLoading)}
      </LinearGradient>
    </TouchableOpacity>
  );
};

export default GradientButton;
