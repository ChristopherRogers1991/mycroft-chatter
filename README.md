# mycroft-chatter
Provides a chat like interface to [Mycroft](https://mycroft.ai/)

![mycroft-chatter-demo](https://github.com/ChristopherRogers1991/mycroft-chatter/blob/master/data/screenshots/mycroft-chatter.gif)

To use:
```
virtualenv -p `which python3` ~/.virtualenvs/mycroft-chatter
source ~/.virtualenvs/mycroft-chatter
git clone https://github.com/ChristopherRogers1991/mycroft-chatter.git
cd mycroft-chatter
pip install -r requirements.txt
pip install .
python client/chat.py
```

Note that you can disable Mycroft's audio response by stopping the it's audio service.

### Author's Note:
Feedback is welcome. I had no experience with python3, websockets, or pyqt before starting this, so feel free to share pointers.
