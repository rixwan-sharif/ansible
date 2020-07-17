
# Wagtail CMS with Ansible

This directory contails ansible roles for setting up Wagtail-CMS with MariaDB,Supervisor and Nginx

 -  Sample Wagtails project is stored on this git repo.
	 https://github.com/rixwan-sharif/wagtail.git 
 - maria-db ansible role
   - Install dependencies
   - Installs MariaDB from official repo
   - Sets up mysql root password and wagtaildb  

 - wagtail-cms ansible role
   - checkout code from git
   - Install dependencies
   - creates virtualenv and install dependencies in it 
   - configure MariaDB with wagtail
   - create superuser
   - setup supervisor

- nginx ansible role
   - Install Nginx
   - Configure Nginx with wagtail  
