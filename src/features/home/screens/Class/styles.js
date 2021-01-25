import {StyleSheet} from 'react-native';

export const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    flex: 1,
    paddingHorizontal: 16,

  },
  chatContainer: {
    alignItems: 'center',
    flexDirection: 'row',
    justifyContent: 'center',
  },
  chatTitle: {
    color: '#A1A1A1',
  },
  header: {
    fontWeight: 'bold',
    fontSize: 20,
  },
  itemIcon: {
    borderWidth: 1,
  },
  listTitle: {
    fontWeight: '500',
  },
  subtitle: {
    fontWeight: '400',
    fontSize: 14,
    color: 'gray',
  },
  footerView: {
    flex: 1,
    flexDirection: 'row',
  },
  descriptionContainer: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: 'green',
  },
});
