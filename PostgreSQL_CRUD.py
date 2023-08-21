import os
import psycopg2

# @staticmethod
# permite aceesar metodo sem criar objetos

class BancoDeDados:
    # Atributo PUBLICO da classe
    def criar_tabela(nome_tabela_nova, conn):
        cursor = conn.cursor()
        if nome_tabela_nova == 'Produtos':
            sql_string = f''' 
                create table if not exists {nome_tabela_nova} (\
                    id serial primary key,\
                    nome text,\
                    valor text,\
                    descricao text, \
                    categoria text 
                )
        '''
        elif nome_tabela_nova == 'Vendas':
            pass
        
        elif nome_tabela_nova == 'Cliente_Cadastro':
            pass

        elif nome_tabela_nova == 'Vendas_fiado':
            pass


        cursor.execute(sql_string)
        conn.commit()
        cursor.close()
        print(f'Tabela {nome_tabela_nova} criada com sucesso.')

    @staticmethod
    def insere_dados(conn,nome_tabela, nome_produto, valor_produto, descricao_produto, categoria_produto):
        cursor = conn.cursor()

        sql_string = f"""
            insert into {nome_tabela}\
            (nome,valor,descricao,categoria)\
            values ('{nome_produto}', '{valor_produto}', '{descricao_produto}','{categoria_produto}')
        """

        cursor.execute(sql_string)
        conn.commit()
        cursor.close()
        print(f'Dados: {nome_produto} - {valor_produto} - {descricao_produto},{categoria_produto} ',end=' ')
        print(f'inseridos em {nome_tabela} com sucesso.')

    @staticmethod
    def delete_linha(id_linha,nome_tabela,conn):
        cursor = conn.cursor()

        sql_string=(f"""
        DELETE FROM  {nome_tabela}
        WHERE id = {id_linha}
        """)

        cursor.execute(sql_string)
        conn.commit()
        cursor.close()

        print(f'linha da ID: {id_linha} e da tabela:{nome_tabela} deletada com sucesso!')

        # DELETAR LINHA VIA ID

    @staticmethod
    def mostra_tabela(nome_tabela, conn):
        cursor = conn.cursor()
        sql_string = f"""
            select * from {nome_tabela} 
            WHERE id = 2
        """
        cursor.execute(sql_string)  # Execute a consulta usando o cursor
        resultados = cursor.fetchall()  # Recupere os resultados da consulta
        for item in resultados:
            print(item)
        conn.commit()
        cursor.close()


    @staticmethod
    def atualiza_linha(nome_tabela,id_linha, nome_novo, numero_novo, email_novo,conn):
        cursor = conn.cursor()
        sql_string = (f"""
UPDATE {nome_tabela}
SET nome = '{nome_novo}', numero = '{numero_novo}', email = '{email_novo}'
WHERE id = {id_linha}
        """
        )
        cursor.execute(sql_string)
        conn.commit()
        cursor.close()


        

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
                nome_tabela = input('Informe o nome da tabela nova: ')
                BancoDeDados.criar_tabela(nome_tabela,conn)
            elif operacao == 2:
                tabela = input('Informe o nome da tabela: ')
                nome = input('Informe o nome do produto: ')
                valor = input('Informe o valor do produto: ')
                descricao = input('Descricao do produto: ')
                categoria = input('Informe qual a categoria do produto: ')

                #### VERFICAR DADOS COM IFS

                BancoDeDados.insere_dados(conn, 
                    nome_tabela=tabela,
                    nome_produto=nome,
                    valor_produto=valor,
                    descricao_produto=descricao,
                    categoria_produto=categoria              
                )
            elif operacao == 3:
                tabela_delete = input('Informe de qual tabela voce deseja deletar o ID:')
                nmr_linha = input('Informe o ID que voce deseja deletar:')


                BancoDeDados.delete_linha(nmr_linha,tabela_delete ,conn)

                pass
            elif operacao == 4:
                show_tabela = input('Qual tabela voce deseja visualizar? ')
                BancoDeDados.mostra_tabela(show_tabela,conn)     
            elif operacao == 5:
                tabelas = input('de qual tabela voce deseja atualizar os dados?')
                id_update = input('Digite a ID que voce deseja atualizar ')
                nome_novo = input('Informe o novo nome: ')
                numero_novo = input('Informe o numero novo: ')
                email_novo = input('Informe o email novo: ')
                BancoDeDados.atualiza_linha(tabelas,id_update, nome_novo, numero_novo, email_novo,conn)


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
    