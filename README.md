# Back-end Challenge 🏅 2021 - Space Flight News :brazil:


Uma API Rest criada usando dados da API [Space Flight News](https://api.spaceflightnewsapi.net/v3/documentation).
******
### Linguagem e banco
*   Python [3.8.8]
*   MongoDB - Atlas

### Principais frameworks
*   FastAPI [0.73.0]
*   Pymongo [4.0.1]
*****
### Instruções para instalação
1.   Certifique-se que possui instalado o Python e o Pip em seu dispositivo.
2.   Faça o fork/clone ou apenas o clone do repositório git.
3.   Instale as dependências do projeto
     ```
        pip install -r requirements.txt
     ```
4.   Configure o banco MongoDB Atlas e a(s) collection(s) a serem utilizadas
     ```
        backend-challenge/
        ├─ settings/
           ├─ db.py  <-

     ```
5.   Inicie o servidor.
     *   Em desenvolvimento
         ```
            uvicorn app:APP --reload
         ```

     *   Em produção
         ```
            uvicorn app:APP
         ```

6 . Acesse a documentação na rota /docs (ex: http://127.0.0.1:8000/docs)



> This is a challenge by Coodesh








