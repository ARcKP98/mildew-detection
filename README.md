# Powdery Mildew detector in Cherry Leaves

![Am I Responsive screenshot](/readme-images/am_i_responsive.png)
The [link](https://cherry-leaf-powdery-mildew-7270464476a9.herokuapp.com/) to the live project
<br>
This is a Machine Learning(ML) project which focuses on detecting powdery mildew on cherry leaves to determine whether a leaf is healthy or infected. This project is a result of a business request made by a fictitious company called Farmy & Foods who have an issue with powdery mildew infecting their cherry plantation. 

<br>

## Contents
- [Powdery Mildew detector in Cherry Leaves](#powdery-mildew-detector-in-cherry-leaves)
  - [Contents](#contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements (optional)](#acknowledgements-optional)

<br>

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
1. Cherry leaves that have been affected by powdery mildew will have white or gray powdery regions/spots on the surface of the leaf.

Validation: An image montage of the cherry leaves can be generated to identify the differences in healthy and infected leaves.

2. Cherry leaves that have been affected by powdery mildew will also have some discoloration on parts of the leaf(the stem, the edges, the center, etc.) with distorted edges.

Validation: An image montage along with the average image difference of healthy and infected leaves can be used to identify the differences in the healthy and infected leaves structure and colour. 


## The rationale to map the business requirements to the Data Visualisations and ML tasks
The first business requirement states that: *The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew*. This requirement will be satisfied by visualising the data which includes: 
* Showing an image montage of healthy or infected leaves.
* Showing the difference between an average healthy leaf and an average infected leaf.
* Showing the average and variability of images for healthy and infected leaves.

The second business requirement states that: *The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew*. This requirement will be satisfied by:
* Allowing the user to add images to the dashboard which predict whether the image(s) is healthy leaf or an infected leaf.
* Allow the user to generate report based on the predictions.

## ML Business Case
* The client is interested in having a tool that can be used to detect whether a given cherry leaf is healthy or infected with powdery mildew. 
* This will save client a lot of time as examining each cherry tree takes 30 minutes plus and additional minute which is required to apply the compund to the cherry leaf if it is infected.
* A Binary Classification ML model will be constructed to predict whether the cherry leaf is healthy or not.
* The client has agreed that performance goal of the predictions should be 97%.
* The client has requested a dashboard with this functionality. 
* The dataset will be provided by the client which will be used to train the model. 


## Dashboard Design
The clients requirements can be implemented in the following 5 pages:
* Project Summary
* Project Hypothesis
* Cherry Leaf Visualiser
* Mildew Detector for Cherry Leaves
* Model Performance

1. Project Summary
- General information about the project. 
- Introduce the problem and the business requirements.

2. Project Hypothesis
- State the poject hypothesis.
- State how the hypotheses were validated.

3. Cherry Leaf Visualiser 
- 

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
