-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rutvik2samant
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accomodationbookings`
--

DROP TABLE IF EXISTS `accomodationbookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accomodationbookings` (
  `idBooking` int NOT NULL AUTO_INCREMENT,
  `checkinDate` datetime NOT NULL,
  `checkoutDate` datetime NOT NULL,
  `idAccomodation` int NOT NULL,
  `noOfGuests` int NOT NULL DEFAULT '1',
  `totFare` double NOT NULL,
  `paymentstatus` char(1) NOT NULL DEFAULT 'N',
  PRIMARY KEY (`idBooking`),
  KEY `idAccomodation` (`idAccomodation`)
) ENGINE=InnoDB AUTO_INCREMENT=194 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accomodationbookings`
--

LOCK TABLES `accomodationbookings` WRITE;
/*!40000 ALTER TABLE `accomodationbookings` DISABLE KEYS */;
INSERT INTO `accomodationbookings` VALUES (1,'2022-05-12 00:00:00','2022-05-28 00:00:00',5,5,630,'N'),(2,'2022-05-13 00:00:00','2022-05-19 00:00:00',5,5,1200,'N'),(3,'2022-04-30 00:00:00','2022-05-06 00:00:00',6,4,345,'N'),(192,'2022-05-19 00:00:00','2022-07-21 00:00:00',7,8,235,'N'),(193,'2022-05-20 00:00:00','2022-08-10 00:00:00',5,2,210,'N');
/*!40000 ALTER TABLE `accomodationbookings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 12:52:28
