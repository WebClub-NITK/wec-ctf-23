# **Can You Break In?**

Category: WEB

Author: Dhruva

Answer / Flag: `WEC{N3V3r_G0nNa_g1v3_Y0u_Up}`

## Problem Statement

You have been asked to break into a website but it's not simple. The website is password protected and only the owner can access the website and now it's on you to get in!!

Here's what we know about him :
<ul>
    <li> He's pretty basic and has a gmail account</li><br>
    <li> Nobody knows his real name but we have an encrypted version of what might be his name: <i><b> YPJRHZASLF</b></i></li><br>
    <li> He also also thinks of himself as a memelord. His favourite number is a five digit number made of two legendary numbers</li>
</ul>

Given the information, what do you think might be his email? Also, do you really need a password to login?

## Relevant files / links

Docker image of the website `docker pull dhruv693/wec_ctf_web_q:latest`

## Hint

Vaccines ? Think more malicious

## Solution

<ul>
 <li>The actual name of the owner is <b><i>RICKASTLEY</i></b>. When shifted with a key 7 it results in <i><b> YPJRHZASLF</b></i> and the five digit number is 69420, so the email required is : <i>rickastley69420@gmail.com</i></li>

 <li>Then they need to use an SQL injection to break into the website
<pre><code>rickastley69420@gmail.com' OR '1' = '1</code></pre>
Password isn't required to gain access.</li>
<li>Then they are redirected to a page with the url ending with 
<b>V0VDe04zVjNyX0cwbk5hX2cxdjNfWTB1X1VwfQ==</b>  which is the base64 encryption of the flag!
</ul>
