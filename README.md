# Haku: Building a Recipe Recommender

### Backgroung Information:

Ever since I was a kid I have always enjoyed tasting new foods , which lead me to try food recipes from various cultures around the world. Additionally, I was raised in a family of cooking enthusiasts, so good food was always around, but most importantly, someone was always cooking. I would sit in the kitchen and observe, asking myself why certain ingredients would mix well together. Having spent enough time observing I eventually started cooking when I was 10 years old. My passion for cooking completely changed when I attended college. During that time I was  studying engineering, a subject that further brought out my curiosity. I was constantly surprised as a student because I was able to make connections in all my classes. 
That is when I realized that the ability to make connections was a central aspect of life, as it promotes the ability to understand that symbols all round us such as letters, numbers, or even taste are essential components to understand the world.

Lizeth Aranda from Harvard Business Publishing says : “The cooking process for me is the clearest example of how we develop widely applicable skills while doing something we love. I think cooking not only develops our learning agility, but it also builds analytical skills and mathematical thinking. Among all the skills we acquire in the process of cooking, I think creativity and innovation are the most powerful.”

She says that cooking helps her disconnect and gives her the space to find new approaches at solving problem from a different perspective. This really embodies the powerful learning ability to make connections. Problem solving is the strong ability to find relationships (connections) between the resources we have and what we want to solve. I believe that grasping the idea of creating new experiences through our taste buds strengthens our ability to make connections when we try to solve a problem.

I applied that mindset to everything I was doing especially cooking. I realized that every ingredients that I had home could be combined in a certain way to create tasteful recipes. I wanted to make connections between everything I ate, because I knew that every ingredients can be matched, it was just a question of quantity and method. I believe that food can be transformed in countless ways, it is just a matter of making connections. For my project, I wanted to build a model that was able to help individuals make these connections.

### Problem Statement 

 - Only about 36% Americans cook on a daily basis. 
 - Only 13.7% prepare their meals from a passion for cooking.
 - Retirees are most likely to cook at home while individuals that work daily lack the time to do so. 
 
 
 
 The objective is to build a recommender system able to bring forth various recipes an individual can make with the ingredients they have at home. 

Because this is an unsupervised learning model, the metric of evaluation for  success will be entirely reflected on the satisfaction of the user. 

### Data Dictionary: 

|Feature|Type|Description|
|---|---|---|
|title|string|The title of the recipe|
|raw_ingredients|string|Cleaned data for ingredients|
|directions|string|Cooking directions|
link|string|Link to cooking recipe|
cosine similarity|float|Cosine similarity between ingredients and cooking recipe|

### Analysis

The web app is composed of three different models. Each models use a Word2Vec neural network tuned with the same hyper-parameters. The only thing that differentiates each models is their size. I purposely chose three different sized model in order to give the user the choice of having fast but low recommendations or slow but high recommendations.

Looking at the first model: 100,000 Recipes:

### Recommendations/ Conclusion:
The Haku prototype can be used as a tool to inspire and to try new recipes even with a limited number of ingredients we can have at home. 
As a base-model, allowing the user to choose from 3 different trained models, I am satisfied with the performance of Haku.
In order to further develop and improve the web app, I intend to work on the speed at which it outputs results. 
Work with smaller models and optimize its performance in order to deploy the app online. 
A future for Haku is a model that generates-recipes instead of matching already-existent recipes. This would be a complex and deeper investigation, but working on this project gave me an introduction to the possibilities that still exist. 

