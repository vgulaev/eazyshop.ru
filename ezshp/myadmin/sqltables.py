sqlqueryes = ["""
        CREATE TABLE shops (
        id CHAR(36) PRIMARY KEY,
        caption CHAR(100),
        synonyms CHAR(100)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """,
        """
        CREATE TABLE users (
        id CHAR(36) PRIMARY KEY,
        login CHAR(100),
        pass CHAR(100),
        shop CHAR(36),
        FOREIGN KEY (shop) REFERENCES shops(id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """,
        """
        CREATE TABLE goods (
        id CHAR(36) PRIMARY KEY,
        shop CHAR(36),
        caption CHAR(100),
    
        FOREIGN KEY (shop) REFERENCES shops(id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """,
        """
        CREATE TABLE pricetypes (
        id CHAR(36) PRIMARY KEY,
        shop CHAR(36),
        caption CHAR(100),
        
        FOREIGN KEY (shop) REFERENCES shops(id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """,
        """
        CREATE TABLE prices (
        pricetype CHAR(36),
        good CHAR(36),
        price DECIMAL(8,2),
        
        PRIMARY KEY(pricetype, good),
        FOREIGN KEY (good) REFERENCES goods(id),
        FOREIGN KEY (pricetype) REFERENCES pricetypes(id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """]
#for e in sqlqueryes:
#    print e