from pip._vendor.colorama import init, Fore

password = 'password'

def display(password):
    if password == 'password':
        print(Fore.GREEN + 'you are logged in')
    else:
        print(Fore.RED + 'incorrect password')

#this is exported out to hello world
#python3 -m venv env(virtual environment, {package-manager-name})
#source {package-manager-name}/bin/activate
# pip install {package}
