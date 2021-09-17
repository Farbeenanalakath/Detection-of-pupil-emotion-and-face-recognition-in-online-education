/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - pupil_emotion
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pupil_emotion` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `pupil_emotion`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `course` */

insert  into `course`(`id`,`course`) values 
(1,'BSC.COMPUTER SCIENCE'),
(2,'BBA'),
(3,'BCOM'),
(4,'BCA'),
(5,'MCA');

/*Table structure for table `emotion` */

DROP TABLE IF EXISTS `emotion`;

CREATE TABLE `emotion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class_id` int DEFAULT NULL,
  `userid` int DEFAULT NULL,
  `emotion` varchar(500) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `attendance` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emotion` */

insert  into `emotion`(`id`,`class_id`,`userid`,`emotion`,`rating`,`attendance`) values 
(1,1,4,'happy',4.5,'1'),
(2,1,5,'happy',3.56,'1');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(90) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'danya','123','staff'),
(4,'riya','riya','student'),
(5,'drishya','aaa','student');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lid` int DEFAULT NULL,
  `fname` varchar(90) DEFAULT NULL,
  `lname` varchar(90) DEFAULT NULL,
  `gender` varchar(90) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `pin` bigint DEFAULT NULL,
  `qualification` varchar(90) DEFAULT NULL,
  `experience` varchar(90) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `staff` */

insert  into `staff`(`id`,`lid`,`fname`,`lname`,`gender`,`photo`,`place`,`post`,`pin`,`qualification`,`experience`,`email`,`phone`) values 
(1,2,'Dhanya','das','FEMALE','c.jpg','calicut','calicut',909090,'PHD','4yrs','danyadas@gmail.com',9090909090);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lid` int DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `age` bigint DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` bigint DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `sem` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `student` */

insert  into `student`(`id`,`lid`,`fname`,`lname`,`age`,`gender`,`photo`,`place`,`post`,`pin`,`course_id`,`sem`,`email`,`phone`) values 
(2,4,'Riya','s',22,'FEMALE','riya.jpeg','calicut','calicut',989876,1,1,'riyas@gmail.com',9887678989),
(3,5,'drishya','mk',23,'FEMALE','en.jpg','calicut','calicut',909090,1,1,'drishyamk@gmail.com',9876567867);

/*Table structure for table `video` */

DROP TABLE IF EXISTS `video`;

CREATE TABLE `video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int DEFAULT NULL,
  `video` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `video` */

insert  into `video`(`id`,`staff_id`,`video`,`date`) values 
(1,2,'7.mp4','2021-05-24');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
