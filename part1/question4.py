import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT a.name, a.species, a.age 
FROM animals AS a 
LEFT JOIN people_animals AS p ON a.animal_id = p.pet_id 
WHERE p.owner_id IS NULL

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(DISTINCT ani.animal_id) AS pets_older  
FROM animals AS ani 
JOIN people_animals AS pa ON ani.animal_id = pa.pet_id 
JOIN people AS peo ON peo.person_id = pa.owner_id
WHERE ani.age > peo.age


"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT peo.name AS person_name, ani.name AS animal_name, ani.species
FROM animals AS ani
JOIN people_animals AS pa ON ani.animal_id = pa.pet_id
JOIN people AS peo ON peo.person_id = pa.owner_id
WHERE peo.name = 'bessie'
AND ani.animal_id NOT IN (
    SELECT pet_id
    FROM people_animals 
    WHERE owner_id != (SELECT person_id FROM people WHERE name = 'bessie')
)

"""