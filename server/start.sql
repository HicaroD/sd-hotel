CREATE TABLE IF NOT EXISTS Rooms (
    id INT PRIMARY KEY,
    occupied BOOLEAN,
    description VARCHAR(255)
);

INSERT INTO Rooms (id, occupied, description)
SELECT 1, FALSE, 'Quarto com uma cama de casal'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 1);

INSERT INTO Rooms (id, occupied, description)
SELECT 2, FALSE, 'Quarto com uma cama de casal'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 2);

INSERT INTO Rooms (id, occupied, description)
SELECT 3, FALSE, 'Quarto com uma cama de casal'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 3);

--------------------------------------------------------------

INSERT INTO Rooms (id, occupied, description)
SELECT 4, FALSE, 'Quarto com duas camas de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 4);

INSERT INTO Rooms (id, occupied, description)
SELECT 5, FALSE, 'Quarto com duas camas de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 5);

INSERT INTO Rooms (id, occupied, description)
SELECT 6, FALSE, 'Quarto com duas camas de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 6);

--------------------------------------------------------------

INSERT INTO Rooms (id, occupied, description)
SELECT 7, FALSE, 'Suíte com uma cama de casal e uma de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 7);

INSERT INTO Rooms (id, occupied, description)
SELECT 8, FALSE, 'Suíte com uma cama de casal e uma de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 8);

--------------------------------------------------------------

INSERT INTO Rooms (id, occupied, description)
SELECT 9, FALSE, 'Quarto com uma cama de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 9);

INSERT INTO Rooms (id, occupied, description)
SELECT 10, FALSE, 'Quarto com uma cama de solteiro'
WHERE NOT EXISTS (SELECT 1 FROM Rooms WHERE id = 10);
