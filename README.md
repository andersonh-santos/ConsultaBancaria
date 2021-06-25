# Consulta Bancaria
A consulta bancária é um script que irá pegar as informações de um arquivo de planilha relacionado a contas e registros bancários e irá mostrar:

<ul>
<li>O saldo total por pessoa;</li>
  <img width="350" src="doc/total_por_pessoa.png"/>
<li>O saldo total por conta;</li>
  <img width="330" src="doc/total_por_conta.png"/>
<li>O total de todas as contas por data.</li>
  <img width="370" src="doc/total_por_data.png"/>
</ul>


# Regras

<ul>
  <li>Todas as informações serão exibidas no console;</li>
  <li>Um registro sem conta e/ou sem valor será ignorado;</li>
<li>Todas as ocorrências acima serão registradas em um txt. O txt terá o número da linha que está com problema.</li>
</ul>

# Depedências

* [python3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/installing/)

# Como rodar o projeto

Abra o terminal e rode os seguintes comandos:
```
$ git clone https://github.com/andersonh-santos/ConsultaBancaria.git
$ cd ConsultaBancaria
$ pip install -r requirements.txt
$ python3 main.py
```
