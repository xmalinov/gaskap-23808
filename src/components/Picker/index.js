import React from 'react';

import styles from './styles';
import DropDownPicker from 'react-native-dropdown-picker';

const Picker = props => {
  return (
    <DropDownPicker
      placeholder={props.placeHolder}
      items={props.items}
      defaultValue={props.defaultValue}
      containerStyle={styles.container}
      style={styles.innerStyle}
      itemStyle={styles.itemStyle}
      labelStyle={{ fontSize: 14, textAlign: 'left', color: '#000' }}
      selectedLabelStyle={styles.selectedLabelStyle}
      dropDownStyle={styles.dropdownStyle}
      placeholderStyle={styles.placeholderStyle}
      onChangeItem={props.onChangeItem}
    />
  );
};

export default Picker;
