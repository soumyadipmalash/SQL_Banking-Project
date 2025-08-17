
/*

-- Insert Data into Customer Table
SET IDENTITY_INSERT dbo.Customer ON;
INSERT INTO dbo.Customer (Acno, Name, Address, Phone, Email, Aadhar_No, Acc_Type, Status, Balance) VALUES
(1, 'Soumyadip Malash', 'Salboni,Paschim Medinipur', '987181818', 'soumyadipmalash@gmail.com', '1234-1243-4545', 'saving', 'active', 12200.00),
(2, 'Swapan Malash', 'Salboni,Paschim Medinipur', '9673844318', 'swapanmalashslb@gmail.com', '4545-1243-4545', 'current', 'active', 10000.00),
(3, 'Ruma Malash', 'Salboni,Paschim Medinipur', '4545456', 'rumamalas@gmail.com', '1234-5656-4545', 'saving', 'active', 10000.00);
SET IDENTITY_INSERT dbo.Customer OFF;
GO

*/

select * from Customer;





/*

-- Insert Data into Transaction Table
SET IDENTITY_INSERT dbo.[Transaction] ON;
INSERT INTO dbo.[Transaction] (Tid, Dot, Amount, Type, Acno) VALUES
(1, '2025-10-16', 2000, 'deposit', 1),
(2, '2025-10-15', 2000, 'deposit', 2),
(3, '2025-10-18', 1200, 'withdraw', 1);
SET IDENTITY_INSERT dbo.[Transaction] OFF;
GO

*/

select * from dbo.[Transaction];