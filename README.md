# Remote Machine Monitor
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/krishnanunnir/server_monitor_bot/blob/master/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)



<p align="center">
  <img src="docs/bot-working.gif" height=600 width=300 />
</p>

## Why?

You can use this program if you need to
1. Get screenshots of a machine you don't have physical access to.
2. Run bash commands on your remote machine to get stats for server load, downtime and so on.
This is a tool I developed to control my PC when I don't have access to it.

## How?
1. Clone this github repo  
```https://github.com/krishnanunnir/Remote-Machine-Monitor.git && cd Remote-Machine-Monitor```

2. Create a virtual environment  
``` mkdir .env && python3 -m venv .env/smb```

3. Activate the virtual environment  
```source .env/smb/bin/activate```

4. Now we need to install all requirements  
```cd bin && python run_once.py```

5. Generate a bot in telegram, add the __token value__ of the bot and the __user ids__ of the users permitted to use this bot in the properties.py file.

6. Configure other values in the properties.py for curr_dir, logs and permitted_commands.

7. We are now good to go and can start our server by running  
```python start.py```

## Future?
1. [X] Grabbing screenshots of the users device.
2. [ ] Scheduling messages for an interval
