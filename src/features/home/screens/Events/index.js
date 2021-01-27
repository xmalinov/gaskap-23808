import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon, SearchBar} from 'react-native-elements';
import SegmentedControl from '@react-native-community/segmented-control';

import {styles} from './styles';
import {SafeAreaView} from 'react-native';
import ListEvents from './ListEvents';
import RandomEvents from './RandomEvents';
import {profileApiService} from '../../../../services/user';

const eventLists = [
  {
    title: 'Event 1',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'Event 2',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'Event 3',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'Event 4',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'Event 5',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'Event 6',
    description: 'Description',
    location: 'Location date and time',
  },
];

class Events extends Component {
  state = {
    selectedIndex: 0,
    searchTerm: '',
    isSearchActive: false,
  };

  componentDidMount = async () => {
    const results = await profileApiService.getProfile();
    console.log(results)
  }

  updateSearchTerm = search => {
    this.setState({searchTerm: search});
  };

  handleListItemClick = item => {
    console.log(item.title);
  };

  getListComponent = () => {
    const index = this.state.selectedIndex;
    if (index === 0) {
      return <RandomEvents />;
    } else {
      return (
        <ListEvents
          handleItemClick={this.handleListItemClick}
          itemList={eventLists}
        />
      );
    }
  };

  render() {
    return (
      <SafeAreaView style={styles.wrapper}>
        <View style={styles.headerContainer}>
          <SegmentedControl
            values={['Random', 'List']}
            selectedIndex={this.state.selectedIndex}
            onChange={event => {
              this.setState({
                selectedIndex: event.nativeEvent.selectedSegmentIndex,
              });
            }}
          />

          <View style={{paddingVertical: 10}}>
            <SearchBar
              round
              placeholder="Search"
              onChangeText={this.updateSearch}
              value={this.state.searchTerm}
              showCancel={true}
              showLoading={this.state.isSearchActive}
              lightTheme={true}
              containerStyle={styles.searchContainer}
              inputContainerStyle={styles.searchInput}
            />
          </View>
        </View>
        <ScrollView>
          {this.getListComponent()}
        </ScrollView>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = state => {
  return {};
};
const mapDispToProps = dispatch => ({});

export default connect(
  mapStateToProps,
  mapDispToProps,
)(Events);
