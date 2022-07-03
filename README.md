# Path Finder Visualization
This is a personal project I created intended to learn more about various pathfinding algorithms by seeing their strengths and weaknesses in different types of mazes. This project was created using python pygame and visualizes depth-first search, breadth-first search, and A* pathfinding in user-created mazes and pathfinding scenarios. Please email me at 3069391@gmail.com or comment on this project page should you have any questions about the visualizer, suggestions for further improvement, or have found any bugs.

## Screenshots 
<div style="display: flex">
<img src="https://user-images.githubusercontent.com/82241006/177055972-4c30bccc-39ee-4c27-ba9d-dfedaf38445a.png" alt="start page" width="400"/>
<br>
<br>
<img src="https://user-images.githubusercontent.com/82241006/177056008-82dfefaf-d5e6-40ad-97cd-1abef8abad73.png" alt="start page" width="400"/>
<img src="https://user-images.githubusercontent.com/82241006/177056053-876f53d4-e82d-48bb-b278-d54d030f3c91.png" alt="start page" width="400"/>
<img src="https://user-images.githubusercontent.com/82241006/177056063-0cea4718-81b7-4604-a578-8458c225f790.png" alt="start page" width="400"/>
<br>
<br>
</div>
![image](https://user-images.githubusercontent.com/82241006/177056063-0cea4718-81b7-4604-a578-8458c225f790.png)
 

## Setup Instructions
1. First, download the source code, either by executing a `git clone https://github.com/x2dtu/path-finder.git` in a terminal or downloading the project as a zip through the Github page and extracting that zip.
2. This project uses python3 and a python library called pygame. In order to play, make sure you have python3 installed. In a terminal in the project working directory, you can run `pip install -r requirements.txt` to install the necessary pygame library. 
3. Finally, run `python3 path_finder.py` in the project directory in order to start playing the game. Good luck!

## Objective and Controls
In this visualizer, you can select any of three different pathfinding algorithms: breadth-first search, depth-first search, or A*. You can also choose whether or not these algorithms consider squares to be adjacent to the squares diagonal of it. See how these different algorithms react as barriers are put up to block their path! <br>
<br>
The starting menu explains the controls and how to play. Regardless, here is a description of how to use this visualizer. Click a path finding algorithm to continue. You can also select whether or not the algorithm can use diagonals or not. Once a path finding algorithm has been selected, left click any of the grid tiles to select a starting point (blue color), then left click again to select an endpoint (orange color). Left clicking more will add black barriers that the algorithm can't go through. Right clicking any tile will reset it. Once the start and end points have been selected, the algorithm can be started by hitting the spacebar. Upon activation, the algorithm will attempt to form a path from the start point to the endpoint, coloring active tiles under consideration green and traversed tiles red. If it finds a path, it will color the path purple. You can clear the board entirely by pressing the c key, you can clear everything but the barriers with the x key, and you can come back to this menu by pressing the escape key. You can also press the a key to switch to the A* algorithm, the b key to switch to the BFS algorithm, and the d key to switch to the DFS algorithm. Finally, you can press the r key to randomly add barriers and the start and endpoints if those aren't already added, and you can quit by pressing the q key.
