#!/usr/bin/env python
# coding: utf-8

# # L9: Building LLM prompts with variables

# In the next cell, you will import the function `print_llm_response` that uses an LLM with an instruction that you provide as a string and displays the result.

# In[1]:


from helper_functions import print_llm_response


# Basically, you can use that function as if you were asking a chatbot. You just need to provide your instructions as a string. For instance, you can ask "What is the capital of France?" using the following code:

# In[2]:


print_llm_response("What is the capital of France?")


# Let's ask the LLM for the lifestyle description for Otto Matic, whose name is stored in `name`, if he were a `dog_age` years old dog.

# In[3]:


name = "Otto Matic"
dog_age = 21/7


# In[4]:


print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
Describe what life stage that would be for a dog and what that might 
entail in terms of energy level, interests, and behavior.""")


# <b>You just used AI with your own variables!</b> You used an LLM with instructions that included variables you defined in this notebook.
# 
# <b>Congratulations 🎉🎉🎉</b>

# ## Variable names restrictions

# The following variable names also have some problems. Try to fix them yourself or use the help from the chatbot.

# In[6]:


driver = "unicorn"
drivers_vehicle = "colorful, asymmetric dinosaur car"
favorite_planet = "Pluto"


# Now, update the next cell with any changes you made in the previous cell.

# In[7]:


print_llm_response(f"""Write me a 300 word children's story about a {driver} racing
a {drivers_vehicle} for the {favorite_planet} champion cup.""")


# ## Extra practice
# 
# Try the exercises below to practice the concepts from this lesson. Read the comments in each cell with the instructions for each exercise.
# 
# <b>Feel free to use the chatbot if you need help.</b>

# In[14]:


# Fix this code
one_favorite_book = "1001 Ways to Wear a Hat"
second_fav_book="2002 Ways to Wear a Scarf" 
print(f"My most favorite book is {one_favorite_book}, but I also like {second_fav_book}")


# In[15]:


# Make variables for your favorite game, movie, and food.
# Then use print_llm_response to ask the LLM to recommend you
# a new song to listen to based on your likes.

favorite_game= "cricket"
favorite_movie ="crimsston tide"
favorite_food = "biriyani"

print_llm_response(f"My most favorite game is {favorite_game}, favorite movie is {favorite_movie} and favorite food is {favorite_food}")


# In[ ]:




