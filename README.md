# Energise_app

#### Final QA Academy Project

## List of Contents
[Project Goals](#PG)
   * [Minimum Viable Product](#MVP)
   
[Project Management](#PM)
   * [Trello Board](#trello)  
   * [Risk Assessment](#RA)
   * [MoSCoW Priority Assessment](#MPA)
   

[Design Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)

[Development and Functionality](#Funct)
   
[Testing](#testing)
   * [Report](#report)

[Deployment](#depl)
   * [Technologies Used](#tech)
     
[Future Version Improvements](#improve)

[Key Learnings](#learn)



<a name="PG"></a>
## Project Goals
General:
To develop, test and deploy a multi service Flask application using the concept, technologies and tools of Continous Integration Pipeline.  

Specific:
Motivation: the Covid-19 lockdown has a negative impact on most people's physical activity levels. The ENERGISE APP will help people of all ages and abilities to engage in a simple, quick, fun activity.
    


<a name="MVP"></a>
### Minimum Viable Product
This project delivers the first version of the app that allows the users to randomly generate an activity to engage in.

Software development: Python, HTML
Cloud platform: GCP
Micro-service architecture: core service - service1 - front end, SQL db, Services 2-4 - back end, random object generation
Project management: Trello board
Version Control System: git
CI server: Jenkins
Deploymentcontainerisation and an orchestration tools: Docker Compose, Docker Swarm  

The final version of the Energise App will be accessible to all users who will have an option to build their own activity repositories as registered users or will be able to use the provided content. 

<a name="PM"></a>
## Project Management 

<a name="trello"></a>
### Trello Board

[Trello](https://trello.com/b/BuIqKvQV/energise-app) 
![Trello](/Documentation_Images/energise_app_trello.png)

<a name="RA"></a>
### Risk Assessment 

![Risk](/Documentation_Images/risk_register_energise_app.jpg)

<a name="MPA"></a>
### MoSCoW Priority Assessment
![MoSCoW](/Documentation_Images/energise_app_MoSCoW_Priority_Assessment_Table.jpg)
  
<a name="architecture"></a>
## Design Architecture
<a name="erd"></a>
### Entity Relationship Diagrams

![ERD](/Documentation_Images/energise_app_erd.jpg)

#### Version 1 and Future Updates
In Energise App Version 1 all users will be able to use the standard content that randomly generates an activity to perform.
The updated version of the Energise App will be allow users to register and to build their own personalised activity repositories.

<a name="Funct"></a>
## Development and Functionality
(https://github.com/Poonam1390/Energise_app) - Version Control System

![App]()
 
 
<a name="testing"></a>
## Testing
Due to time constraints only unit testing was developed, this area needs more attention at the later stages of app development.

Pytest has been used for testing.Test coverage for the backend is % 

Test coverage and example of test report:

   
<a name="depl"></a>
## Deployment
![CIPipeline](/Documentation_Images/ci_pipeline.jpg)
 
<a name="improve"></a>
## Future Version Improvements
 - Enable registered users to develop own content
 - Improve graphic design 
 - Implement more complex architecture
 - Develop unit and integration tests
- Ensure data security  

<a name="learn"></a>
## Key Learnings

Working on this project has highlighted the importance of: 
1. Incremental software development to detect and correct problems at the earliest stage 
2. Keeping the initial design simple (MVP) and gradually building the complexity 
3. The different component of CI Pipeline and their role in software development and deployment
4. Using different resources and sharing knowledge to solve problems as a team  

And, finally - it's amazing how much we have learned in the last 12 weeks! Ben and Luke - thank you for sharing your knowledge and the continous support!
