CREATE TABLE [dbo].[Transaction] (
  [Tid] [int] IDENTITY,
  [Dot] [date] NULL,
  [Amount] [decimal](15, 2) NULL,
  [Type] [nvarchar](20) NULL,
  [Acno] [int] NULL,
  PRIMARY KEY CLUSTERED ([Tid])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[Transaction]
  ADD CONSTRAINT [FK_Transaction_Customer] FOREIGN KEY ([Acno]) REFERENCES [dbo].[Customer] ([Acno])
GO