import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen8187370Navigator from '../features/BlankScreen8187370/navigator';
import BlankScreen7187369Navigator from '../features/BlankScreen7187369/navigator';
import BlankScreen6187368Navigator from '../features/BlankScreen6187368/navigator';
import BlankScreen5187367Navigator from '../features/BlankScreen5187367/navigator';
import BlankScreen4187366Navigator from '../features/BlankScreen4187366/navigator';
import BlankScreen3187365Navigator from '../features/BlankScreen3187365/navigator';
import BlankScreen2187364Navigator from '../features/BlankScreen2187364/navigator';
import BlankScreen1187363Navigator from '../features/BlankScreen1187363/navigator';
import BlankScreen0187362Navigator from '../features/BlankScreen0187362/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen8187370: { screen: BlankScreen8187370Navigator },
BlankScreen7187369: { screen: BlankScreen7187369Navigator },
BlankScreen6187368: { screen: BlankScreen6187368Navigator },
BlankScreen5187367: { screen: BlankScreen5187367Navigator },
BlankScreen4187366: { screen: BlankScreen4187366Navigator },
BlankScreen3187365: { screen: BlankScreen3187365Navigator },
BlankScreen2187364: { screen: BlankScreen2187364Navigator },
BlankScreen1187363: { screen: BlankScreen1187363Navigator },
BlankScreen0187362: { screen: BlankScreen0187362Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
