# Cilantro
> React-Native Mobile App

## Available Scripts
When first running the app on a local machine, run `yarn dev` to install the required `node_modules`.

To run the application in android studio, first launch an AVD (Android Virtual Device) and then run the command `react-native run-android` in your powershell or cmd terminal. If for any reason the development server closes itself but the app is still running, run the command `npm start` to relaunch the development server.

## Customising App Environment Variables
All necessary environment variables that Cilantro requires are configured on the app's initial load.

When the app is first launched on a user's mobile device they will be prompted to enter a series of information:

```
First, lets start with a team name:
```
Gives the user an option to input a team name for the purposes of the Red River Robotics Competition.

```
Next, we'll need the IP of your Pi:
```
Cilantro's [Python Flask Kit]() is designed to be installed on a Raspberry Pi. The flask app serves as an API, and such the mobile app uses simple network requests to command the robot to do a series of pre-written tasks.


User's also have the option to add their own endpoints other than the default included controller ones.