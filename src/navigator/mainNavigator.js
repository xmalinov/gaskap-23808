import React, {useState, useEffect} from 'react';
import {connect} from 'react-redux';
import {View, Text, Button, Image} from 'react-native';
import {createStackNavigator} from '@react-navigation/stack';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';

import LoginScreen from '../features/auth/screens/Login';
import ForgetPasswordScreen from '../features/auth/screens/ForgetPassword';
import SignupScreen from '../features/auth/screens/Signup';
import EmailScreen from './../features/auth/screens/Signup/EmailScreen';
import GaurdainScreen from './../features/auth/screens/Signup/GaurdainScreen';
import PasswordScreen from './../features/auth/screens/Signup/PasswordScreen';
import ProfileScreen from '../features/user/screens/profile/ProfileMain';
import ProfileUpdate from '../features/user/screens/profile/ProfileUpdate';

import SettingsScreen from '../features/user/screens/settings/SettingsMain';

import ConfirmationCodeScreen from './../features/auth/screens/Signup/ConfirmationCodeScreen';
import ScreenConstants from '../constants/screenConstants';
import NameScreen from '../features/auth/screens/Signup/NameScreen';
import Icon from 'react-native-vector-icons/FontAwesome5';
import {images} from '../constants/images';
import {Icon as IconElement} from 'react-native-elements';

import ClassScreen from '../features/home/screens/Class';
import ClassDetail from '../features/home/screens/Class/ClassDetail';

import HomeScreen from '../features/home/screens';
import EventsScreen from '../features/home/screens/Events';

import NewsScreen from '../features/home/screens/News';
import ChatScreen from '../features/chat/ChatScreen';
import {getAccessToken} from '../utils/storageUtils';

/**
 * new navigators can be imported here
 */

function DetailsScreen() {
  return (
    <View style={{flex: 1, justifyContent: 'center', alignItems: 'center'}}>
      <Text>Details!</Text>
    </View>
  );
}

const ChatStack = createStackNavigator();

function ChatStackScreen() {
  return (
    <ChatStack.Navigator headerMode="none">
      <ChatStack.Screen
        name={ScreenConstants.search}
        component={ChatScreen}
        options={{
          animationEnabled: true,
        }}
      />
      {/* <ChatStack.Screen name="Details" component={DetailsScreen} /> */}
    </ChatStack.Navigator>
  );
}

const UsersStack = createStackNavigator();

function UsersStackScreen() {
  return (
    <UsersStack.Navigator headerMode="none">
      <UsersStack.Screen
        name={ScreenConstants.search}
        component={DetailsScreen}
        options={{
          animationEnabled: true,
        }}
      />
      {/* <UsersStack.Screen name="Details" component={DetailsScreen} /> */}
    </UsersStack.Navigator>
  );
}

const ChatTab = createBottomTabNavigator();

function ChatTabScreen() {
  return (
    <ChatTab.Navigator
      initialRouteName={ScreenConstants.chat}
      tabBarOptions={{
        activeTintColor: '#F06931',
      }}>
      <ChatTab.Screen
        name={ScreenConstants.chat}
        component={ChatStackScreen}
        options={{
          tabBarLabel: ScreenConstants.chat,
          tabBarIcon: ({color, size}) => (
            <Icon name="comment-dots" color={color} size={size} />
          ),
        }}
      />
      <ChatTab.Screen
        name={ScreenConstants.users}
        component={UsersStackScreen}
        options={{
          tabBarLabel: ScreenConstants.users,
          tabBarIcon: ({color, size}) => (
            <Icon name="users" color={color} size={size} />
          ),
        }}
      />
    </ChatTab.Navigator>
  );
}

const SearchStack = createStackNavigator();
function SearchStackScreen() {
  return (
    <SearchStack.Navigator headerMode="none">
      <SearchStack.Screen
        name={ScreenConstants.search}
        component={DetailsScreen}
        options={{
          animationEnabled: true,
        }}
      />
      {/* <SearchStack.Screen name="Details" component={DetailsScreen} /> */}
    </SearchStack.Navigator>
  );
}

const ProfileStack = createStackNavigator();
function ProfileStackScreen() {
  return (
    <ProfileStack.Navigator
      initialRouteName={ScreenConstants.profile}
    // headerMode="none"
    >
      <ProfileStack.Screen
        name={ScreenConstants.profile}
        component={ProfileScreen}
        options={{
          animationEnabled: true,
        }}
      />
      <ProfileStack.Screen
        name={ScreenConstants.profileUpdate}
        component={ProfileUpdate}
        options={{
          title: 'Profile Detail',
        }}
      />
    </ProfileStack.Navigator>
  );
}

const SettingStack = createStackNavigator();

function SettingStackScreen() {
  return (
    <SettingStack.Navigator
      initialRouteName={ScreenConstants.setting}
    // headerMode="none"
    >
      <SettingStack.Screen
        name={ScreenConstants.setting}
        component={SettingsScreen}
        options={{
          animationEnabled: true,
        }}
      />
      {/* <SettingStack.Screen
        name={ScreenConstants.profileUpdate}
        component={ProfileUpdate}
        options={{
          title: 'Update',
          headerRight: () => (
            <Button
              onPress={() => alert('This is a button!')}
              title="Done"
              color="black"
            />
          ),
        }}
      /> */}
    </SettingStack.Navigator>
  );
}

const RightView = ({navigation}) => {
  console.log(navigation);
  return (
    <View
      style={{
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
      }}>
      <IconElement
        name="comment-dots"
        type="font-awesome-5"
        color="black"
        reverseColor="black"
        onPress={() => navigation.navigate(ScreenConstants.chat)}
        containerStyle={{paddingHorizontal: 10}}
      />

      <IconElement
        name="search"
        type="font-awesome-5"
        color="black"
        reverseColor="black"
        onPress={() => navigation.navigate(ScreenConstants.search)}
        containerStyle={{paddingHorizontal: 10}}
      />
      <IconElement
        name="user"
        type="font-awesome-5"
        color="black"
        reverseColor="black"
        onPress={() => navigation.navigate(ScreenConstants.profile)}
        containerStyle={{paddingHorizontal: 10}}
      />
      <IconElement
        name="cog"
        type="font-awesome-5"
        color="black"
        reverseColor="black"
        onPress={() => navigation.navigate(ScreenConstants.setting)}
        containerStyle={{paddingHorizontal: 10}}
      />
    </View>
  );
};

const LeftView = () => {
  return (
    <Image
      source={images.logo}
      style={{
        marginLeft: 20,
        width: 100,
        // height: 40,
        resizeMode: 'contain',
      }}
    />
  );
};

const HomeStack = createStackNavigator();

function HomeStackScreen() {
  return (
    <HomeStack.Navigator
      screenOptions={({navigation}) => ({
        title: '',
        headerRight: () => <RightView navigation={navigation} />,
        headerLeft: () => <LeftView navigation={navigation} />,
      })}
      initialRouteName={ScreenConstants.home}>
      <HomeStack.Screen name={ScreenConstants.home} component={HomeScreen} />
      <HomeStack.Screen name="Details" component={DetailsScreen} />
    </HomeStack.Navigator>
  );
}

const ClassStack = createStackNavigator();

function ClassStackScreen() {
  return (
    <ClassStack.Navigator initialRouteName={ScreenConstants.classes}>
      <ClassStack.Screen
        name={ScreenConstants.classes}
        component={ClassScreen}
        options={({navigation}) => ({
          title: '',
          headerRight: () => <RightView navigation={navigation} />,
          headerLeft: () => <LeftView navigation={navigation} />,
        })}
      />
      <ClassStack.Screen
        name={ScreenConstants.classDetail}
        component={ClassDetail}
      />
    </ClassStack.Navigator>
  );
}

const EventStack = createStackNavigator();

function EventsStackScreen() {
  return (
    <EventStack.Navigator initialRouteName={ScreenConstants.classes}>
      <EventStack.Screen
        name={ScreenConstants.events}
        component={EventsScreen}
        options={({navigation}) => ({
          title: '',
          headerRight: () => <RightView navigation={navigation} />,
          headerLeft: () => <LeftView navigation={navigation} />,
        })}
      />
      <EventStack.Screen
        name={ScreenConstants.classDetail}
        component={ClassDetail}
      />
    </EventStack.Navigator>
  );
}

const NewsStack = createStackNavigator();

function NewsStackScreen() {
  return (
    <NewsStack.Navigator initialRouteName={ScreenConstants.classes}>
      <NewsStack.Screen
        name={ScreenConstants.events}
        component={NewsScreen}
        options={({navigation}) => ({
          title: '',
          headerRight: () => <RightView navigation={navigation} />,
          headerLeft: () => <LeftView navigation={navigation} />,
        })}
      />
      <NewsStack.Screen
        name={ScreenConstants.classDetail}
        component={ClassDetail}
      />
    </NewsStack.Navigator>
  );
}

const Tab = createBottomTabNavigator();

const TabNavigator = () => {
  return (
    <Tab.Navigator
      initialRouteName={'Main'}
      tabBarOptions={{
        activeTintColor: '#F06931',
      }}>
      <Tab.Screen
        name={ScreenConstants.home}
        component={HomeStackScreen}
        options={{
          tabBarLabel: ScreenConstants.home,
          tabBarIcon: ({color, size}) => (
            <Icon name="home" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name={ScreenConstants.classes}
        component={ClassStackScreen}
        options={{
          tabBarLabel: ScreenConstants.classes,
          tabBarIcon: ({color, size}) => (
            <Icon name="book-open" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name={ScreenConstants.events}
        component={EventsStackScreen}
        options={{
          tabBarLabel: ScreenConstants.events,
          tabBarIcon: ({color, size}) => (
            <Icon name="calendar" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name={ScreenConstants.news}
        component={NewsStackScreen}
        options={{
          tabBarLabel: ScreenConstants.news,
          tabBarIcon: ({color, size}) => (
            <Icon name="newspaper" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name={ScreenConstants.notifications}
        component={HomeStackScreen}
        options={{
          tabBarLabel: ScreenConstants.notifications,
          tabBarIcon: ({color, size}) => (
            <Icon name="bell" color={color} size={size} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};

const AuthStack = createStackNavigator();

const AuthNavigation = () => {
  return (
    <AuthStack.Navigator
      initialRouteName={ScreenConstants.login}
    // headerMode="none"
    >
      <AuthStack.Screen
        options={{headerShown: false}}
        name={ScreenConstants.login}
        component={LoginScreen}
      />
      <AuthStack.Screen
        name={ScreenConstants.forgetPassword}
        component={ForgetPasswordScreen}
      />
      <AuthStack.Screen
        name={ScreenConstants.signUp}
        component={SignupScreen}
      />
      <AuthStack.Screen name={ScreenConstants.email} component={EmailScreen} />
      <AuthStack.Screen
        name={ScreenConstants.confirmationCode}
        component={ConfirmationCodeScreen}
      />
      <AuthStack.Screen name={ScreenConstants.addName} component={NameScreen} />
      <AuthStack.Screen
        name={ScreenConstants.password}
        component={PasswordScreen}
      />
      <AuthStack.Screen
        name={ScreenConstants.guardain}
        component={GaurdainScreen}
      />
    </AuthStack.Navigator>
  );
};

const RootStack = createStackNavigator();

function RootStackScreen(props) {
  let isAuthorized = false;

  if (props.auth) {
    if (props.profile.is_active) {
      isAuthorized = true;
    } else if (props.user.is_active) {
      isAuthorized = true;
    }
  }

  if (isAuthorized) {
    return (
      <RootStack.Navigator headerMode="none">
        <RootStack.Screen
          name="Main"
          component={TabNavigator}
          options={{headerShown: false}}
        />
        <RootStack.Screen
          name={ScreenConstants.chat}
          component={ChatTabScreen}
        />
        <RootStack.Screen
          name={ScreenConstants.search}
          component={SearchStackScreen}
        />
        <RootStack.Screen
          name={ScreenConstants.profile}
          component={ProfileStackScreen}
        />
        <RootStack.Screen
          name={ScreenConstants.setting}
          component={SettingStackScreen}
        />
      </RootStack.Navigator>
    );
  } else {
    return <AuthNavigation />;
  }
}

const mapStateToProps = state => {
  return {
    auth: state.authReducer.auth,
    user: state.authReducer.user,
    profile: state.customReducer.profile,
  };
};

export default connect(mapStateToProps)(RootStackScreen);
