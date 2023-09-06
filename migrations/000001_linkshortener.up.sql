create table USERS
(
    id            serial primary key,
    username      varchar not null unique,
    password      varchar not null,
    created_stamp timestamp default current_timestamp
);


create table LINKS
(
    id            serial primary key,
    code          varchar not null unique,
    url           varchar not null,
    user_id       integer not null references USERS (id),
    expires_stamp timestamp default null,
    created_stamp timestamp default current_timestamp
);

delete from USERS where username in ('root', 'Kolya_SP');

insert into USERS (username, password)
values ('root', '{bcrypt}$2a$10$Zam0u6RYgvyRfPuvm4d.HOyRSeYpvzPbBdTazI85/Ad4uVNcJV74e'), -- [root] bcrypt 10 rounds
       ('Kolya_SP', '{bcrypt}$2a$10$lGAtN/0sT6qyzvWB0xIZ1OUpO0q2V9slGy.SIDEnUn5096Y3FC57a'); -- [Kolya_SP] bcrypt 10 rounds

create table messages
(
    id                    serial primary key,
    message_text          varchar not null,
    message_date          timestamp default current_timestamp

);