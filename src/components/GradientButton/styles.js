import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
  container: {
    borderWidth: 2,
    borderColor: '#e3e3e3',
    padding: 10,
    margin: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {textAlign: 'center'},
  gradient: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 20,
  },
  button: {
    width: '100%',
    height: 45,
    borderRadius: 20,
    // paddingHorizontal: 10,
  },
  text: {
    color: 'black',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default styles;
