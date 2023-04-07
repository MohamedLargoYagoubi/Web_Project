# **WEB PROJECT: SOCCER SITE**

![banner](https://github.com/MohamedLargoYagoubi/images/blob/main/PROJECT%20WEB.gif)
 **✰ INTRODUCTION ✰**

We are a group of students from the [University of Lleida](http://www.udl.cat/ca/) (UDL) and have developed a soccer website using [Django](http://www.udl.cat/ca/) and other technologies such as [Docker](https://www.docker.com/) or [Fly](https://fly.io/).
You will be able to see the leagues, teams and players that have been created. In addition, you will have an administrator option to modify, delete or add new elements.

**✰ INTRUCTIONS FOR DEPLOYING THE PROJECT ✰** 
> Note: You must have [Docker](https://www.docker.com/products/docker-desktop/) installed.
 1. Clone the repository from Github by running the following command in your terminal or command prompt:

    `git clone https://github.com/MohamedLargoYagoubi/Web_Project.git`
 2. Navigate to the cloned directory using the `cd` command until you reach the project root directory (until you reach the directory containing the `manage.py` file):

    `cd .\Web_Project\futbol\`

 3. Build the Docker image by running the following command:

    `docker-compose build`
 4. Start the Docker containers by running the following command:
 
    `docker-compose up`
 5. Wait for Docker Compose to build and start the containers. Once the process is complete, you should be able to access the web application by going to `http://localhost` in your web browser.
 6. To stop the Docker containers, press `Ctrl+C` in your terminal or command prompt, or run the following command:

    `docker-compose down`

**✰ INTRUCTIONS FOR DEPLOYING THE PROJECT ✰** 

⚠️ TODO ⚠️

**✰ GROUP MEMBERS ✰** 
- Sergi Fernández Espona
- Alex Gonzalez Toré
- Mohamed Largo Yagoubi
- Ian Portolés Vilalta
