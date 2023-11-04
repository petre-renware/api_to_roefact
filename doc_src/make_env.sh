
#
# --- find all python (*.py) files from curent directory
# find "./" -type f -name "*.py*"
# --- and full commande to make them executables
chmod +x `find "./" -type f -name "*.py*"`
chmod +x `find "./" -type f -name "*.sh*"`




# create CGI running environmet

python3 -m venv pyenv
source pyenv/bin/activate
pip install -r requirements.txt





