<p align="center">
  <img src="https://github.com/frankchang1000/ShooterStopper/blob/main/docs/ShooterStopperlogo.png", width="300"/>
</p>
# ShooterStopper

Ensuring **safety** for students using live security feeds and advanced AI.

## Table of Contents 🧾
* [Why ShooterStopper](#why-shooterstopper)
* [How it Works](#how-it-works-)
* [Installation and Usage](#installation-and-usage-)
* [Challenges](#challenges-)
* [Accomplishments](#accomplishments-)
* [How can we improve?](#how-can-we-improve-)
* [License](#License)

## Why ShooterStopper❓

**June 3rd is National Gun Violence Day** and our team wanted to spread awareness by creating ShooterStopper to prevent more innocent lives from being lost due to school shootings. Futhermore, we want to prevent the grief that loved ones of victims experience from the irreversible damage.

<p align="center">
  <img src="https://github.com/frankchang1000/ShooterStopper/blob/main/docs/slides/statistics.png", width="800"/>
</p>

The Everytown Research Organization conveys the absurd amount of shootings in the past decade, we are targeting to reduce the number of school shootings that contain casualties and injuries to reinforce the idea of going to school safely students and parents.

## How it Works 💻
<p align="center">
  <img src="https://github.com/frankchang1000/ShooterStopper/blob/main/docs/slides/howitWorks.png", width="800"/>
</p>

## Installation and Usage ✅

Before beginning installation, ShooterStopper wants to ensure the privacy of our users and want to highlight that we detect **objects rather than people.**

### Installation ⚙️

First follow the following steps **using POWERSHELL and not CMD** (works on Windows 10 and 11; different commands required for Unix and Linux systems).

```python
git clone https://github.com/frankchang1000/ShooterStopper.git
cd ShooterStopper
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

## Challenges 👎

When we first planned ShooterStopper, we originally wanted to implement the Ring API in our project that we later found inaccessible. We improvised and used webcam cameras to simulate a security camera, but we soon found the resolution and frames of the camera quality were poor as we found some input lag.



## Accomplishments 🎆

Despite our setbacks, we are proud to create a working product that delivers our stance on how to defend school shootings as school shootings have been a major conflict this decade. We are proud to face this problem with an efficent and working method with our AI training and model that can detect items instantly and compare how simular an item is to an weapon.

We also take pride in implementing **CockroachDB's** database in our project.

## How can we Improve? 🤔

In the future, ShooterStopper hopes to expand by implementing an instant notifying of law enforcement or police when a gun is spotted. Also in the future, we wish to use better cameras so we can have a detection on a weapon for 10+ frames on camera. As for now, the input delay makes movement blurry and laggy. We also hope to use TFlite for improved tracking speed.

## License

Copyright 2022 ©Frank Chang, Thomas Chia, Ryan Dadoo, Stephen Tsai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
