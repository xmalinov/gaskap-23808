import React, {Component} from 'react';
import {View, Text, ScrollView} from 'react-native';
import {connect} from 'react-redux';
import {Avatar, ListItem, Icon, SearchBar} from 'react-native-elements';
import SegmentedControl from '@react-native-community/segmented-control';

import {styles} from './styles';
import {SafeAreaView} from 'react-native';
import ListNews from './ListNews';
import RandomNews from './RandomNews';

const newsLists = [
  {
    title: 'News 1',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'News 2',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'News 3',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'News 4',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'News 5',
    description: 'Description',
    location: 'Location date and time',
  },
  {
    title: 'News 6',
    description: 'Description',
    location: 'Location date and time',
  },
];

class News extends Component {
  state = {
    selectedIndex: 0,
    searchTerm: '',
    isSearchActive: false,
  };

  updateSearchTerm = search => {
    this.setState({searchTerm: search});
  };

  handleListItemClick = item => {
    console.log(item.title);
  };

  getListComponent = () => {
    const index = this.state.selectedIndex;
    if (index === 0) {
      return <RandomNews />;
    } else {
      return (
        <ListNews
          handleItemClick={this.handleListItemClick}
          itemList={newsLists}
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
)(News);
