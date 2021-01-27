import React from 'react';
import { StyleSheet, View, ActivityIndicator } from 'react-native';

const styles = StyleSheet.create({
	wrapper: {
		flex: 1,
		alignItems: 'center',
		justifyContent: 'center'
	}
})

export const Loader = props => {
	return (
		<View style={styles.wrapper}>
			<ActivityIndicator size={props.size} />
		</View >
	)
}