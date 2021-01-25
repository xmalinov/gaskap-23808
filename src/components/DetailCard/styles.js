import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  listTitle: {
    fontWeight: '500',
  },
  itemIcon: {
    borderWidth: 1,
  },
  imageContainer: {
    height: '100%',
    width: '100%'
  },
  profileImage: {
    height: 200,
    width: '100%',
    resizeMode: 'contain',
  }
});

export default styles;
