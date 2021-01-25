import {StyleSheet} from 'react-native';

export const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    // justifyContent: 'center',
    // alignItems: 'center',
    // display: 'flex',
    // flex: 1,
    height: '100%',
    paddingHorizontal: 40,
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
    paddingVertical: 100,
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
  errorStyle: {
    height: 0,
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
  itemResendCodeWrapper: {
    width: '100%',
    flexDirection: 'row',
    // alignItems: 'center',
    // justifyContent: 'center',
    // justifyContent: 'space-between',
    paddingBottom: 40,
    // backgroundColor: 'red',
  },
  itemResendCode: {
    flex: 0.5,
    fontSize: 20,
    color: '#3275B6',
  },
  confirmationTitle: {
    fontSize: 30,
    paddingTop: 100,
    paddingBottom: 20,
  },
  itemConfirmationCode: {
    color: 'black',
    fontSize: 16,
    paddingBottom: 40,
  },
  infoTitle: {
    color: 'grey',
    fontSize: 14,
    paddingTop: 10
  },
  checkBackground: {
    backgroundColor: 'white',
    borderColor: 'transparent',
    width: '90%',
    marginTop: -6,
  },
});
