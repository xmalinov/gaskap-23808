import {StyleSheet} from 'react-native';

export const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    display: 'flex',
    flex: 1,
    paddingHorizontal: 36,
  },
  itemsContainer: {
    position: 'relative',
    height: '100%',
    width: '100%',
    // justifyContent: 'center',
    alignItems: 'center',
  },
  titleText: {
    fontSize: 30,
    paddingTop: 100,
  },
  itemTextInput: {
    height: 40,
    width: '100%',
    borderRadius: 20,
    borderColor: '#D6D6D6',
    backgroundColor: '#EFEFEF',
    borderWidth: 2,
    // marginVertical: 2,
    paddingHorizontal: 20,
  },
  itemTextContainer: {
    borderBottomWidth: 0,
    paddingHorizontal: 0,
    marginHorizontal: 0,
  },
  itemConfirmationCode: {
    color: 'grey',
    fontSize: 16,
    paddingTop: 10,
    paddingBottom: 40,
    textAlign: 'center'
  },
});
