# Autonomous-Drone-Delivery-Using-5G-AI
Team Svachalanam's submission for the ITU WTSA hackathon. 


The GitHub repository includes several subfolders and files, whose functions are described below:


Links.docx: Includes links to the submission document, as well as a screen recording of the simulated sandbox.

Python Scripts: This includes several files which aid in facilitating communication between the unity environment, as well as between the UEclient and server files. Builds upon the public work of Y.T. Elashry, whose code aided the development of Unity-Python communication.<br />

•	UdpComms.py: Python file which relays information into unity..<br />
•	Server.py: Main file which receives inputs from UEclient, and relays to UdpComms<br />
•	UEClient.py: Client-side file, relays information to server akin to a UE<br />


Simulation.unitypackage: Compiled document which includes several subfiles including scenes, assets, and other prefabs. Simulation occurs in Scenes/SimScene<br />



•	Assigner: Responsible for receiving inputs from UdpSocket, and converting into box instantiation/destruction.<br />
•	OrderCoordinator: Serves as the main task coordinator, responsible for assigning orders to drones.<br />
•	Drone.cs: Custom script within drone, responsible for interactions with payload.


Operation Instructions:

1.	Download a copy of the repository
2.	Install Unity Hub, and Unity editor 2022.3.46
3.	Open a blank project, under the 3D built-in render pipeline
4.	Go to file->open scene, and select the unity package. 
5.	Click import all.
6.	Navigate to SimScene
7.	Initialize the server.py file
8.	Press play within the unity editor
9.	Initialize the UEclient file and enter co-ordinates. It is recommended to maintain the co-ordinates between –500,-215 on the x-axis, and 60,-10 on the y-axis for both objects to avoid going out of bounds.  


