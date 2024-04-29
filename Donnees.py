from faker import Faker
import unicodedata
import random
import os

# faire attention au niveau des num etudiants selectionné pour les ue et etc cela doit pas etre la liste des num de utilisateur valide

fake = Faker('fr_FR')

# Définir le chemin de sortie pour les fichiers texte
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ids_universite = []

# Générer des données pour la table universite
def generate_universite():
    data = []
    generated_ids = set()  # Utiliser un ensemble pour stocker les identifiants déjà générés
    with open(os.path.join(output_dir, 'universite.txt'), 'w') as f:
        for _ in range(10):
            id_universite = fake.unique.random_int(min=1, max=10)
            while id_universite in generated_ids:  # Vérifier si l'identifiant est déjà généré
                id_universite = fake.unique.random_int(min=1, max=10)  # Regénérer un nouvel identifiant
            generated_ids.add(id_universite)  # Ajouter l'identifiant à l'ensemble des identifiants générés
            label = fake.company()
            label = label.encode('UTF-8')
            # Formatage de l'instruction INSERT INTO
            f.write(f"INSERT INTO universite (id_universite, label) VALUES({id_universite}, '{label}');\n")
            data.append((id_universite, label))
            ids_universite.append(id_universite)
    return data

nums_etudiant_valide = []

# Générer des données pour la table utilisateur_valide
def generate_utilisateur_valide():
    data = []
    with open(os.path.join(output_dir, 'utilisateur_valide.txt'), 'w') as f:
        for _ in range(100):
            num_etudiant = fake.unique.random_int(min=20001001, max=20240324)
            nom = fake.last_name()
            prenom = fake.first_name()
            mail_utilisateur = fake.email()
            role = fake.random_element(elements=('etudiant', 'professeur', 'administratif'))
            id_universite = random.choice(ids_universite)
            f.write(f"INSERT INTO utilisateur_valide (num_etudiant, nom, prenom, mail_utilisateur, role, id_universite) VALUES ({num_etudiant}, '{nom}', '{prenom}', '{mail_utilisateur}', '{role}', {id_universite});\n")
            data.append((num_etudiant, nom, prenom, mail_utilisateur, role, id_universite))
            nums_etudiant_valide.append(num_etudiant)
    return data

ids_utilisateur = []

nums_etudiant = []

# Générer des données pour la table utilisateur
def generate_utilisateur():
    data = []
    with open(os.path.join(output_dir, 'utilisateur.txt'), 'w') as f:
        for _ in range(50):  
            num_etudiant = random.choice(nums_etudiant_valide)
            mdp = fake.password()
            #recuperer la liste des num_etudiant de la table utilisateur_valide
            id_utilisateur = fake.unique.random_int(min=100000, max=999999)
            f.write(f"INSERT INTO utilisateur (num_etudiant, mdp, id_utilisateur) VALUES ({num_etudiant}, '{mdp}', {id_utilisateur});\n")
            data.append((num_etudiant, mdp, id_utilisateur))
            ids_utilisateur.append(id_utilisateur)
            nums_etudiant.append(num_etudiant)
    return data

ids_ue = []
# Générer des données pour la table ue
def generate_ue():
    data = []
    with open(os.path.join(output_dir, 'ue.txt'), 'w') as f:
        for _ in range(50):  
            id_ue = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            f.write(f"INSERT INTO ue (id_ue, label) VALUES ({id_ue}, '{label}');\n")
            data.append((id_ue, label))
            ids_ue.append(id_ue)
    return data

# Generer des données pour la table enseignants_ue
def generate_enseignants_ue():
    data = []
    with open(os.path.join(output_dir, 'enseignants_ue.txt'), 'w') as f:
        for _ in range(50):  
            id_utilisateur = random.choice(ids_utilisateur)
            id_ue = random.choice(ids_ue)
            f.write(f"INSERT INTO enseignants_ue (id_utilisateur, id_ue) VALUES ({id_utilisateur}, {id_ue});\n")
            data.append((id_utilisateur, id_ue))
    return data

ids_formation = []
# Générer des données pour la table formation
def generate_formation():
    data = []
    with open(os.path.join(output_dir, 'formation.txt'), 'w') as f:
        for _ in range(20):  
            id_formation = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            id_universite = random.choice(ids_universite)
            f.write(f"INSERT INTO formation (id_formation, label, id_universite) VALUES ({id_formation}, '{label}', {id_universite});\n")
            data.append((id_formation, label, id_universite))
            ids_formation.append(id_formation)
    return data

# Générer des données pour la table formation_ue
def generate_formation_ue():
    data = []
    with open(os.path.join(output_dir, 'formation_ue.txt'), 'w') as f:
        for _ in range(50):  
            id_formation = random.choice(ids_formation)
            id_ue = random.choice(ids_ue)
            f.write(f"INSERT INTO formation_ue (id_formation, id_ue) VALUES ({id_formation}, {id_ue});\n")
            data.append((id_formation, id_ue))
    return data

def generate_promotion():
    data = []
    with open(os.path.join(output_dir, 'promotion.txt'), 'w') as f:
        for _ in range(50):
            id_utilisateur = random.choice(ids_utilisateur)
            id_formation = random.choice(ids_formation)
            annee = fake.year()
            f.write(f"INSERT INTO promotion (id_utilisateur, id_formation, annee) VALUES ({id_utilisateur}, {id_formation}, '{annee}');\n")
            data.append((id_utilisateur, id_formation, annee))
    return data

ids_chapitre = []

# Générer des données pour la table chapitre
def generate_chapitre():
    data = []
    with open(os.path.join(output_dir, 'chapitre.txt'), 'w') as f:
        for _ in range(50):
            id_chapitre = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            id_ue = random.choice(ids_ue)
            f.write(f"INSERT INTO chapitre (id_chapitre, label, id_ue) VALUES ({id_chapitre}, '{label}', {id_ue});\n")
            data.append((id_chapitre, label, id_ue))
            ids_chapitre.append(id_chapitre)
    return data

# Générer des données pour la table chapitre_chapitre
def generate_chapitre_chapitre():
    data = []
    with open(os.path.join(output_dir, 'chapitre_chapitre.txt'), 'w') as f:
        for _ in range(50):
            id_chapitre = random.choice(ids_chapitre)
            id_chapitre_suivant = random.choice(ids_chapitre)
            f.write(f"INSERT INTO chapitre_chapitre (id_chapitre, id_chapitre_suivant) VALUES ({id_chapitre}, {id_chapitre_suivant});\n")
            data.append((id_chapitre, id_chapitre_suivant))
    return data

ids_cours = []
# Générer des données pour la table cours
def generate_cours():
    data = []
    with open(os.path.join(output_dir, 'cours.txt'), 'w') as f:
        for _ in range(50):
            id_cours = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            contenu = fake.text()
            contenu = contenu.encode('UTF-8')
            id_chapitre = random.choice(ids_chapitre)
            f.write(f"INSERT INTO cours (id_cours, label, contenu, id_chapitre) VALUES ({id_cours}, '{label}', '{contenu}', {id_chapitre});\n")
            data.append((id_cours, label, contenu, id_chapitre))
            ids_cours.append(id_cours)
    return data

ids_quizz = []
# Générer des données pour la table quizz
def generate_quizz():
    data = []
    with open(os.path.join(output_dir, 'quizz.txt'), 'w') as f:
        for _ in range(50):
            id_quizz = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            type = fake.random_element(elements=('normal','negatif'))
            id_utilisateur = random.choice(ids_utilisateur)
            id_chapitre = random.choice(ids_chapitre)
            f.write(f"INSERT INTO quizz (id_quizz, label,type, id_utilisateur, id_chapitre) VALUES ({id_quizz}, '{label}' , '{type}', {id_utilisateur}, {id_chapitre});\n")
            data.append((id_quizz, label, id_utilisateur, id_chapitre))
            ids_quizz.append(id_quizz)
    return data

ids_note_quizz = []
# Générer des données pour la table note_quizz
def generate_note_quizz():
    data = []
    with open(os.path.join(output_dir, 'note_quizz.txt'), 'w') as f:
        for _ in range(50):
            id_note_quizz = fake.unique.random_int(min=1, max=10000)
            date = fake.date()
            note = fake.random_int(min=0, max=20)
            id_quizz =random.choice( ids_quizz)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO note_quizz (id_note_quizz, date, note, id_quizz, id_utilisateur) VALUES({id_note_quizz}, '{date}', {note}, {id_quizz}, {id_utilisateur});\n")
            data.append((id_note_quizz, date, note, id_quizz, id_utilisateur))
            ids_note_quizz.append(id_note_quizz)
    return data


ids_question = []
ids_nbre_bonne_reponse = []
# Générer des données pour la table question
def generate_question():
    data = []
    with open(os.path.join(output_dir, 'question.txt'), 'w') as f:
        f.write("\n")
        for _ in range(50):
            id_question = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            type = fake.random_element(elements=('multiple', 'vrais', 'faux','seul'))
            nombre_bonne_reponse = fake.random_int(min=1, max=4)
            id_quizz = random.choice(ids_quizz)
            f.write(f"INSERT INTO question (id_question, label,type, nombre_bonne_reponse, id_quizz) VALUES({id_question}, '{label}', '{type}', {nombre_bonne_reponse}, {id_quizz});\n")
            data.append((id_question, label, nombre_bonne_reponse, id_quizz))
            ids_question.append(id_question)
            ids_nbre_bonne_reponse.append(nombre_bonne_reponse)
    return data

ids_reponse = []
ids_est_bonne_reponse = []
def generate_reponse():
    data = []
    with open(os.path.join(output_dir, 'reponse.txt'), 'w') as f:
        for _ in range(50):
            id_reponse = fake.unique.random_int(min=1, max=10000)
            contenu = fake.text()
            contenu = contenu.encode('UTF-8')
            est_bonne_reponse = fake.boolean(chance_of_getting_true=50)
            id_question = random.choice(ids_question)
            f.write(f"INSERT INTO reponse (id_reponse, contenu, est_bonne_reponse, id_question) VALUES({id_reponse}, '{contenu}', {est_bonne_reponse}, {id_question});\n")
            data.append((id_reponse, contenu, est_bonne_reponse, id_question))
            ids_reponse.append(id_reponse)
            ids_est_bonne_reponse.append(est_bonne_reponse)
    return data

ids_annotation = []
def generate_annotation():
    data = []
    with open(os.path.join(output_dir, 'annotation.txt'), 'w') as f:
        for _ in range(50):
            id_annotation = fake.unique.random_int(min=1, max=10000)
            contenu = fake.text()
            contenu = contenu.encode('UTF-8')
            date = fake.date()
            id_question = random.choice(ids_question)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO annotation (id_annotation, contenu, date, id_question, id_utilisateur) VALUES({id_annotation}, '{contenu}', '{date}', {id_question}, {id_utilisateur});\n")
            data.append((id_annotation, contenu, date, id_question, id_utilisateur))
            ids_annotation.append(id_annotation)
    return data

def generate_reponse_utilisateur():
    data = []
    with open(os.path.join(output_dir, 'reponse_utilisateur.txt'), 'w') as f:
        for _ in range(50):
            id_reponse = random.choice(ids_reponse)
            id_utilisateur = random.choice(ids_utilisateur)
            id_note_quizz = random.choice(ids_note_quizz)
            f.write(f"INSERT INTO reponse_utilisateur (id_reponse, id_utilisateur, id_note_quizz) VALUES({id_reponse}, {id_utilisateur}, {id_note_quizz});\n")
            data.append((id_reponse, id_utilisateur, id_note_quizz))
    return data


ids_note_du_quizz = []
def generate_note_du_quizz():
    data = []
    with open(os.path.join(output_dir, 'note_du_quizz.txt'), 'w') as f:
        for _ in range(50):
            id_note_du_quizz = fake.unique.random_int(min=1, max=10000)
            note = fake.random_int(min=0, max=20)
            id_quizz = random.choice(ids_quizz)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO note_du_quizz (id_note_du_quizz, note, id_utilisateur, id_quizz) VALUES({id_note_du_quizz}, {note}, {id_utilisateur}, {id_quizz});\n")
            data.append((id_note_du_quizz, note, id_utilisateur, id_quizz))
            ids_note_du_quizz.append(id_note_du_quizz)
    return data

ids_carte_mentale = []
def generate_carte_mentale():
    data = []
    with open(os.path.join(output_dir, 'carte_mentale.txt'), 'w') as f:
        for _ in range(50):
            id_carte_mentale = fake.unique.random_int(min=1, max=10000)
            date = fake.date()
            titre = fake.word()
            titre = titre.encode('UTF-8')
            visibilite = fake.boolean(chance_of_getting_true=50)
            id_chapitre = random.choice(ids_chapitre)
            f.write(f"INSERT INTO carte_mentale (id_carte_mentale, date, titre, visibilite, id_chapitre) VALUES({id_carte_mentale}, '{date}', '{titre}', {visibilite}, {id_chapitre});\n")
            data.append((id_carte_mentale, date, titre, visibilite, id_chapitre))
            ids_carte_mentale.append(id_carte_mentale)
    return data

def generate_utilisateur_carte_mentale():
    data = []
    with open(os.path.join(output_dir, 'utilisateur_carte_mentale.txt'), 'w') as f:
        for _ in range(50):
            id_utilisateur = random.choice(ids_utilisateur)
            id_carte_mentale = random.choice(ids_carte_mentale)
            privilege = fake.random_element(elements=('editeur', 'consultant'))
            f.write(f"INSERT INTO utilisateur_carte_mentale (id_utilisateur, id_carte_mentale, privilege) VALUES({id_utilisateur}, {id_carte_mentale}, '{privilege}');\n")
            data.append((id_utilisateur, id_carte_mentale, privilege))
    return data


# les deux champs sont clé primaire du coup impossibilire de dupliquer les données
ids_element = []
def generate_element():
    data = []
    with open(os.path.join(output_dir, 'element.txt'), 'w') as f:
        for _ in range(50):
            id_element = fake.unique.random_int(min=1, max=10000)
            longueur = fake.random_int(min=0, max=20)
            largeur = fake.random_int(min=0, max=20)
            position_x = fake.random_int(min=0, max=20)
            position_y = fake.random_int(min=0, max=20)
            type = fake.random_element(elements=('image', 'texte'))
            id_carte_mentale = random.choice(ids_carte_mentale)
            f.write(f"INSERT INTO element (id_element, longueur, largeur, position_x, position_y, type, id_carte_mentale) VALUES({id_element}, {longueur}, {largeur}, {position_x}, {position_y}, '{type}', {id_carte_mentale});")
            data.append((id_element, longueur, largeur, position_x, position_y, type, id_carte_mentale))
            ids_element.append(id_element)
    return data

def generate_element_element():
    data = []
    with open(os.path.join(output_dir, 'element_element.txt'), 'w') as f:
        for _ in range(50):
            element_id_element = random.choice(ids_element)
            element_id_element1 = random.choice(ids_element)
            f.write(f"INSERT INTO element_element (element_id_element, element_id_element1) VALUES({element_id_element}, {element_id_element1});")
            data.append((element_id_element, element_id_element1))
    return data

ids_forum = []
def generate_forum():
    data = []
    with open(os.path.join(output_dir, 'forum.txt'), 'w') as f:
        for _ in range(50):
            id_forum = fake.unique.random_int(min=1, max=10000)
            label = fake.word()
            label = label.encode('UTF-8')
            date = fake.date()
            etat = fake.boolean(chance_of_getting_true=50)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO forum (id_forum, label, date, etat, id_utilisateur) VALUES({id_forum}, '{label}', '{date}', {etat}, {id_utilisateur});")
            data.append((id_forum, label, date, etat, id_utilisateur))
            ids_forum.append(id_forum)
    return data

ids_forum_cours = []
def generate_forum_cours():
    data = []
    with open(os.path.join(output_dir, 'forum_cours.txt'), 'w') as f:
        for _ in range(50):
            id_forum_cours = fake.unique.random_int(min=1, max=10000)
            id_forum =random.choice( ids_forum)
            id_cours = random.choice(ids_cours)
            f.write(f"INSERT INTO forum_cours (id_forum_cours, id_forum, id_cours) VALUES({id_forum_cours}, {id_forum}, {id_cours});")
            data.append((id_forum_cours, id_forum, id_cours))
            ids_forum_cours.append(id_forum_cours)
    return data

ids_forum_quizz = []
def generate_forum_quizz():
    data = []
    with open(os.path.join(output_dir, 'forum_quizz.txt'), 'w') as f:
        for _ in range(50):
            id_forum_cours = fake.unique.random_int(min=1, max=10000)
            id_forum = random.choice(ids_forum)
            id_quizz = random.choice(ids_quizz)
            f.write(f"INSERT INTO forum_quizz (id_forum_cours, id_forum, id_quizz) VALUES({id_forum_cours}, {id_forum}, {id_quizz});")
            data.append((id_forum_cours, id_forum, id_quizz))
            ids_forum_quizz.append(id_forum_cours)
    return data

ids_message = []
def generate_message():
    
    data = []
    with open(os.path.join(output_dir, 'message.txt'), 'w') as f:
        for _ in range(50):
            id_message = fake.unique.random_int(min=1, max=10000)
            contenu = fake.text()
            contenu = contenu.encode('UTF-8')
            date = fake.date()
            id_forum = random.choice(ids_forum)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO message (id_message, contenu, date, id_forum, id_utilisateur) VALUES({id_message}, '{contenu}', '{date}', {id_forum}, {id_utilisateur});")
            data.append((id_message, contenu, date, id_forum, id_utilisateur))
            ids_message.append(id_message)
    return data

ids_methode_des_j_chapitre = []
def generate_methode_des_j_chapitre():
    data = []
    with open(os.path.join(output_dir, 'methode_des_j_chapitre.txt'), 'w') as f:
        for _ in range(50):
            id_methode_des_j_chapitre = fake.unique.random_int(min=1, max=10000)
            date = fake.date()
            id_cours = random.choice(ids_cours)
            id_utilisateur = random.choice(ids_utilisateur)
            f.write(f"INSERT INTO methode_des_j_chapitre (id_methode_des_j_chapitre, date, id_cours, id_utilisateur) VALUES({id_methode_des_j_chapitre}, '{date}', {id_cours}, {id_utilisateur});")
            data.append((id_methode_des_j_chapitre, date, id_cours, id_utilisateur))
            ids_methode_des_j_chapitre.append(id_methode_des_j_chapitre)
    return data



      
if __name__ == '__main__':
    generate_universite()
    generate_utilisateur_valide()
    generate_utilisateur()
    generate_ue()
    generate_formation()
    generate_formation_ue()
    generate_chapitre()
    generate_chapitre_chapitre()
    generate_cours()
    generate_quizz()
    generate_note_quizz()
    generate_question()
    generate_reponse()
    generate_annotation()
    generate_reponse_utilisateur()
    generate_note_du_quizz()
    generate_carte_mentale()
    generate_utilisateur_carte_mentale()
    generate_element()
    generate_element_element()
    generate_forum()
    generate_forum_cours()
    generate_forum_quizz()
    generate_message()
    generate_methode_des_j_chapitre()
    print("Données générées avec succès")

    