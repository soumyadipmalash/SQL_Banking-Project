                                 -- Banking Project SQL                      @Soumyadip Malash
/*

-- Drop Customer Table if exists
IF OBJECT_ID('Customer', 'U') IS NOT NULL
    DROP TABLE Customer;
GO

-- Create Customer Table
CREATE TABLE Customer (
    Acno INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(30) NULL,
    Address NVARCHAR(100) NULL,
    Phone NVARCHAR(15) NULL,
    Email NVARCHAR(80) NULL,
    Aadhar_No NVARCHAR(20) NULL,
    Acc_Type NVARCHAR(20) NULL,
    Status NVARCHAR(15) NULL,
    Balance DECIMAL(15,2) NULL
);
GO

*/



/* 
-- Drop Transaction Table if exists
IF OBJECT_ID('dbo.[Transaction]', 'U') IS NOT NULL
    DROP TABLE dbo.[Transaction];          -- Transaction is a 'Reserved Keyword' that's why i use [Transaction]
GO

-- Create Transaction Table
CREATE TABLE dbo.[Transaction] (
    Tid INT IDENTITY(1,1) PRIMARY KEY,
    Dot DATE NULL,
    Amount DECIMAL(15,2) NULL,
    Type NVARCHAR(20) NULL,
    Acno INT NULL,
    CONSTRAINT FK_Transaction_Customer FOREIGN KEY (Acno) REFERENCES dbo.Customer(Acno)
);
*/




-- select @@SERVERNAME  -- for getting the server name
-- select @@VERSION     -- for getting the version of SQL Server
-- select @@LANGUAGE    -- for getting the language of SQL Server

