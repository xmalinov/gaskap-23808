import {StyleSheet} from 'react-native';

export const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
  },
  profilePhoto: {
    borderWidth: 1,
    marginTop: 10,
  },
  userName: {
    marginTop: 10,
    fontSize: 24,
    fontWeight: '500',
  },
  itemIcon: {
    borderWidth: 1,
  },
  listWrapper: {
    flex: 1,
    width: '100%',
    backgroundColor: 'red',
  },
  listTitle: {
    fontWeight: '500',
  },
});
