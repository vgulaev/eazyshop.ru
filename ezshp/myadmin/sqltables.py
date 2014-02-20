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
        caption CHAR(100) COLLATE utf8_general_ci,
        INDEX (caption),
    
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
        
# maintanance tables without busines logic
sqlqueryes += ["""
        CREATE TABLE sessions (
        id CHAR(36) PRIMARY KEY,
        login CHAR(36),
        time_start CHAR(100),
        FOREIGN KEY (login) REFERENCES users(id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """]

updatequeryes = []
#for 0 version to 1
updatequeryes += [["""
        CREATE TABLE sysinfo (
        key_name CHAR(36) PRIMARY KEY,
        value CHAR(100)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
        """,
        "INSERT INTO sysinfo (key_name, value) VALUES ('versiondb', '1')",
        "ALTER TABLE goods ADD COLUMN ProductNo VARCHAR(40) AFTER caption"]]

updatequeryes += [["""ALTER TABLE goods ADD COLUMN unit VARCHAR(40)""",
        """
        UPDATE sysinfo
        set value = '2' WHERE key_name = 'versiondb'
        """]]

updatequeryes += [["""ALTER TABLE users ADD COLUMN uid1c VARCHAR(40)""",
        """
        UPDATE sysinfo
        set value = '3' WHERE key_name = 'versiondb'
        """]]