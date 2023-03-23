/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 5.5.8-log : Database - dbfakenewsdetection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbfakenewsdetection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbfakenewsdetection`;

/*Table structure for table `tblcategory` */

DROP TABLE IF EXISTS `tblcategory`;

CREATE TABLE `tblcategory` (
  `catId` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`catId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tblcategory` */

insert  into `tblcategory`(`catId`,`category`,`status`) values 
(1,'Top stories','1'),
(2,'Sports','1'),
(3,'Movies','1'),
(4,'International','1');

/*Table structure for table `tbllogin` */

DROP TABLE IF EXISTS `tbllogin`;

CREATE TABLE `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbllogin` */

insert  into `tbllogin`(`username`,`password`,`usertype`,`status`) values 
('admin@gmail.com','admin','admin','1'),
('megha@gmail.com','megha','localbody','1'),
('tintu@gmail.com','tintu','user','1');

/*Table structure for table `tblnews` */

DROP TABLE IF EXISTS `tblnews`;

CREATE TABLE `tblnews` (
  `nId` int(11) NOT NULL AUTO_INCREMENT,
  `uId` int(11) NOT NULL,
  `catId` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `news` varchar(1000) NOT NULL,
  `img` varchar(200) NOT NULL,
  `ndate` date NOT NULL,
  PRIMARY KEY (`nId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tblnews` */

insert  into `tblnews`(`nId`,`uId`,`catId`,`title`,`news`,`img`,`ndate`) values 
(1,1,1,'Kerry to go to Paris in gesture of sympathy','Kerry to go to Paris in gesture of sympathy','/media/d930fb0a2ac711e8901b0a9df65c8753.jpg','2022-04-22');

/*Table structure for table `tbluser` */

DROP TABLE IF EXISTS `tbluser`;

CREATE TABLE `tbluser` (
  `uId` int(11) NOT NULL AUTO_INCREMENT,
  `uName` varchar(50) NOT NULL,
  `uAddress` varchar(100) NOT NULL,
  `uEmail` varchar(50) NOT NULL,
  `uContact` varchar(50) NOT NULL,
  PRIMARY KEY (`uId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tbluser` */

insert  into `tbluser`(`uId`,`uName`,`uAddress`,`uEmail`,`uContact`) values 
(1,'Tintu','Aluva','tintu@gmail.com','7845965237');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
