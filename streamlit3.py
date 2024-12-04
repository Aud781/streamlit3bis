import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


authenticator.login()


def accueil():
      st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")


if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  #authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')




with st.sidebar:
    if st.session_state["authentication_status"]:
    # Le bouton de déconnexion
        authenticator.logout("Déconnexion")

        st.write(f"Bienvenue {lesDonneesDesComptes['usernames']['root']['name']}")

    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
            )

if st.session_state["authentication_status"]:  
# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        #st.write("Bienvenue sur la page d'accueil !")
        st.markdown("<h1 style='text-align: center; color: purple;'>Bienvenue sur la page d'acceuil</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(" ")
        with col2:
            st.image("img_bienvenue.png")
        with col3:
            st.write(" ")
    elif selection == "Photos":
        #st.write("Bienvenue sur mon album photo")
        st.markdown("<h1 style='text-align: center; color: purple;'>Bienvenue sur mon album photo</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Mont Fuji")
            st.image("japon.jpg")
        with col2:
            st.write("Temple Inari")
            st.image("inari.jpg")
        with col3:
            st.write("Gyeon")
            st.image("gyon.jpg")

# ... et ainsi de suite pour les autres pages