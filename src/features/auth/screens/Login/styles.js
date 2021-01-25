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
    paddingVertical: 20,
    width: '100%',
    justifyContent: 'center',
    alignItems: 'center',
    // backgroundColor: 'red',
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
  },
  errorStyle: {
    height: 0,
  },
  forgetPasswordContainer: {
    width: '100%',
    alignItems: 'flex-end',
    paddingBottom: 80,
  },
  forgetPasswordTitle: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  item: {
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#e3e3e3',
    padding: 10,
    color: 'black',
    width: '48%',
    margin: 2,
  },
  itemSlogan: {
    height: 100,
    width: '60%',
    resizeMode: 'contain',
  },
  itemFooterWrappe: {
    width: '100%',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 20,
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
  itemLogo: {},
  itemFont: {
    color: 'black',
    fontWeight: 'bold',
    padding: 10,
  },

  logo: {
    width: '100%',
  },
  mainText: {
    fontSize: 20,
    fontFamily: 'Roboto-Medium',
    marginTop: 20,
    color: '#130D3C',
  },
  checkBackground: {
    backgroundColor: 'white',
    borderColor: 'transparent',
    width: '90%',
    marginTop: -6,
    paddingHorizontal: 0
  },
});
