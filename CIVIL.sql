-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 21, 2019 at 09:58 PM
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
-- Database: `CIVIL`
--

-- --------------------------------------------------------

--
-- Table structure for table `R1`
--

CREATE TABLE `R1` (
  `id` int(10) NOT NULL,
  `time` varchar(40) NOT NULL,
  `mon` varchar(40) NOT NULL,
  `tue` varchar(40) NOT NULL,
  `wed` varchar(40) NOT NULL,
  `thu` varchar(40) NOT NULL,
  `fri` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R1`
--

INSERT INTO `R1` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'Struct-Analysis', '---', 'Envr-Engg II', 'Fluid Mechanics', '---'),
(2, '09-10', '---', 'Struct-Analysis', '---', 'Concrete - Engg', 'Concrete - Engg'),
(3, '10-11', 'Fluid Mechanics', 'Envr - Engg II', 'Fluid Mechanics', 'Railway Airport', 'Railway Airport'),
(4, '11-12', 'Railway Airport', 'Transport. Engg', 'Transport. Engg', 'Structural Analysis', 'Design of Masonry Structure'),
(5, '12-01', 'Concrete Engg', 'Design of Masonry Structure', 'Design of Masonry Structure', 'Envr. Engg', 'Transport Engg'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', 'Fluid Mechanics Lab', '---', 'Concrete Engg - Lab', '---', 'Envr. Engg II - Lab'),
(8, '04-06', 'Structural Analysis Lab', '---', '---', '---', 'Transportation Engg Lab');

-- --------------------------------------------------------

--
-- Table structure for table `R2`
--

CREATE TABLE `R2` (
  `id` int(10) NOT NULL,
  `time` varchar(40) NOT NULL,
  `mon` varchar(40) NOT NULL,
  `tue` varchar(40) NOT NULL,
  `wed` varchar(40) NOT NULL,
  `thu` varchar(40) NOT NULL,
  `fri` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R2`
--

INSERT INTO `R2` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'Struct-Analysis', '---', 'Envr-Engg II', 'Fluid Mechanics', '---'),
(2, '09-10', '---', 'Struct-Analysis', '---', 'Concrete - Engg', 'Concrete - Engg'),
(3, '10-11', 'Fluid Mechanics', 'Envr - Engg II', 'Fluid Mechanics', 'Railway Airport', 'Railway Airport'),
(4, '11-12', 'Railway Airport', 'Transport. Engg', 'Transport. Engg', 'Structural Analysis', 'Design of Masonry Structure'),
(5, '12-01', 'Concrete Engg', 'Design of Masonry Structure', 'Design of Masonry Structure', 'Envr. Engg', 'Transport Engg'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', 'Envr. Engg II - Lab', 'Fluid Mechanics Lab', '---', 'Concrete Engg - Lab', '---'),
(8, '04-06', 'Transportation Engg Lab', 'Structural Analysis Lab', '---', '---', '---');

-- --------------------------------------------------------

--
-- Table structure for table `R3`
--

CREATE TABLE `R3` (
  `id` int(10) NOT NULL,
  `time` varchar(40) NOT NULL,
  `mon` varchar(40) NOT NULL,
  `tue` varchar(40) NOT NULL,
  `wed` varchar(40) NOT NULL,
  `thu` varchar(40) NOT NULL,
  `fri` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R3`
--

INSERT INTO `R3` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'Struct-Analysis', '---', 'Envr-Engg II', 'Fluid Mechanics', '---'),
(2, '09-10', '---', 'Struct-Analysis', '---', 'Concrete - Engg', 'Concrete - Engg'),
(3, '10-11', 'Fluid Mechanics', 'Envr - Engg II', 'Fluid Mechanics', 'Railway Airport', 'Railway Airport'),
(4, '11-12', 'Railway Airport', 'Transport. Engg.', 'Transport. Engg.', 'Structural Analysis', 'Design of Masonry Structure'),
(5, '12-01', 'Concrete Engg.', 'Design of Masonry Structure', 'Design of Masonry Structure', 'Envr. Engg.', 'Transport Engg.'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', '---', 'Envr. Engg. II - Lab', 'Fluid Mechanics Lab', '---', 'Concrete Engg. - Lab'),
(8, '04-06', '---', 'Transportation Engg. Lab', 'Structural Analysis Lab', '---', '---');

-- --------------------------------------------------------

--
-- Table structure for table `R4`
--

CREATE TABLE `R4` (
  `id` int(10) NOT NULL,
  `time` varchar(40) NOT NULL,
  `mon` varchar(40) NOT NULL,
  `tue` varchar(40) NOT NULL,
  `wed` varchar(40) NOT NULL,
  `thu` varchar(40) NOT NULL,
  `fri` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `R4`
--

INSERT INTO `R4` (`id`, `time`, `mon`, `tue`, `wed`, `thu`, `fri`) VALUES
(1, '08-09', 'Struct-Analysis', '---', 'Envr-Engg II', 'Fluid Mechanics', '---'),
(2, '09-10', '---', 'Struct-Analysis', '---', 'Concrete - Engg', 'Concrete - Engg'),
(3, '10-11', 'Fluid Mechanics', 'Envr - Engg II', 'Fluid Mechanics', 'Railway Airport', 'Railway Airport'),
(4, '11-12', 'Railway Airport', 'Transport. Engg', 'Transport. Engg', 'Structural Analysis', 'Design of Masonry Structure'),
(5, '12-01', 'Concrete Engg', 'Design of Masonry Structure', 'Design of Masonry Structure', 'Envr. Engg', 'Transport Engg'),
(6, '01-02', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH', 'LUNCH'),
(7, '02-04', 'Concrete Engg - Lab', '---', 'Envr. Engg II - Lab', 'Fluid Mechanics Lab', '---'),
(8, '04-06', '---', '---', 'Transportation Engg. Lab', 'Structural Analysis Lab', '---');

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
