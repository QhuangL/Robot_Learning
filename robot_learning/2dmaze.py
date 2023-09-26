# -*- coding: utf-8 -*-
"""mecs6616-Spring2023-Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6sQoGdNwmxTeIIM9eSgu3sLmJ_vmUGH

# ***Important***

**Before starting, make sure to read the [Assignment Instructions](https://courseworks2.columbia.edu/courses/172081/pages/assignment-instructions) page on Courseworks2 to learn the workflow for completing this project.**

# Introduction

This project aims to demonstrate how classical machine learning methods can be used in robotics setting. In this project, we will be working on a navigation agent that navigates inside a simple 2D maze.

<div>
<img src="https://drive.google.com/uc?id=1mSpegY1psdek3Lgh6cxzcCGUCF-lddnV" width="300"/>
</div>


The image above shows the simulation world. The "robot" (also called "agent") is shown by the green dot. The goal location is shown by the red square. The aim of the agent is to navigate to the goal.

The ultimate goal in this project is to learn an appropriate behavior for the agent by imitating demonstrations from an expert user. These demonstrations have been collected by a human controlling the agent via a keyboard, and will be provided to you as training data.

Note that in this project we are explicitly not allowing the use of Deep Learning or Reinforcement Learning. We will be using these in future projects, which will allow us to see what significant benefits these technologies bring. Until then, this project is restricted to "traditional" supervised learning.

The library you should use for the learning algorithms is scikit-learn. Its general use, as well as individual functions, are extensively documented on the [scikit-learn page](https://scikit-learn.org/stable/)

This project has 3 parts. The instructions for each part are below.

# Part 0. Project Setup (do NOT change)


***IMPORTANT:***
- Do NOT install any other dependencies or a different version of an already provided package. You may, however, import other packages. Note that scikit-learn is already installed in colab
- your code should go in the "Solutions" section. (You can minimize sections with the arrows on the left.)

You will be accessing data files located in a class github repo. The following cell clones the repo into the working directory
"""

# do NOT change

# After running this cell, the folder 'robot-learning-S2023' will show up in the file explorer on the left (click on the folder icon if it's not open)
# It may take a few seconds to appear
!git clone https://github.com/roamlab/robot-learning-S2023.git

# do NOT change

# copy all needed files into the working directory. This is simply to make accessing files easier
!cp -av /content/robot-learning-S2023/project1/* /content/

# do NOT change

!pip install pybullet

"""# Solutions (enter solutions here)

## Part 1. Inferring the position of an agent with RGB images

<div>
<img src="https://drive.google.com/uc?id=1Cn2sAcz0sOXX5x1dvRCEtKCL5yJDYkKS" width="300"/>
</div>

The first task is to learn to infer where the agent is inside the maze based on RGB image observations like the one shown above. Each such observation will consist of an RGB image of size [64, 64] for each color channel, so the total size of each observation is [64, 64, 3].

The maze has its own coordinate system, in which the agent's location must be expressed. You will be provided with RGB image observations in this environment, as well as the groundtruth location of the agent in each image, expressed in the maze coordinate system. The task is to learn a model that can predict the location of an agent given this RGB observation.

Note that this can be seen as a regression problem (if the location of the agent is a continuous variable) or a classification problem (if we discretize the output space to a finite number of possible locations).

In this part, you will need to implement the class PositionRegressor. Your class will need to implement two methods to get a score. The methods to implement are documented below.

We will test the performance of your model in this part using mean square error (MSE) between the predicted positions and the groundtruth. We will perform this evaluation on both the training data which is provided to you, and which your model will be training with, and on some additional testing data that is held out. Your score will be: score = 1 - MSE and then clipped between 0 and 1.

Please implement your solution below. You should fill in the two functions in the cell below. Our scoring code will then load the data from file and call your functions, passing them the appropriate arguments.
"""

# enter solution for part 1 here

import numpy as np

class PositionRegressor():

    """ Implement solution for Part 1 by filling in the functions below  """

    def train(self, data):
        """A method that trains a regressor with given data

           Args:
               data: a dictionary that contains images and the groundtruth location of
                     an agent.
           Returns:
               Nothing
        """

        # for key, val in data.items():
            # print(key, val)
        print("Using dummy solution for PositionRegressor")
        pass

    def predict(self, Xs):
        """A method that predicts y's given a batch of X's

           Args:
               Xs: a batch of data (in this project, it is in shape [batch_size, 64, 64, 3])
           Returns:
               The fed-forward results (predicted y's) with a trained model.
        """

        return np.zeros((Xs.shape[0], 2))

"""## Part 2. Behavioral cloning with low dimensional data

In this part, your model is asked to determine what action the agent should take, based on an observation from its environment. The action can be one of three choices: go up, go left, or go right. The goal of the agent is to reach the goal squre, shown in red in the images above.

Note that, in general terms, what you are providing here is a "policy" - a model that selects an action based on observations from the world. Numerous methods are available for training policies, and we will cover many of them in the Reinforcement Learning part of the class.

However, learning a policy can also sometimes be a Supervised Learning problem: you will be provided with labeled examples from an "expert". Each labeled example will contain a tuple of the form $(o, a)_i$, where $o$ represents an observation and $a$ represents the  action taken by the expert given that observation. You must simply learn to imitate the expert, a process also known as behavioral cloning. If the action space is discrete, then behavioral cloning is a classification problem and if the action space is continuous, it will be a regression problem.

In this project, we will be working on an environment with a discrete action space, so we can see behavioral cloning as a classification problem with three output classes (go up, go left, go right). While the action space is the same in Parts II and III, the nature of the observation used in each case will be different.

In Part II, the observation will consist of the ground truth position of the agent in the maze coordinate system. Training data will thus contain tuples $(o, a)_i$  where $o$ is the agent's location in the maze, and $a$ is the action taken by the expert at that location. You can use any classification method from Scikit-learn to learn the mapping between observations and actions.

In this part, you will need to implement the class PositionRegressor. Your class will need to implement two methods to get a score. The methods to implement are documented below.

In this part, you will need to implement the class POSBCRobot(). The methods to implement are documented below.

In this part, we will evaluate your model by simply having the robot follow the commands that it provides, or, in other words, "rolling out your policy" in the environment. After 20 steps, we will evaluate how close to the goal the robot has ended up. Formally,  the score for a single run will be calculated based on the minimum distance between your agent and the target location achieved over a trajectory of 100 steps. We will run your agent for 20 times in the environment and use the following formula to calculate your score: score = $\frac{(Init\_dist -  min\_dists)/20}{Init\_dist}$.

Please implement your solution below. You should fill in the two functions in the cell below. Our scoring code will then load the data from file and call your functions, passing them the appropriate arguments.
"""

# enter solution for part 2 here

import numpy as np

class POSBCRobot():

    """ Implement solution for Part 2 by filling in the functions below """

    def train(self, data):
        """A method for training a policy.

            Args:
                data: a dictionary that contains X (observations) and y (actions).

            Returns:
                This method does not return anything. It will just need to update the
                property of a RobotPolicy instance.
        """

        # for key, val in data.items():
            # print(key, val.shape)
        print("Using dummy solution for POSBCRobot")
        pass

    def get_actions(self, observations):
        """A method for getting actions. You can do data preprocessing and feed
            forward of your trained model here.

            Args:
                observations: a batch of observations (images or vectors)

            Returns:
                A batch of actions with the same batch size as observations.
        """

        return np.zeros(observations.shape[0])

"""## Part 3. Behavioral cloning with visual observations

In this part, you asked to do a similar task as Part II, but the observations will be a lot more challenging to use. Instead of being provided with the actual robot location, your model will receive as input RGB image observations of the world, similar to the ones you used to do localization in Part I.

All requirements from your code, as well as the evaluation method, are unchanged compared to Part II. The only difference is the nature of the observation that is provided to you.

Please implement your solution below. You should fill in the two functions in the cell below. Our scoring code will then load the data from file and call your functions, passing them the appropriate arguments.
"""

# enter solution for part 3 here

import numpy as np

class RGBBCRobot():

    """ Implement solution for Part3 by filling in the functions below """

    def train(self, data):
        """A method for training a policy.

            Args:
                data: a dictionary that contains X (observations) and y (actions).

            Returns:
                This method does not return anything. It will just need to update the
                property of a RobotPolicy instance.
        """

        # for key, val in data.items():
            # print(key, val.shape)
        print("Using dummy solution for RGBBCRobot")
        pass

    def get_actions(self, observations):
        """A method for getting actions. You can do data preprocessing and feed
            forward of your trained model here.

            Args:
                observations: a batch of observations (images or vectors)

            Returns:
                A batch of actions with the same batch size as observations.
        """

        return np.zeros(observations.shape[0])

"""# Testing

We will be using the cells below to auto-generate your score for this project. To see how you are doing with the project, simply run the cells below.

If you would like to visualize your policy just set gui_enable to True. This will generate an animated .png file which can be visualized with the cell at the end of the notebook. Note that this does take a little bit longer to run.

The solution cells provided to you return zeros. You are required to update them with your solutions.



**Grading Rubrics**

You are graded based on the scores you achieved for each part. Each part is 5 points and the final grade you get for this project is the sum of all points from three parts (thus, 15 maximum in total)

**Part 1**

- score >= 0.99, you get 5/5
- score >= 0.95, you get 4/5
- score >= 0.80, you get 2/5

**Part 2**

- score >= 0.99, you get 5/5
- score >= 0.80, you get 3/5

**Part 3**

- score >= 0.99, you get 5/5
- score >= 0.90, you get 4/5
- score >= 0.80, you get 3/5
- score >= 0.60. you get 2/5

### Turn GUI on/off (you may change) -- **please set to False before submission**
"""

# Enabling the gui saves animated pngs to the working directory
# You can view the pngs using the cell at the bottom of the notebook
# Code runs slightly slower when gui is enabled

gui = False

"""### Score Policy (do NOT change)"""

# do NOT change

!pip3 install numpngw

# do NOT change

from score_policy import *
score_all_parts(POSBCRobot(), RGBBCRobot(), PositionRegressor(), gui_enable=gui)

"""### Show GUI (optional, you may change)"""

from IPython.display import Image
# Image(filename='pos_bc_anim.png', width=200, height=200)
# Image(filename='rgb_bc_anim.png', width=200, height=200)

