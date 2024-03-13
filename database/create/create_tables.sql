CREATE TABLE Races(
    raceID INT NOT NULL AUTO_INCREMENT,
    raceName VARCHAR(30),
    raceBonus VARCHAR(30),
    PRIMARY KEY (raceID)
);

CREATE TABLE RaceSkills(
    rSkill INT NOT NULL AUTO_INCREMENT,
    skill VARCHAR(30),
    roll VARCHAR(30),
    skillType VARCHAR(30),
    magic VARCHAR(30),
    raceID INT NOT NULL,
    PRIMARY KEY (rSkill),
    FOREIGN KEY (raceID) REFERENCES Races(raceID)
);

CREATE TABLE Classes(
    classID INT NOT NULL AUTO_INCREMENT,
    className VARCHAR(30),
    classBonus VARCHAR(30),
    PRIMARY KEY (classID)
);

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

CREATE TABLE User(
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(30),
    pass VARCHAR(30),
    characterID INT NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE Characters(
    characterID INT NOT NULL AUTO_INCREMENT,
    charName VARCHAR(30),
    class VARCHAR(30),
    race  VARCHAR(30),
    skill1 VARCHAR(30),
    skill2 VARCHAR(30),
    skill3 VARCHAR(30),
    raceID INT NOT NULL,
    classID INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY  KEY (characterID), 
    FOREIGN KEY (raceID) REFERENCES Races(raceID),
    FOREIGN KEY (classID) REFERENCES Classes(classID),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);





