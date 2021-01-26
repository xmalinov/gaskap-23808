import {createStackNavigator} from '@react-navigation/stack';

import Login from './Login'

export default BlankBlueprintNavigator = createStackNavigator(
  {
    Login: {screen: Login},
  },
  {
    initialRouteName: 'Login',
  },
)
