CREATE DATABASE IF NOT EXISTS comercio_eletrônico DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;

use comercio_eletrônico;

create table clientes(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    saldo decimal(10,2) not null,
);

create table produtos(
    id_produto int auto_increment primary key,
    nome varchar(100) not null,
    preco decimal(10,2) not null,
    estoque int not null
);

