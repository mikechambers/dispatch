# Dispatch

Dispatch is a Python 3 script that syncs the current weekly edition of The Economist into reader mode for the Apple Safari browser on macOS and iOS.

This can be used as an alternative to the Economist iOS app for reading the digital version of the Economist on macOS and iOS, and makes it easy to search through articles. It requires that you have access to the digital version of the Economist.

## Requirements

* Python 3 (has not been tested with Python 2)
* Safari browser running on macOS
* Access to the digital version of the Economist

## Usage

### Setup on macOS

On macOS make sure you are logged into the Economist (https://www.economist.com/) in Safari.

If you want the articles to be synced to your machine, and available to read offline, go to Safari > Settings > Advanced and make sure that *Save articles for offline reading automatically* is checked.

Download the dispatch.py script, and place it in a location you will remember.

### Sync to Reading mode on macOS

Open the terminal application, switch to the directory where the script is saved, and then run the script with the following command:

```bash
python3 dispatch.py
```

This will sync all of the current weeks articles for the Economist into the Reader mode in Safari, which you can view at *Safari > View > Show Reading List Sidebar*

The articles may take a couple of minutes to sync, but you can begin to read them immediately.

Tip, if you press **CMD-SHIFT-R** when viewing the article, it will format the article in Reader mode which makes it much easier to read.

### Sync with iOS

If you would like to have the reading list synced with Safari on iOS, enabled iCloud syncing for Safari on iOS and macOS by following the instructions at:

https://support.apple.com/guide/icloud/set-up-safari-mm5400ef10c4/icloud

View this article for information on how to view Reading List in Safari on iOS, including how to enabled offline mode:

https://support.apple.com/en-us/108970

### Print all article URLs

If you would like to just get a list the URLs for all of the articles for the current edition, then call the script and set the **print** flag like so:

```bash
python3 dispatch.py --print
```

This will print out the URL for each article in the current edition, with one url per line.

## Questions, Feature Requests, Feedback

If you have any questions, feature requests, need help, or just want to chat, you can ping me on [Twitter](https://twitter.com/mesh) or via email at [mikechambers@gmail.com](mailto:mikechambers@gmail.com).

You can also log bugs and feature requests on the [issues page](https://github.com/mikechambers/dispatch/issues).

## License

Project released under a [MIT License](LICENSE.md).

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE.md)

