PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE USERS(
            id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            contact INT NOT NULL,
            height INT NOT NULL,
            weight INT NOT NULL,
            age INT NOT NULL,
            bmi INT NOT NULL
        );
COMMIT;
