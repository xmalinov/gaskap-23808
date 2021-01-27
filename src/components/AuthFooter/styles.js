import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'flex-end',
  },
  itemFooterWrapper: {
    width: '100%',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingBottom: 20,
  },
  itemFooterText: {
    fontSize: 14,
    color: '#B5B5B5',
    paddingRight: 6,
  },
  itemSignupText: {
    fontSize: 14,
    color: '#3E7EBB',
  },
  itemLogo: {
    width: '60%',
    height: 80,
    resizeMode: 'contain',
  },
});

export default styles;
