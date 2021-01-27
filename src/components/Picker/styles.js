import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
  container: {
    width: '100%',
    height: 45,
    marginBottom: 10,
    // paddingHorizontal: 10,
    borderRadius: 20,
  },
  innerStyle: {
    borderColor: '#D6D6D6',
    borderWidth: 2,
    borderRadius: 20,
    backgroundColor: '#EFEFEF',
    width: '100%',
  },
  itemStyle: {
    justifyContent: 'flex-start',
    paddingHorizontal: 10,
    paddingVertical: 10,
  },
  selectedLabelStyle: {
    color: 'black',
  },
  dropdownStyle: {
    backgroundColor: '#fafafa',
    borderRadius: 20,
  },
  placeholderStyle: {
    color: '#636c72',
    // textAlign: 'center',
  },
});

export default styles;
