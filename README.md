## W1m camera daemons [![Travis CI build status](https://travis-ci.org/warwick-one-metre/camd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/camd)

Part of the observatory software for the Warwick one-meter telescope.

`camd` interfaces with and wraps the Andor cameras and exposes them via Pyro.

`cam` is a commandline utility for controlling the cameras.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

The Andor SDK is required for `onemetre-camera-server`, and must be installed separately.
Download the latest SDK version from the [Docs repository](https://github.com/warwick-one-metre/docs/tree/master/andor/sdk), extract it, and then install using:
```
sudo ./install_andor
```
Select option 5 (All USB Cameras).
After installing `onemetre-camera-server`, the `red_camd` and `blue_camd` services must be enabled using:
```
sudo systemctl enable red_camd.service blue_camd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start red_camd.service blue_camd.service
```


