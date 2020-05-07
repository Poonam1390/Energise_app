CREATE TABLE IF NOT EXISTS play
             (
                          id INTEGER NOT NULL AUTO_INCREMENT,
                          exercise VARCHAR(100) NOT NULL,
                          sing VARCHAR(100) NOT NULL,
                          dance VARCHAR(100) NOT NULL,
                          PRIMARY KEY (id)                       
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `play` WRITE;
/*!40000 ALTER TABLE `play` DISABLE KEYS */;
INSERT INTO `play` VALUES (1,'pushups','titanic song','Do the cha cha'),(2,'Burpies','Shape of you','Macarena dance'),(3,'Plank','Let it go','Belly dance');
/*!40000 ALTER TABLE `play` ENABLE KEYS */;
UNLOCK TABLES;
