-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 16, 2019 at 03:19 PM
-- Server version: 10.3.15-MariaDB-1
-- PHP Version: 7.3.4-2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CSE`
--

-- --------------------------------------------------------

--
-- Table structure for table `R1`
--

CREATE TABLE `R1` (
  `id` int(10) NOT NULL,
  `time` varchar(20) NOT NULL,
  `mon` varchar(20) NOT NULL,
  `tue` varchar(20) NOT NULL,
  `wed` varchar(20) NOT NULL,
  `thu` varchar(20) NOT NULL,
  `fri` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R1`
--

INSERT INTO `R1` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'TOC', '---', 'DAA', '---', '---'),
(2, '09-10', '---', 'TOC', '---', 'NFT', 'NFT'),
(3, '10-11', '---', '---', '---', 'IOOM', 'IOOM'),
(4, '11-12', 'IOOM', '---', '---', 'TOC', 'OS'),
(5, '12-01', 'NFT', 'OS', 'OS', 'DAA', '---'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', 'IOOM - LAB', 'NFT - LAB', '---', '---', '---'),
(8, '04-06', 'SOFT-LAB III', 'OS - LAB', '---', '---', '---');

-- --------------------------------------------------------

--
-- Table structure for table `R2`
--

CREATE TABLE `R2` (
  `id` int(10) NOT NULL,
  `time` varchar(20) NOT NULL,
  `mon` varchar(20) NOT NULL,
  `tue` varchar(20) NOT NULL,
  `wed` varchar(20) NOT NULL,
  `thu` varchar(20) NOT NULL,
  `fri` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R2`
--

INSERT INTO `R2` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'TOC', '---', 'DAA', '---', '---'),
(2, '09-10', '---', 'TOC', '---', 'NFT', 'NFT'),
(3, '10-11', '---', '---', '---', 'IOOM', 'IOOM'),
(4, '11-12', 'IOOM', '---', '---', 'TOC', 'OS'),
(5, '12-01', 'NFT', 'OS', 'OS', 'DAA', '---'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', 'NFT - LAB', 'IOOM - LAB', '---', '---', '---'),
(8, '04-06', 'OS - LAB', 'SOFT-LAB III', '---', '---', '---');

-- --------------------------------------------------------

--
-- Table structure for table `R3`
--

CREATE TABLE `R3` (
  `id` int(10) NOT NULL,
  `time` varchar(20) NOT NULL,
  `mon` varchar(20) NOT NULL,
  `tue` varchar(20) NOT NULL,
  `wed` varchar(20) NOT NULL,
  `thu` varchar(20) NOT NULL,
  `fri` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R3`
--

INSERT INTO `R3` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'TOC', '---', 'DAA', '---', '---'),
(2, '09-10', '---', 'TOC', '---', 'NFT', 'NFT'),
(3, '10-11', '---', '---', '---', 'IOOM', 'IOOM'),
(4, '11-12', 'IOOM', '---', '---', 'TOC', 'OS'),
(5, '12-01', 'NFT', 'OS', 'OS', 'DAA', '---'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', '---', '---', 'IOOM - LAB', '---', 'NFT - LAB'),
(8, '04-06', '---', '---', 'SOFT-LAB III', '---', 'OS - LAB');

-- --------------------------------------------------------

--
-- Table structure for table `R4`
--

CREATE TABLE `R4` (
  `id` int(10) NOT NULL,
  `time` varchar(20) NOT NULL,
  `mon` varchar(20) NOT NULL,
  `tue` varchar(20) NOT NULL,
  `wed` varchar(20) NOT NULL,
  `thu` varchar(20) NOT NULL,
  `fri` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R4`
--

INSERT INTO `R4` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'TOC', '---', 'DAA', '---', '---'),
(2, '09-10', '---', 'TOC', '---', 'NFT', 'NFT'),
(3, '10-11', '---', '---', '---', 'IOOM', 'IOOM'),
(4, '11-12', 'IOOM', '---', '---', 'TOC', 'OS'),
(5, '12-01', 'NFT', 'OS', 'OS', 'DAA', '---'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', '---', '---', 'NFT - LAB', '---', 'IOOM - LAB'),
(8, '04-06', '---', '---', 'OS - LAB', '---', 'SOFT-LAB III');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `R1`
--
ALTER TABLE `R1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `R2`
--
ALTER TABLE `R2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `R3`
--
ALTER TABLE `R3`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `R4`
--
ALTER TABLE `R4`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
