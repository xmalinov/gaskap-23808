import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon} from 'react-native-elements';
import Dialog from 'react-native-dialog';
import * as customActions from '../../../../../store/custom/constants';
import DateTimePicker from '@react-native-community/datetimepicker';
import {format, compareAsc} from 'date-fns';

import {styles} from './styles';
import {
  grades,
  keys,
  profileItems,
  settingItems,
} from '../../../../../constants/generalConstants';
import Picker from '../../../../../components/Picker';
import {Loader} from '../../../../../components/Loader';

const classLisItems = [
  {
    class: 'Geometry 101',
    taughtBy: 'Mrs. Wrenfield',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'World History',
    taughtBy: 'Mr Goodwyn',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'Cooking Making',
    taughtBy: 'Mrs. Smith Cookies',
    location: 'Room',
    iconName: 'user',
  },
  {
    class: 'Underwater Basket Weaving',
    taughtBy: 'Uncle Ben',
    location: 'Room',
    iconName: 'user',
  },
];

const gradeList = [
  {
    label: grades.first,
    value: grades.first,
  },
  {
    label: grades.second,
    value: grades.second,
  },
  {
    label: grades.third,
    value: grades.third,
  },
  {
    label: grades.fourth,
    value: grades.fourth,
  },
  {
    label: grades.fifth,
    value: grades.fifth,
  },
  {
    label: grades.sixth,
    value: grades.sixth,
  },
  {
    label: grades.seventh,
    value: grades.seventh,
  },
  {
    label: grades.eight,
    value: grades.eight,
  },
  {
    label: grades.freshman,
    value: grades.freshman,
  },
  {
    label: grades.sophomore,
    value: grades.sophomore,
  },
  {
    label: grades.junior,
    value: grades.junior,
  },
  {
    label: grades.senior,
    value: grades.senior,
  },
];

class ProfileUpdate extends Component {
  state = {
    showDialog: false,
    showDatePicker: false,
    itemValue: '',
    studentId: '',
    dob: new Date(),
    city: '',
    state: '',
  };

  handleUpdateConfirm = item => {
    this.setState({showDialog: false}, () => {
      let params = {};

      switch (item.title) {
        case profileItems.age:
          const date = format(this.state.dob, keys.date_format);
          params = {date_of_birth: date};
          break;
        case profileItems.city:
          params = {city: this.state.city};
          break;
        case profileItems.state:
          params = {state: this.state.state};
          break;
        default:
          break;
      }

      this.props.updateProfile(params);
    });
  };

  handleTextChange = (value, item) => {
    switch (item.title) {
      case profileItems.age:
        this.setState({dob: value});
        break;
      case profileItems.city:
        this.setState({city: value});
        break;
      case profileItems.state:
        this.setState({state: value});
        break;
      default:
        break;
    }
  };

  getPlaceHolder = item => {
    let placeholder = '';
    const {profile} = this.props;

    if (profile) {
      switch (item.title) {
        case profileItems.studentId:
          placeholder = profile.profile.student_id;
          break;
        case profileItems.schoolId:
          placeholder = profile.profile.school.number;
          break;
        case profileItems.age:
          placeholder = profile.profile.date_of_birth;
          break;
        case profileItems.city:
          placeholder = profile.profile.city;
          break;
        case profileItems.state:
          placeholder = profile.profile.state;
          break;
        default:
          break;
      }
    } else {
      placeholder = item.title;
    }

    return placeholder || item.title;
  };

  handleGradeChange = ({value}) => {
    this.props.updateProfile({grade: value});
  };

  getInputView = item => {
    if (profileItems.age === item.title) {
      return (
        <DateTimePicker
          testID="dateTimePicker"
          value={this.state.dob}
          mode={'date'}
          is24Hour={true}
          display="default"
          maximumDate={new Date()}
          onChange={this.onDateChange}
        />
      );
    } else {
      return (
        <Dialog.Input
          autoCapitalize="none"
          onChangeText={value => this.handleTextChange(value, item)}
          placeholder={this.getPlaceHolder(item)}
        />
      );
    }
  };

  updateDialog = item => {
    return (
      <View>
        <Dialog.Container visible={this.state.showDialog}>
          <Dialog.Title>{`Change ${item.title}`}</Dialog.Title>
          <Dialog.Description>{`New ${item.title}`}</Dialog.Description>
          {this.getInputView(item)}
          <Dialog.Button
            onPress={() => this.setState({showDialog: false})}
            label="Cancel"
          />
          <Dialog.Button
            onPress={() => this.handleUpdateConfirm(item)}
            label="Confirm"
          />
        </Dialog.Container>
      </View>
    );
  };

  getEditView = item => {
    const profile = this.props.profile;

    if (item.title === profileItems.grade && item.isEditable) {
      return (
        <View style={{width: '60%'}}>
          <Picker
            defaultValue={profile.profile.grade}
            placeHolder="Select grade"
            items={gradeList}
            onChangeItem={this.handleGradeChange}
          />
        </View>
      );
    } else {
      return (
        <>
          <Text style={{paddingRight: 16}}>{this.getPlaceHolder(item)}</Text>
          {item.isEditable && (
            <Icon
              // raised
              size={16}
              name="edit"
              type="font-awesome-5"
              // color='#f50'
              onPress={() => this.setState({showDialog: true})}
            />
          )}
        </>
      );
    }
  };

  onDateChange = (event, selectedDate) => {
    const currentDate = selectedDate || this.state.dob;
    this.setState({dob: currentDate});
  };

  getDetailView = item => {
    if (item.title === profileItems.classAssigned) {
      return classLisItems.map((classItem, index) => {
        return (
          <ListItem bottomDivider key={index}>
            <Avatar
              rounded
              icon={{
                name: 'book-open',
                type: 'font-awesome-5',
                color: 'black',
              }}
              containerStyle={styles.itemIcon}
            />
            <ListItem.Content>
              <ListItem.Title style={styles.listTitle}>
                {classItem.class}
              </ListItem.Title>
              <ListItem.Subtitle style={styles.listTitle}>
                {`Taught by ${classItem.taughtBy} in ${classItem.location}`}
              </ListItem.Subtitle>
            </ListItem.Content>
          </ListItem>
        );
      });
    } else {
      return (
        <ListItem bottomDivider>
          <Avatar
            rounded
            icon={{name: item.iconName, type: 'font-awesome-5', color: 'black'}}
            containerStyle={styles.itemIcon}
          />
          <ListItem.Content>
            <ListItem.Title style={styles.listTitle}>
              {item.title}
            </ListItem.Title>
          </ListItem.Content>
          {this.getEditView(item)}
        </ListItem>
      );
    }
  };

  render() {
    const {item} = this.props.route.params;
    const {isMakingNetworkRequest} = this.props;

    if (isMakingNetworkRequest) {
      return <Loader size="large" />;
    }

    return (
      <View style={styles.wrapper}>
        {this.getDetailView(item)}
        {this.updateDialog(item)}
      </View>
    );
  }
}

const mapStateToProps = state => {
  return {
    isMakingNetworkRequest: state.customReducer.isMakingNetworkRequest,
    profile: state.customReducer.profile,
  };
};
const mapDispToProps = dispatch => ({
  updateProfile: obj => dispatch({type: customActions.UPDATE_PROFILE, obj}),
});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(ProfileUpdate);
