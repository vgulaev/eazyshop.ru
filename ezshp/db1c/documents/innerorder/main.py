# -*- coding: utf-8 -*-
sql_query_for_create_table = ["""CREATE TABLE IF NOT EXISTS innerorder (
        id1C CHAR(36) PRIMARY KEY,
        docnumber CHAR(12),
        docdate CHAR(36),
        organization CHAR(36),
        userowner CHAR(36),
        doer CHAR(36),
        dataversion CHAR(36)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
"""]

sql_query_for_create_table += ["""CREATE TABLE IF NOT EXISTS innerorder_goods (
        id1C CHAR(36),
        rownumber INT,
        good CHAR(36),
        quantity INT,
        unit CHAR(36),

        primary key (id1C, rownumber),
        FOREIGN KEY (id1C) REFERENCES innerorder(id1C)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
"""]