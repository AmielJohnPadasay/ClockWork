-- MySQL Script generated by MySQL Workbench
-- Thu Apr  3 07:59:13 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema clockwork_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema clockwork_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clockwork_schema` DEFAULT CHARACTER SET utf8 ;
USE `clockwork_schema` ;

-- -----------------------------------------------------
-- Table `clockwork_schema`.`Task_Storage`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clockwork_schema`.`Task_Storage` (
  `task_id` INT NOT NULL AUTO_INCREMENT,
  `task_name` VARCHAR(45) NOT NULL,
  `task_description` VARCHAR(255) NOT NULL,
  `submitted_link` VARCHAR(255) NULL,
  `submitted_files` MEDIUMBLOB NULL,
  `due_date_time` DATETIME NULL,
  `priority_level` VARCHAR(30) NULL,
  `status` VARCHAR(20) NULL,
  `submitted_date` DATE NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`task_id`),
  UNIQUE INDEX `user_id` (`user_id` ASC) INVISIBLE,
  UNIQUE INDEX `task_id_UNIQUE` (`task_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `clockwork_schema`.`Users_Info` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clockwork_schema`.`Users_Info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clockwork_schema`.`Users_Info` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  `birthdate` DATE NOT NULL,
  `role` VARCHAR(12) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `middle_initial` VARCHAR(5) NULL,
  `suffix` VARCHAR(5) NULL,
  `sex` VARCHAR(10) NOT NULL,
  `fingerprint` TINYBLOB NULL,
  `task_id` INT NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `fingerprint_UNIQUE` (`fingerprint` ASC) VISIBLE,
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  INDEX `fk_Users_Info_Task_Storage1_idx` (`task_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_Info_Task_Storage1`
    FOREIGN KEY (`task_id`)
    REFERENCES `clockwork_schema`.`Task_Storage` (`task_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
