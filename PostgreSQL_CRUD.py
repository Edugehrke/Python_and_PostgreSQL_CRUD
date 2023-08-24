import os
import psycopg2
import time

# @staticmethod
# permite aceesar metodo sem criar objetos

class Strong:
    
    @staticmethod
    def criar_tabela(conn):
        cursor = conn.cursor()
        sql_string = '''
    CREATE TABLE IF NOT EXISTS Estoque(
        id_produto serial primary key,
        nome_produto text,
        valor_produto double precision,
        descricao_produto text,
        categoria_produto text
    );
    CREATE TABLE IF NOT EXISTS Vendas(
        id_cliente serial primary key,
        id_produto integer,
        horario_venda double precision,
        valor_venda double precision,
        CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES Estoque (id_produto)
    );
    CREATE TABLE IF NOT EXISTS Vendas_Fiado(
        id serial primary key,
        id_produto integer,
        id_cliente integer,
        horario_venda float,
        valor_venda float,
        CONSTRAINT fk_produto_vendas_fiado FOREIGN KEY (id_produto) REFERENCES Estoque (id_produto)
        ); 

    CREATE TABLE IF NOT EXISTS Cliente_cadastro(
        id serial primary key,
        teleone integer,
        nome text,
        email text,
        cpf text,
        cep integer,
        nmr_casa integer,
        complemento text,
        cartao integer,
        CONSTRAINT fk_id_cliente FOREIGN KEY (nmr_casa) REFERENCES Vendas (id_cliente)

    )
'''
        print('Tabelas criadas com sucesso!')
        cursor.execute(sql_string)
        conn.commit()
        cursor.close()



    @staticmethod
    def insere_dados(conn,nome_tabela, nome_produto, valor_produto, descricao_produto, categoria_produto):
        cursor = conn.cursor()
        sql_string = f"""
            insert into {nome_tabela}\
            (nome_produto,valor_produto,descricao_produto,categoria_produto)\
            values ('{nome_produto}', '{valor_produto}', '{descricao_produto}','{categoria_produto}')
        """

        cursor.execute(sql_string)
        conn.commit()
        cursor.close()
        print(f'Dados: {nome_produto} - {valor_produto} - {descricao_produto},{categoria_produto} ',end=' ')
        print(f'inseridos em {nome_tabela} com sucesso.')



        

def database_manager():
    os.system('cls')
    conn = psycopg2.connect(
        dbname="Strong_conv",
        user="postgres",
        password="Strong123@",
        host="localhost",
        port="5432"
    )
    print(conn.status)

    menu_interface = '''
1 - Criar tabela
2 - Inserir dados
3 - Deletar linha
4 - Mostrar tabela
5 - Aualizar linha
6 - Sair
Insira a operação (1 - 6): '''

    while True:
        try:
            operacao = int(
                input(menu_interface)
            )

            if operacao == 1:
                Strong.criar_tabela(conn)

            elif operacao == 2:
                nome_tabela = input('Informe o nome da tabela: ')

                if nome_tabela == 'Estoque':
                    nome_produto = input('Informe o nome do produto: ')
                    valor_produto = input('Informe o valor do produto: ')
                    descricao_produto = input('Descricao do produto: ')
                    categoria_produto = input('Informe qual a categoria do produto: ')
                    
                    lista_tabela_produtos = [conn,nome_tabela,nome_produto,valor_produto,descricao_produto,categoria_produto]

                elif nome_tabela == 'Vendas':
                    pass
                    ##Criar uma funcao verifica item na tabela Produtos retornando TRUE OR FALSE
                    ##INSERT INTO Na tabela vendas
                    ##Update na tabela Estoque

                
                elif nome_tabela == 'Vendas_fiado':
                    pass

                elif nome_tabela == 'Cliente_Cadastro':
                    pass


                #### VERFICAR DADOS COM IFS

                Strong.insere_dados( 
                    *lista_tabela_produtos      
                )

            elif operacao == 3:
                tabela_delete = input('Informe de qual tabela voce deseja deletar o ID:')
                nmr_linha = input('Informe o ID que voce deseja deletar:')


                Strong.delete_linha(nmr_linha,tabela_delete ,conn)

                pass
            elif operacao == 4:
                show_tabela = input('Qual tabela voce deseja visualizar? ')
                Strong.mostra_tabela(show_tabela,conn)     
            elif operacao == 5:
                tabelas = input('de qual tabela voce deseja atualizar os dados?')
                id_update = input('Digite a ID que voce deseja atualizar ')
                nome_novo = input('Informe o novo nome: ')
                numero_novo = input('Informe o numero novo: ')
                email_novo = input('Informe o email novo: ')
                Strong.atualiza_linha(tabelas,id_update, nome_novo, numero_novo, email_novo,conn)


                pass
            elif operacao == 6:
                print('Programa encerrado.')
                break
            else:
                print(
                    'Informe uma operação válida'
                )

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    conn.close()
    print('Conexão encerrada.')
            

if __name__ == '__main__':
    database_manager()
    