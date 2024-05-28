create database Drink_Agile;
use Drink_Agile;

CREATE TABLE Estoque (
    idEstoque INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    idProdutos INT,
    quantidade INT,
    FOREIGN KEY (idProdutos) REFERENCES Produtos(idProdutos)
);


create table funcionarios (
	idFuncionarios int not null auto_increment,
    nomeFunc varchar(100),
    cargoFunc varchar(100),
    salarioFunc decimal(10,2),
primary key (idFuncionarios));



create table historicofuncionarios (
	idHistorico INT NOT NULL AUTO_INCREMENT,
    idFuncionario int,
    nomeAntigo varchar(100),
    cargoAntigo varchar(100),
    salarioAntigo decimal(10,2),
    nomeNovo varchar(100),
    cargoNovo varchar(100),
    salarioNovo decimal(10,2),
    dataAlteracao timestamp,
primary key (idHistorico));

CREATE TABLE clientes (
    idClientes INT NOT NULL AUTO_INCREMENT,
    nomecli VARCHAR(100),
    Sociedadecli VARCHAR(100),
    telefonecli BIGINT, 
    cpfcli BIGINT,
PRIMARY KEY (idClientes));

create table produtos (
	idProdutos int not null auto_increment,
    nomeProd varchar(100),
    preçoProd float,
    descProd varchar(100),
    codProd int,
    idFornecedor int not null, 
    primary key(idProdutos));

create table fornecedor(
	idFornecedor int not null auto_increment,
    nomeForn varchar(100),
    produtoForn varchar(100),
    cidade varchar(100),
    cnpj varchar(100),
    primary key (idFornecedor));
    
create table historicoProduto (
	idHistorico INT NOT NULL AUTO_INCREMENT,
    idProdutos int,
    nomeAntigo varchar(100),
    preçoAntigo float,
    descAntigo varchar(100),
    codAntigo int,
    idFornAntigo int,
    nomeNovo varchar(100),
    preçoNovo float,
    descNovo varchar(100),
    codNovo int,
    idFornNovo int,
    dataAlteracao timestamp,
primary key (idHistorico));

create table historicoclientes (
    idHistcli INT NOT NULL AUTO_INCREMENT primary key,
    idClientes int,
    nomeAntigocli varchar(100),
    sociedadeAntigocli varchar(100),
    telefoneAntigocli bigint,
    cpfAntigocli bigint,
    nomeNovocli varchar(100),
    sociedadeNovocli varchar(100),
    telefoneNovocli bigint,
    cpfnovocli bigint,
    dataAlteracaocli timestamp);
    
    create table historicofornecedores (
    idHistforn INT NOT NULL AUTO_INCREMENT primary key,
    idFornecedor int,
    nomeantigoForn varchar(100),
    produtoantigoForn varchar(100),
    cidadeantigo varchar(100),
    cnpjantigo bigint,
    nomeNovoForn varchar(100),
    produtonovoForn varchar(100),
    cidadenovo varchar(100),
    cnpjnovo bigint,
    dataAlteracaocli timestamp
    );

create table vendas(
idvendas int not null auto_increment,
codvendas varchar (10),
idClientes int not null,
idFornecedor int not null,
valorvendas float (10,2),
descvendas float (10, 2),
totalvendas float (10,2), 
datavendas date,
primary key (idvendas));

    
alter table produtos add constraint fk_produto
foreign key (idFornecedor) references fornecedor(idFornecedor);

alter table vendas add constraint fk_fornecedores
foreign key (idFornecedor) references fornecedor(idFornecedor)
on delete no action on update no action;

alter table vendas add constraint fk_vendas_clientes
foreign key(idClientes) references clientes(idClientes)
on delete no action on update no action;

INSERT INTO Estoque (idProdutos, quantidade) VALUES
(11, 10),
(12, 10),
(13, 10),
(14, 10),
(15, 10),
(16, 10),
(17, 10),
(18, 10),
(19, 10),
(20, 10);

insert into vendas (codvendas, idClientes, idFornecedor, valorvendas, descvendas, totalvendas, datavendas) values
('V001', 1, 1,  3.50, 0, 3.50, '2024-03-01'),
('V002', 2, 2,  3.00, 0, 3.00, '2024-03-02'),
('V003', 3, 3,  2.50, 0, 2.50, '2024-03-03'),
('V004', 4, 4,  1.00, 0, 1.00, '2024-03-04'),
('V005', 5, 5, 6.00, 0, 6.00, '2024-03-05'),
('V006', 6, 6,  4.00, 0, 4.00, '2024-03-06'),
('V007', 7, 7,  3.50, 0,3.50, '2024-03-07'),
('V008', 8, 8,  3.00, 0, 3.00, '2024-03-08'),
('V009', 9, 9,  50.00, 0, 50.00, '2024-03-09'),
('V010', 10, 10, 2.00, 0, 2.00, '2024-03-10');

-- Inserts
INSERT INTO Funcionarios (nomeFunc, cargoFunc, salarioFunc) VALUES
('João', 'Vendedor', 1500.00),
('Maria', 'Vendedora', 1450.00),
('Pedro', 'Repositor', 2000.00),
('Carla', 'Empacotadora', 1450.00),
('Marcos', 'Treineiro', 1450.00),
('Luisa', 'Divulgadora', 2000.00),
('Fábio', 'Segurança', 3000.00),
('Isabela', 'Gerente', 2500.00),
('Rodrigo', 'Repositor', 2000.00),
('Renata', 'Limpeza', 3000.00);

INSERT INTO clientes (nomecli, Sociedadecli, telefonecli, cpfcli) VALUES
('Jurandir', 'Alfa', 17992467432, 46670255810),
('Marina', 'Beta', 11987654321, 12345678901),
('Ricardo', 'Médio', 21976543210, 98765432109),
('Camila', 'Beta', 31965482371, 65482371956),
('Lucas', 'Alfa', 41978965432, 78965432107),
('Amanda', 'Médio', 51985214763, 85214763958),
('Fernando', 'Alfa', 61974185236, 74185236905),
('Isabela', 'Beta', 71963258741, 63258741901),
('Gabriel', 'Médio', 81974185263, 74185263902),
('Mariana', 'Beta', 91985236974, 85236974103);


INSERT INTO produtos (nomeProd, preçoProd, descProd, codProd, idFornecedor) VALUES
('Coca-Cola', 3.50, 'Refrigerante de cola', 23001, 10),
('Fanta', 3.00, 'Refrigerante de laranja', 34002, 9),
('Cotuba', 2.50, 'Cerveja Pilsen', 542003, 8),
('Gelo', 1.00, 'Pacote de gelo', 3456004, 7),
('Torresmo', 6.00, 'Porção de torresmo', 534005, 6),
('Amenduim', 4.00, 'Amendoim torrado e salgado', 6456006, 5),
('Skol', 3.50, 'Cerveja Pilsen', 674007, 4),
('Antarctica', 3.00, 'Refrigerante de guaraná', 743008, 3),
('Red Label', 50.00, 'Whisky escocês', 765009, 2),
('Corote', 2.00, 'Bebida alcoólica saborizada', 3456010, 1);

INSERT INTO fornecedor (nomeForn, produtoForn, cidade, cnpj) VALUES
('PingaZe', 'Corote', 'Belo Horizonte', '12345678901234'),
('Johnnie Walker', 'Red Label', 'São Paulo', '23456789012345'),
('AmBev', 'Antarctica', 'Rio de Janeiro', '34567890123456'),
('AmBev', 'Skol', 'São Paulo', '45678901234567'),
('Dori', 'Amendoim', 'Cedral', '56789012345678'),
('Peg-Pig', 'Torresmo', 'Mirassol', '67890123456789'),
('K-Gelo', 'Gelo', 'Fernandopolis', '78901234567890'),
('Arco Iris', 'Cotuba', 'São Jose do Rio Preto', '89012345678901'),
('Coca', 'Fanta', 'São Paulo', '90123456789012'),
('Coca', 'Coca-Cola', 'Franca', '01234567890123');

/*FUNCIONARIOS - FUNCIONARIOS - FUNCIONARIOS*/

delimiter //
	create procedure proccadastrarFuncionarios (
		in p_nome_func varchar(100), -- Parâmetro de entrada: nome do funcionário
        in p_cargo_func varchar(100), -- Parâmetro de entrada: cargo do funcionário
        in p_salario_func float -- Parâmetro de entrada: salário do funcionário
)
begin
		-- Insere o funcionario na tabela funcionario
        insert into funcionarios (nomeFunc, cargoFunc, salarioFunc) values (p_nome_func, p_cargo_func, p_salario_func); -- Insere os dados na tabela funcionários
        select "Funcionario cadastrado com sucesso!" as mensagem; -- Retorna mensagem de sucesso
end //
delimiter ;

DROP TRIGGER IF EXISTS trig_historico_funcionario; -- Remove o trigger se existir
DELIMITER //
CREATE TRIGGER trig_historico_funcionario 
AFTER UPDATE ON Funcionarios -- Aciona o trigger após uma atualização na tabela Funcionarios
FOR EACH ROW -- Para cada linha afetada pela atualização
BEGIN
    INSERT INTO historicofuncionarios (idFuncionario, nomeAntigo, cargoAntigo, salarioAntigo, nomeNovo, cargoNovo, salarioNovo, dataAlteracao)
    VALUES (OLD.idFuncionarios, OLD.nomefunc, OLD.cargofunc, OLD.salariofunc, NEW.nomefunc, NEW.cargofunc, NEW.salariofunc, NOW()); -- Insere um registro na tabela de histórico com os dados antigos e novos do funcionário
END //
DELIMITER ;

delimiter //
create procedure procalterarfunc (
	in novo_id_func int, -- Parâmetro de entrada: novo ID do funcionário
    in novo_nome_func varchar(100), -- Parâmetro de entrada: novo nome do funcionário
    in novo_cargo_func varchar(100), -- Parâmetro de entrada: novo cargo do funcionário
    in novo_salario_func float -- Parâmetro de entrada: novo salário do funcionário
)
begin
    -- Atualiza o funcionario
    if exists (select 1 from funcionarios where idFuncionarios = novo_id_func) then -- Verifica se o funcionário com o ID especificado existe
        update funcionarios set nomefunc = novo_nome_func, cargofunc = novo_cargo_func, salariofunc = novo_salario_func -- Atualiza os dados do funcionário
        where idFuncionarios = novo_id_func; -- Condição para atualizar o funcionário com o ID especificado
        select 'Funcionário alterado' as mensagem; -- Retorna mensagem de sucesso
    else
        select 'Funcionário não encontrado.' as mensagem; -- Retorna mensagem de erro se o funcionário não for encontrado
    end if;
end //
delimiter ;


/*PRODUTOS - PRODUTOS - PRODUTOS*/

delimiter //
	create procedure proccadastrarProduto (
		in p_nome_prod varchar(100),
        in p_preco_prod varchar(100),
        in p_desc_prod varchar(100),
        in p_cod_prod float,
        in p_codForn_prod int
)
begin
		-- Insere o funcionario na tabela funcionario
        insert into produtos(nomeProd, preçoProd, descProd, codProd, idFornecedor) values (p_nome_prod, p_preco_prod, p_desc_prod, p_cod_prod, p_codForn_prod);
        select "Produto cadastrado com sucesso!" as mensagem;
end //
delimiter ;

delimiter //
create procedure procalterarProd (
	in novo_id_Prod int,
    in novo_nome_Prod varchar(100),
    in novo_preco_Prod float,
    in novo_desc_Prod varchar(100),
    in novo_cod_Pord int,
    in novo_idForn_Prod int
)
begin
    -- Atualiza o Produto
    if exists (select 1 from produtos where idProdutos = novo_id_Prod) then
        update produtos set nomeProd = novo_nome_Prod, preçoProd = novo_preco_Prod, descProd = novo_desc_Prod, codProd = novo_cod_Pord, idFornecedor =  novo_idForn_Prod
        where idProdutos = novo_id_Prod;
        select 'Produto alterado' as mensagem;
    else
        select 'Produto não encontrado.' as mensagem;
    end if;
end //
delimiter ;

DROP TRIGGER IF EXISTS trig_historico_Produtos;
DELIMITER //
CREATE TRIGGER trig_historico_Produtos 
AFTER UPDATE ON Produtos
FOR EACH ROW 
BEGIN
    INSERT INTO historicoproduto (idProdutos, nomeAntigo, preçoAntigo, descAntigo, codAntigo,idFornAntigo,nomeNovo, preçoNovo, descNovo, codNovo, idFornNovo,dataAlteracao)
    VALUES (OLD.idProdutos, OLD.nomeProd, OLD.preçoProd, OLD.descProd, OLD.codProd, OLD.idFornecedor, NEW.nomeProd, NEW.preçoProd, NEW.descProd, NEW.codProd, NEW.idFornecedor, NOW());
END //
DELIMITER ;

/*CLIENTES - CLIENTES - CLIENTES*/

delimiter //
    create procedure proccadastrarClientes (
        in p_nome_cli varchar(100),
        in p_sociedade_cli varchar(100),
        in p_telefone_cli BIGINT,
        in p_cpf_cli BIGINT
)
begin
        -- Insere o funcionario na tabela funcionario
        insert into clientes (nomecli, Sociedadecli, telefonecli, cpfcli) values (p_nome_cli, p_sociedade_cli, p_telefone_cli, p_cpf_cli);
        select "Cliente cadastrado com sucesso!" as mensagem;
end //
delimiter ;

drop procedure if exists procalterarclientes
delimiter //
create procedure procalterarclientes (
    in novo_id_cli int,
    in novo_nome_cli varchar(100),
    in novo_sociedade_cli varchar(100),
    in novo_telefone_cli bigint,
    in novo_cpf_cli bigint

)
begin
    -- Atualiza o funcionario
    if exists (select 1 from clientes where idclientes = novo_id_cli) then
        update clientes set nomecli = novo_nome_cli, Sociedadecli = novo_sociedade_cli, telefonecli = novo_telefone_cli, cpfcli = novo_cpf_cli
        where idClientes = novo_id_cli;
        select 'Cliente alterado' as mensagem;
    else
        select 'Cliente não encontrado.' as mensagem;
    end if;
end //
delimiter ;

DROP TRIGGER IF EXISTS trig_historico_clientes;
DELIMITER //
CREATE TRIGGER trig_historico_clientes
AFTER UPDATE ON clientes
FOR EACH ROW 
BEGIN
    INSERT INTO historicoclientes (idClientes, nomeAntigocli, sociedadeAntigocli, telefoneAntigocli, cpfAntigocli, nomeNovocli, sociedadeNovocli, telefoneNovocli, cpfnovocli, dataAlteracaocli)
    VALUES (OLD.idClientes, OLD.nomecli, OLD.Sociedadecli, OLD.telefonecli, OLD.cpfcli, NEW.nomecli, NEW.Sociedadecli, NEW.telefonecli, NEW.cpfcli, NOW());
END //
DELIMITER ;

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

drop procedure proccadastrarFornecedor
delimiter //
    create procedure proccadastrarFornecedor (
        in p_nome_forn varchar(100),
        in p_produto_forn varchar(100),
        in p_cidade_forn varchar(100),
        in p_cnpj_forn bigint
)
begin
        -- Insere o funcionario na tabela funcionario
        insert into fornecedor (nomeForn, produtoforn, cidade, cnpj) values (p_nome_forn,  p_produto_forn, p_cidade_forn, p_cnpj_forn);
        select "Fornecedor cadastrado com sucesso!" as mensagem;
end //
delimiter ;


drop procedure if exists procalterarfornecedor
delimiter //
create procedure procalterarfornecedor (
		in pn_id_forn int,
		in pn_nome_forn varchar(100),
        in pn_produto_forn varchar(100),
        in pn_cidade_forn varchar(100),
        in pn_cnpj_forn bigint
)

begin
    -- Atualiza o funcionario
    if exists (select 1 from fornecedor where idFornecedor = pn_id_forn) then
        update fornecedor set nomeForn = pn_nome_forn, produtoForn = pn_produto_forn, cidade = pn_cidade_forn, cnpj = pn_cnpj_forn
        where idFornecedor = pn_id_forn;
        select 'Fornecedor alterado' as mensagem;
    else
        select 'Fornecedor não encontrado.' as mensagem;
    end if;
end //
delimiter ;

DROP TRIGGER IF EXISTS trig_historico_fornecedores;
DELIMITER //
CREATE TRIGGER trig_historico_fornecedores
AFTER UPDATE ON fornecedor
FOR EACH ROW 
BEGIN
    INSERT INTO historicofornecedores (idFornecedor, nomeantigoForn, produtoantigoForn, cidadeantigo, cnpjantigo, nomeNovoForn, produtonovoForn, cidadenovo, cnpjnovo, dataAlteracaocli)
    VALUES (OLD.idFornecedor, OLD.nomeForn, OLD.produtoForn, OLD.cidade,OLD.cnpj, NEW.nomeForn, NEW.produtoForn, NEW.cidade, NEW.cnpj, NOW());
END //
DELIMITER ;

create view historico_forn as 
select * from historicofornecedores;

/*LOGIN - LOGIN - LOGIN*/

CREATE TABLE login (
    idLogin INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO login (username, password) VALUES
('RenanMattos', '123'),
('MiguelIgnani', '123'),
('Kaue', '123');

select * from login;
select * from clientes;
select * from fornecedor;
select * from funcionarios;
select * from produtos;
select * from vendas;
select * from estoque;