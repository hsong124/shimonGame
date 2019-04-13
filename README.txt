This is a game to be played with shimon using a windows laptop to run and XXXXX midi kickpad.

Requirements to play:
- loopMidi on windows
- max/msp
- python 3
- shimon
- XXXX Kickpad

Setup:
- Download repository
- Open max files zk.headModel and Helper
- Connect midi kickpad to computer/laptop
- Open loopMidi
- In command line and correct folder, type "python shimonGame.py" to run main script

Content:
- shimonGame.py is main python file to play game
- helper.py is helper file with helper functions for game
- gestures.py is not necessary, was code for sending gesture to shimon, no longer used
- test.py is file to test main components for game like:
    - playing notes, and gesture movement
-Helper.maxpat is max script to send gestures to zk.headModel.maxpat
-zk.headModel.maxpat is script to send head commands to shimon

Debug:
- check ports
- unplug and replug midi kickpad
- make sure all necessary components are running: loopMidi, max patches, shimon
- have fun!