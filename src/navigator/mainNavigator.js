import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen18187381Navigator from '../features/BlankScreen18187381/navigator';
import BlankScreen17187379Navigator from '../features/BlankScreen17187379/navigator';
import BlankScreen16187378Navigator from '../features/BlankScreen16187378/navigator';
import BlankScreen15187377Navigator from '../features/BlankScreen15187377/navigator';
import BlankScreen14187376Navigator from '../features/BlankScreen14187376/navigator';
import BlankScreen13187375Navigator from '../features/BlankScreen13187375/navigator';
import BlankScreen12187374Navigator from '../features/BlankScreen12187374/navigator';
import BlankScreen11187373Navigator from '../features/BlankScreen11187373/navigator';
import BlankScreen10187372Navigator from '../features/BlankScreen10187372/navigator';
import BlankScreen9187371Navigator from '../features/BlankScreen9187371/navigator';
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
BlankScreen18187381: { screen: BlankScreen18187381Navigator },
BlankScreen17187379: { screen: BlankScreen17187379Navigator },
BlankScreen16187378: { screen: BlankScreen16187378Navigator },
BlankScreen15187377: { screen: BlankScreen15187377Navigator },
BlankScreen14187376: { screen: BlankScreen14187376Navigator },
BlankScreen13187375: { screen: BlankScreen13187375Navigator },
BlankScreen12187374: { screen: BlankScreen12187374Navigator },
BlankScreen11187373: { screen: BlankScreen11187373Navigator },
BlankScreen10187372: { screen: BlankScreen10187372Navigator },
BlankScreen9187371: { screen: BlankScreen9187371Navigator },
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
