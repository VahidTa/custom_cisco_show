# custom cisco show commands

Customizing Cisco show commands in terminal.

I added emojis and colors to the output of the show commands and maipulated the output to make it more readable.

This project is just a small example to show how you can add customizations to the output of the show commands.
Codes are in Python 2.7.

## Features

- Popular `show ip int br` customized command.
- Ommited `show interface` command to just show traffic part.

## Usage

### show_intf.py

- Upload/add [show_intf.py](show_intf.py) to IOS XR root directory.
- config e.g. `alias exec show-intf run python show_intf.py`
- run `show-intf` and:
![Customized show command](img/show_intf.png?raw=true)

### intf_traffic.py
It is important to write interface in full name, e.g. `GigabitEthernet0/0/0/0`

- Upload/add [intf_traffic.py](intf_traffic.py) to IOS XR root directory.
- config e.g. `alias exec traffic run python intf_traffic.py`
- run `traffic GigabitEthernet0/0/0/0` and:
![Customized show command](img/traffic_intf.png?raw=true)
