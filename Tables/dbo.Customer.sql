CREATE TABLE [dbo].[Customer] (
  [Acno] [int] IDENTITY,
  [Name] [nvarchar](30) NULL,
  [Address] [nvarchar](100) NULL,
  [Phone] [nvarchar](15) NULL,
  [Email] [nvarchar](80) NULL,
  [Aadhar_No] [nvarchar](20) NULL,
  [Acc_Type] [nvarchar](20) NULL,
  [Status] [nvarchar](15) NULL,
  [Balance] [decimal](15, 2) NULL,
  PRIMARY KEY CLUSTERED ([Acno])
)
ON [PRIMARY]
GO