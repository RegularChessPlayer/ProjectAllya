# ProjectAllya
  Prova prática resolvida em Django2.2 e Python 3 e integração com o meio de pagamento MundiPagg.
  
## Requirementos 
* Virtual Environment
* Python3

## Instalação
No diretório ProjectAllya
* Criação virtual enviroment
  * python3 -m venv env (Criação virtual enviroment)

* Ativar virtual environment em: ProjectAllya/tickets
  * source bin/activate
  
* Instalar as depedências do projeto
    * pip install -r requirements.txt
    
No diretório tickets    
  
  * Criar supperuser
    * python manage.py createsupperuser 
  
  * Iniciar a aplicação:
    * python manage.py runserver
  
  * Acessar http://127.0.0.1:8000/admin/ 
    * Popular Tabelas
  
    
## Utilização

Listar Teatros com shows ativos e com ingressos disponíveis:
   
   * Acessar via browser http://127.0.0.1:8000/ticket/list/theater
   
Listar Shows ativos e com ingressos disponíveis de um Teatro e quantidade de
ingressos disponível por show:

   * Acessar o endpoint passando o último paramentro o id do teatro ex: http://127.0.0.1:8000/ticket/list/theater/2
   
Compra de Ingresso
   * Para comprar o igresso se faz necessário criar uma requisição do tipo POST para o seguinte endpoint: http://127.0.0.1:8000/ticket/buy
   
   * Corpo da requisição deve possuir um JSON com os seguintes campos:
        
        * id_show: tipo inteiro, id do show cadastrado.
        * qtd_ticket: tipo inteiro, quantidade de ingressos que deseja comprar.
        * id_perfil: tipo inteiro, id do perfil cadastrado.
        * card_number: tipo string, número do cartão para exemplos de teste utilizaremos o valor "4000000000000010" p/ operações com sucesso
        e "4000000000000028" p/ operações com falha.
        * card_name: tipo string, nome do usuário do cartão. 
        * card_exp_month: tipo inteiro, mês que expira o cartão.
        * card_exp_year: tipo inteiro, ano que expira o cartão.
        * card_cvv: tipo string, três digítos verificadores do cartão.
        
       # Ex.: 
	     {
	        "id_show": 3,
	        "qtd_ticket": 1,
            "id_perfil": 1,
            "card_number": "4000000000000010",
            "card_name": "Tony Stark",
            "card_exp_month": 1,
            "card_exp_year": 2025,
            "card_cvv":  "123"
         }
   * A requisição irá retornar status e um objeto json com chave 'message'
   
        # Ex.:
            status: 200
            {
                "message": "Operação concluída com sucesso"
            }
            
            status: 422
            {
                "message": "Operacão invalidada"
            }
