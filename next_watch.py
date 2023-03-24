import spacy


nlp = spacy.load('en_core_web_md')

given_description =  "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                     "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk " \
                     "can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery " \
                     "and trained as a gladiator. "

with open('movies.txt', 'r') as file: # Open the file and read each line into a list
    movies_list = file.readlines()

movies_dict = {} # Create an empty dictionary

# Loop through list and store the first 7 chars (Movie A) as the key
# and the description (indices 9 - -1) as the value in the dictionary
for line in movies_list:
    movie = line[:7]
    desc = line[9:-1]
    movies_dict[movie] = desc


def most_similar(dict, compare_desc):
    """
    A function that takes in a dictionary of movies and their descriptions and a description to compare to
    and returns the movie in the dictionary with the most similar description.

    :param dict: A dictionary of movie names and descriptions
    :param compare_desc: The movie description to compare the similarity to
    :return: The movie name with a description most similar to the given description
    :rtype: STR
    """
    model_desc = nlp(compare_desc)

    for movie in dict:
        similarity = nlp(dict[movie]).similarity(model_desc)
        dict[movie] = similarity

    return (max(dict, key=dict.get))


print(f"The movie most similar to Planet Hulk is : {most_similar(movies_dict, given_description)}")
