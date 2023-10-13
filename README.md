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
  - [Bugs](#bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Fork](#fork)
    - [Clone](#clone)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
  - [Acknowledgements (optional)](#acknowledgements-optional)

<br>

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


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
![Project summary page screenshot](/readme-images/project_summary.png)

2. Project Hypothesis
- State the poject hypothesis.
- State how the hypotheses were validated.
![Project hypothesis page screenshot](/readme-images/project_hypotheses.png)

3. Cherry Leaf Visualiser 
- Used to answer the first business requirement.
![Cherry Leaf Visualiser page screenshot overview](/readme-images/cherry_leaf_visualizer_1.png)
- The client can see the difference between average and variability image.
![Cherry Leaf Visualiser page screenshot average and variability image](/readme-images/cherry_leaf_visualizer_2.png)
- The client can see the difference between averge healthy leaf and average infected leaf.
![Cherry Leaf Visualiser page screenshot averge healthy leaf and average infected leaf](/readme-images/cherry_leaf_visualizer_3.png)
- The client can create an image montage for either healthy or infected leaves to better visualise the difference.
![Cherry Leaf Visualiser page image montage](/readme-images/cherry_leaf_visualizer_4.png)
![Cherry Leaf Visualiser page image montage result](/readme-images/cherry_leaf_visualizer_5.png)

4. Mildew Detector for Cherry Leaves
- Here the client can upload image(s) of the cherry leaves in question using the upload tool which accepts PNG and JPEG formats.
![Mildew detector page screenshot](/readme-images/mildew_detector_1.png)
- After the upload, the client will be provided with the results which includes: the image(s) uploaded, a statement stating whether the leaf is infected or not, a bar plot of the result(probability of the diagnostic), a table with the image name and the result for it, and a link to download the image as a .csv file.
![Mildew detector page results screenshot](/readme-images/mildew_detector_2.png)

5. Model Performance
- Shows a bar plot with label frequencies for Train set, Test set, and Validation set.
- Shows the hostory of model training accuracy and losses.
![Model performance page screenshot](/readme-images/model_performance_1.png)
- Shows the model performance evaluation table.
![Model performance page screenshot 2](/readme-images/model_performance_2.png)

## Bugs
- Montage was not being created. Issue was with dir_path in the function where I did not add validation folder. 
- Issues with Image.ANTILAS. Solved by adding pillow<10 to requirements.txt. I tried Image.Lancosz but it did not solve the issue.
- Issues with markdown for download report. Solved by correcting the tags.

## Unfixed Bugs
* The page_icon does not appear on the website despite being in the correct format. This does not affect the functioanlity of the dashboard in any way. 

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

### Fork
1. Log in with your Github account or make one if you don't have one. 
2. Find the repository: mildew_detection.
3. Click the Fork button on the top right corner.

### Clone 
1. Log in with your Github account or make one if you don't have one. 
2. Find the repository: mildew_detection.
3. Click the **Code** button next to the Gitpod button and **copy** the HTTPS link. 
4. Open the terminal. 
5. Make sure that the current directory is the one where you want the cloned repository to be. 
6. Use the command ```git clone``` and paste the link. 
7. Press Enter. Now the repository is cloned. 


## Main Data Analysis and Machine Learning Libraries
* NymPy: Used to convert images into arrays and manipulate arrays.
* Pandas: Used to structure data and to convert it as dataframes.
* Matplotlib: Reading, processing, and displaying image data along with producing graphs of tabular data.
* Seaborn: Visualise and present the data with different plots.
* Plotly: Used to create interactive charts seen on dashboard.
* KerasTuner: Setting and tuning model's hyperparameters.
* TensorFlow: Machine Learning library used to create the model.
* Streamlit: Used to build the dashboard. 
* Scikit-learn: Used to evaluate the model and calculating class weights to handle target imbalance. 
* PIL: Imaging library used to manipulate images uploaded to the dashboard. 

Other tools:
- Codeanywhere: Online IDE.
- GitHub: To store project code and files.
- Heroku: Used to deploy the dashboard.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content

- [Wyman's Home & Garden](https://wymangardens.com/blog/57740/powdery-mildew-and-how-to-control-it#:~:text=As%20the%20infection%20spreads%2C%20the,plant%2C%20but%20that%20is%20rare.) for the information about Powdery Mildew.
- CI Malaria Detector project for structure.
- [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf) to help with model creation. 
- [Streamlit documentation](https://docs.streamlit.io/library/get-started) to create the dasboard and for syntax purposes.


## Acknowledgements (optional)
* Mo Shami for answering and providing me with useful resources and feedback.
