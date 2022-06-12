# Movie Recommender

<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<a href="https://movie-recommender-sarang.herokuapp.com/"><img src="https://github.com/Git-Sarang/movie-recommender/blob/main/static/movie-rec-1.png" alt="Website-Link" /></a>

<div id="tags" align="center">
<a href="https://www.linkedin.com/in/sarang-rawat-a4aa30231"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
<a href="mailto:sarangrawat05@gmail.com?subject=Hi%20Sarang"><img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>&nbsp;
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#deployment">Deployment</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

To open the website click on the project image provided above. Once the webpage loads, type in the Movie of your choiceand click the 'Recommend' button to get top 5 similar recommendations.
This is Data Science & Machine Learning project. This project is natively written in python. 
Data sources:
* Kaggle
* MovieDB
* DatasetSearch

The main data collected had to be cleaned and organised on the basis of movie_ID. Duplicates had to be deleted.

<a href="https://www.kaggle.com/tmdb/tmdb-movie-metadata">TMDB Movies Dataset</a>
_(not included in the repository as it was over 100mbs)_


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [Tensorflow](https://www.tensorflow.org/)



<!-- GETTING STARTED -->
## Getting Started

Prior Knowledge of python and command line is required.

### Prerequisites
Dependencies that need to be installed
* Pandas
  ```sh
  pip install pandas
  ```
* Tensorflow
  ```sh
  pip install tensorflow
  ```
* Streamlit
  ```sh
  pip install streamlit
  ```
* Requests
  ```sh
  pip install requests
  ```

### Deployment

_The model is deployed in a minimalist website design. It is hosted on Heroku._

1. The frontend is made by the _streamlit_ library in python.
2. It can be locally run using the command
   ```sh
   streamlit run app.py
   ```
3. Command file is made by the name 'Procfile'. This contains the bash commands for the Heroko server.
  
4. Finally all files are pushed to the Heroku server.

<a href="https://movie-recommender-sarang.herokuapp.com/">Movie Recommender</a>


### Connect With Me
<div id="tags" align="center">
<a href="https://www.linkedin.com/in/sarang-rawat-a4aa30231"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
<a href="mailto:sarangrawat05@gmail.com?subject=Hi%20Sarang"><img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>&nbsp;
</div>


<p align="center">
Made with 💖 by Sarang</p>
