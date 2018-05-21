import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View
} from 'react-native';

type Props = {};
export default class main extends Component<Props> {
    render() {
        return (
            <View style={styles.container}>
                <Text style={styles.welcome}>
                    Welcome to Cilantro,
                </Text>
                <Text style={styles.instructions}>
                    Let's start with a team name:
                </Text>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'flex-start',
        backgroundColor: '#388E3C',
        padding: 10,
    },
        welcome: {
        fontSize: 20,
        textAlign: 'left',
    },
});
