# Tetris-Game

A simple Tetris game implemented in Python using the Pygame library.

## Table of Contents

- Introduction
- Features
- Installation
- Controls
- Known Problems
- License

## Introduction

This project is a very simple Tetris game developed in Python with the Pygame library. It provides a classic Tetris gaming experience with falling blocks that the player can manipulate to create complete lines.

## Features

- Tetris block manipulation (move left, move right, rotate, move down)
- Simple scoring system
- Classic Tetris block shapes (O, I, S, Z, L, J, T)
- Pygame-based graphical interface

## Installation
Please download the main.exe and logo.png in the release. Put them in a folder and run the exe file to start the game.

## Controls
- Up Arrow: rotates the Tetris block
- Left Arrow: moves the Tetris block left
- Right Arrow: moves the Tetris block right
- Down Arrow: makes it drop faster

## Known Problems
There are several known problems with this program. 
- Sometimes, once a row is completed, it will delete more than that filled-out row.
- Sometimes it will leave artifacts of a row already deleted and once another Tetris block touches it, the artifact disappears.
- Another problem is that there is no game over the screen, if you put too many Tetris blocks and it goes past the top screen the program just doesn't do anything.
- Another problem is that if you keep holding the down arrow button after the Tetris block has reached the bottom, it won't let another new block spawn until you let go.
