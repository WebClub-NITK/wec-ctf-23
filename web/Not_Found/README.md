# **Not_Found**

Category: Web

Author: Md Arfath

Flag: `WEC{N0T_R1CK_R0LL3D}`

## Problem Statement

Go on just look into it !

## Relevant files / links

- [Click Me](https://coderman001.pythonanywhere.com)

## Solution

- The riddle hints towards an SSTI attack


- By using Burp suit one can find out The web Templet Engine used . Jinja2 is used in this case

- The flag is stored in a secret key which one can access by getting the configuration values of the applicaiton.

- We can dump the contents of the config object by using the payload {{conig.items}} . 'name' is the query parameter here.

- https://coderman001.pythonanywhere.com/?name={{config.items()}}