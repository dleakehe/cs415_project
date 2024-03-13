CREATE TABLE ClassSkills(
    cSkills INT NOT NULL AUTO_INCREMENT,
    skill VARCHAR(30),
    roll VARCHAR(30),
    skillType VARCHAR(30),
    magic VARCHAR(30),
    classID INT NOT NULL,
    PRIMARY KEY (cskills),
    FOREIGN KEY (classID) REFERENCES Classes(classID)
);

INSERT INTO ClassSkills(skill, roll, skillType, magic, classID)
VALUES (
    'Poison',
    '1d4',
    'Enhance',
    'Poison',
    1
);

INSERT INTO ClassSkills(skill, roll, skillType, magic, classID)
VALUES (
    'Pommel Strike',
    '1d8',
    'Bludgeon',
    NULL,
    2
);