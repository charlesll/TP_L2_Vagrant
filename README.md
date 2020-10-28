# TP_L2_Vagrant

Code et instructions pour utiliser Python avec Vagrant dans le cadre de l'UE Physique pour les Géosciences (2), IPGP

Charles Le Losq, lelosq@ipgp.fr

## Installation de Python en local

Pour installer Python localement sur votre machine, nous vous conseillons d'utiliser
Anaconda Python:

https://www.anaconda.com/products/individual

La distribution est gratuite et contient les librairies essentielles (numpy, matplotlib et scipy)
pour les TPs.

## Python avec Google Colaboratory

Vous pouvez, si vous avez un compte Google, utiliser le service (gratuit) Google Colab
pour programmer en Python avec des Notebooks. Voir les instructions ici :

https://colab.research.google.com/notebooks/welcome.ipynb?hl=fr_FR

## Python avec VirtualBox+Vagrant

Pour éviter tout problème d'installation sur votre machine, nous avons mis en place des machines virtuelles Vagrant.
Vagrant permet d'avoir une machine de petite taille (< 800 Mb) et un environnement préconfiguré. Les instructions sont les suivantes :

- Installer VirtualBox : https://www.virtualbox.org/
- Installer Vagrant : https://www.vagrantup.com/

- créer un dossier TP_L2, où vous mettrez les fichiers data.txt et script.py disponibles ci dessus (téléchargez les ici : https://github.com/charlesll/TP_L2_Vagrant/archive/main.zip )

- ouvrez un utilitaire de commande, aussi connu sous le nom de 'terminal', pointant dans ce dossier (voir les instructions de votre système d'exploitation sur internet), puis tapez les commandes suivantes :
```
$ vagrant init charlesll/TP_L2
$ vagrant up
$ vagrant ssh
```

- Vous devriez être maintenant dans la machine virtuelle,enfin votre terminal, rien d'autre ne va s'ouvrir, l'interface n'est pas graphique. Si cela a marché, vous devriez voir maintenant dans le terminal les lignes suivantes:
```
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-51-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Oct 28 11:10:43 UTC 2020

  System load:  0.27              Processes:               119
  Usage of /:   4.7% of 38.71GB   Users logged in:         0
  Memory usage: 17%               IPv4 address for enp0s3: 10.0.2.15
  Swap usage:   0%

  8 updates can be installed immediately.
  8 of these updates are security updates.
  To see these additional updates run: apt list --upgradable

  Last login: Wed Oct 28 10:36:09 2020 from 10.0.2.2
  vagrant@ubuntu-focal:~$
```

Il faut maintenant amener le système Vagrant dans le dossier de travail partagé entre votre machine physique et la machine virtuelle, en tapant dans le terminal:
```
vagrant@ubuntu-focal:~$ cd /vagrant
```
Vous pouvez donc faire tourner votre code Python en tapant :
```
vagrant@ubuntu-focal:~$ python3 script.py
```
Voilà, vous pouvez maintenant modifier les fichiers data.txt et script.py à votre convenance, et générer vos figures en répétant la commande ci-dessus.
