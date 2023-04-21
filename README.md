# Letreiro -> super simples <- feito em python com a biblioteca tkinter

![GIF](https://github.com/Inaciocb/Letreiro/blob/main/screenshots/Letreiro.gif)



# Instalação:

Você pode baixar o executável diretamente para windows [Aqui](https://github.com/Inaciocb/Letreiro/releases/tag/LEDSign), clique em "letreiro.exe" e rodar apenas clicando nele (o Windows irá reconhecer como perigoso, para rodar o código basta clicar em "Mais informações": 
![img1](https://github.com/Inaciocb/Letreiro/blob/main/screenshots/Windows1.jpg)

e depois em "Executar assim mesmo".

![img2](https://github.com/Inaciocb/Letreiro/blob/main/screenshots/Windows2.jpg)

Se não quiser rodar um executável no seu computador, você deve interpretar código o "letreiro.py", de código aberto, na sua máquina, siga os passos abaixo:
# Windows:

## 1. Baixe e instale o Python3.
Você pode baixar a partir do [site oficial](https://www.python.org/downloads/windows/).
Após a instalação, abra o prompt de comando (cmd) e verifique se o Python foi instalado corretamente digitando:
```
python --version
```

## 2. Clone o repositório:
```bash
git clone https://github.com/Inaciocb/Letreiro.git
```
## 3. Entre no diretório:
```bash
cd Letreiro/sourcecode
```
## 3. Provavelmente a biblioteca tkinter já veio instalada com a sua instalação do python, então, basta rodar o programa com o comando:
```
python3 letreiro.py
```


## - Caso a biblioteca não tenha vindo instalada por padrão, instale o pip para acessar a biblioteca tkinter:
```
python -m ensurepip --default-pip
```
## 5. Instale a biblioteca tkinter:
```
python -m pip install tkinter
```
##6. Basta rodar o programa, você pode fazer isso com uma IDE ou executando o comando:
```bash
python3 letreiro.py
```

***

# Linux:

Abra o terminal e digite os comandos:

É preciso que o python já esteja instalado, verifique rodando o seguinte comando:
```bash
  python --version
```
Caso não esteja, é necessário instalar o Python3.
Após ter o python instalado, siga os passos abaixo.

## 1. Clone o repositório:
```bash
git clone https://github.com/Inaciocb/Letreiro.git
```
## 2. Entre no diretório:
```bash
cd Letreiro/sourcecode
```
## 3. Provavelmente a biblioteca tkinter já veio instalada com a sua instalação do python, então, basta rodar o programa com o comando:
```
python3 letreiro.py
```


## - Caso a biblioteca não tenha vindo instalada por padrão, instale o pip para acessar a biblioteca tkinter:

  -Debian/Ubuntu/PopOS/Mint:
```bash
sudo apt-get install python-pip
```
  -Fedora/Redhat/CentOS/OracleLinux/ClearOS:
```bash
sudo dnf install python3-pip
```
    
  -Arch/Manjaro:
```bash
sudo pacman -S python-pip
```
## - Instale a biblioteca tkinter:
```
pip install tkinter
```
## - Rode o programa usando o comando:
```
python3 letreiro.py
```
