# **Momento Mori**

Category: web

Author: Abhiraj Mengade

Answer / Flag: `WEC{TR4IT0R}`

## Problem Statement

Someone Time Travelled to the past and killed a man. Can you help us catch him?

## Relevant files / links

https://FrequentLightblueWeb.mixedbag.repl.co

## Solution

- Visit the URL provided in the problem statement.
- You will be greeted with a vague index page.
- Inspect the page and you will find a js script url in it.
- Visit the url and you will find a js script.
- The script contains a link to a gist.
- Visit the gist and you will find a function in it which takes a string as paramater.
- To get the parameter, you need visit the `/brute` endpoint.
- The endpoint displays a picture of a fortnite character.
- On inspecting this page you will find a js script url.
- Visit the url and you will find a link to a gist file.
- Visit the gist file and you will find a function which takes a string as parameter.
- Enter `BRUTUS` as the name of the character to the function and it will output another string
- Enter this string as the parameter to the first function to get the flag.
